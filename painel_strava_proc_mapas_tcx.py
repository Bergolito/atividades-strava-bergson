#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para processar arquivos TCX (Training Center XML) e extrair coordenadas.

Este script lê todos os arquivos TCX da pasta 'INPUT', extrai as coordenadas
de latitude, longitude, elevação e outras informações relevantes, e salva os 
resultados em arquivos CSV na pasta 'OUTPUT'.
"""

import os
import glob
import pandas as pd
import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('log_processamento_tcx.txt')
    ]
)
logger = logging.getLogger(__name__)

# Diretórios
INPUT_DIR = 'INPUT'
OUTPUT_DIR = 'OUTPUT'

# Namespace padrão usado nos arquivos TCX da Garmin/Strava
NAMESPACES = {
    'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
    'ns2': 'http://www.garmin.com/xmlschemas/UserProfile/v2',
    'ns3': 'http://www.garmin.com/xmlschemas/ActivityExtension/v2',
    'ns4': 'http://www.garmin.com/xmlschemas/ProfileExtension/v1',
    'ns5': 'http://www.garmin.com/xmlschemas/ActivityGoals/v1'
}

#====================================================================================
def criar_diretorios():
    """Cria os diretórios necessários para o processamento."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    logger.info(f"Verificação de diretórios concluída. Diretório de saída: {OUTPUT_DIR}")

#====================================================================================
def processar_arquivo_tcx(arquivo_tcx):
    """
    Processa um arquivo TCX e extrai coordenadas e outras informações relevantes.
    
    Args:
        arquivo_tcx: Caminho para o arquivo TCX
        
    Returns:
        DataFrame pandas com as informações extraídas
    """
    try:
        # Parsear o arquivo XML
        tree = ET.parse(arquivo_tcx)
        root = tree.getroot()
        
        # Lista para armazenar os dados de cada trackpoint
        trackpoints_data = []
        
        # Extrair informações básicas da atividade
        activity_element = root.find('.//ns:Activity', NAMESPACES)
        
        # Tipo de esporte (corrida, ciclismo, etc.)
        sport_type = activity_element.attrib.get('Sport', 'Unknown') if activity_element is not None else 'Unknown'
        
        # Data e ID da atividade
        activity_id = root.find('.//ns:Id', NAMESPACES)
        activity_id_text = activity_id.text if activity_id is not None else 'Unknown'
        
        # Encontrar todos os trackpoints
        trackpoints = root.findall('.//ns:Trackpoint', NAMESPACES)
        
        # Extrair dados de cada trackpoint
        for trackpoint in trackpoints:
            # Dados básicos
            point_data = {
                'activity_id': activity_id_text,
                'sport_type': sport_type
            }
            
            # Timestamp
            time_elem = trackpoint.find('./ns:Time', NAMESPACES)
            if time_elem is not None:
                point_data['timestamp'] = time_elem.text
            
            # Posição (latitude/longitude)
            position = trackpoint.find('./ns:Position', NAMESPACES)
            if position is not None:
                lat_elem = position.find('./ns:LatitudeDegrees', NAMESPACES)
                lon_elem = position.find('./ns:LongitudeDegrees', NAMESPACES)
                
                if lat_elem is not None and lon_elem is not None:
                    point_data['latitude'] = float(lat_elem.text)
                    point_data['longitude'] = float(lon_elem.text)
            
            # Altitude
            altitude_elem = trackpoint.find('./ns:AltitudeMeters', NAMESPACES)
            if altitude_elem is not None:
                point_data['altitude'] = float(altitude_elem.text)
            
            # Distância
            distance_elem = trackpoint.find('./ns:DistanceMeters', NAMESPACES)
            if distance_elem is not None:
                point_data['distance'] = float(distance_elem.text)
            
            # Frequência cardíaca
            heart_rate = trackpoint.find('.//ns:HeartRateBpm/ns:Value', NAMESPACES)
            if heart_rate is not None:
                point_data['heart_rate'] = int(heart_rate.text)
            
            # Cadência
            cadence = trackpoint.find('./ns:Cadence', NAMESPACES)
            if cadence is not None:
                point_data['cadence'] = int(cadence.text)
            
            # Extensões (potência, etc.)
            extensions = trackpoint.find('.//ns3:TPX', NAMESPACES)
            if extensions is not None:
                # Potência (Watts)
                power = extensions.find('.//ns3:Watts', NAMESPACES)
                if power is not None:
                    point_data['power'] = float(power.text)
                
                # Velocidade
                speed = extensions.find('.//ns3:Speed', NAMESPACES)
                if speed is not None:
                    point_data['speed'] = float(speed.text)
            
            # Adicionar ponto à lista se tiver pelo menos latitude e longitude
            if 'latitude' in point_data and 'longitude' in point_data:
                trackpoints_data.append(point_data)
        
        # Criar DataFrame com os dados extraídos
        df = pd.DataFrame(trackpoints_data)
        
        # Se tivermos pontos suficientes, calcular campos adicionais
        if len(df) > 0:
            # Calcular velocidade entre pontos se não disponível nas extensões
            if 'speed' not in df.columns and 'timestamp' in df.columns and 'distance' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['time_diff'] = df['timestamp'].diff().dt.total_seconds()
                df['distance_diff'] = df['distance'].diff()
                # Calcular velocidade em m/s
                df.loc[df['time_diff'] > 0, 'calculated_speed'] = df['distance_diff'] / df['time_diff']
            
            # Calcular inclinação se tivermos altitude e distância
            if 'altitude' in df.columns and 'distance' in df.columns:
                df['altitude_diff'] = df['altitude'].diff()
                df['distance_diff'] = df['distance'].diff()
                # Evitar divisão por zero
                df.loc[df['distance_diff'] > 0, 'gradient'] = (df['altitude_diff'] / df['distance_diff']) * 100
        
        return df
    
    except Exception as e:
        logger.error(f"Erro ao processar o arquivo {arquivo_tcx}: {str(e)}")
        return None

#====================================================================================
def processar_todos_arquivos():
    """Processa todos os arquivos TCX no diretório de entrada."""
    arquivos_tcx = glob.glob(os.path.join(INPUT_DIR, '*.tcx'))
    
    if not arquivos_tcx:
        logger.warning(f"Nenhum arquivo TCX encontrado no diretório: {INPUT_DIR}")
        return
    
    logger.info(f"Encontrados {len(arquivos_tcx)} arquivos TCX para processamento")
    
    arquivos_processados = 0
    
    for arquivo_tcx in arquivos_tcx:
        nome_arquivo = os.path.basename(arquivo_tcx)
        nome_base = os.path.splitext(nome_arquivo)[0]
        arquivo_saida = os.path.join(OUTPUT_DIR, f"{nome_base}.csv")
        
        logger.info(f"Processando arquivo: {nome_arquivo}")
        
        df = processar_arquivo_tcx(arquivo_tcx)
        
        if df is not None and not df.empty:
            # Salvar DataFrame como CSV
            df.to_csv(arquivo_saida, index=False)
            logger.info(f"Arquivo processado com sucesso. Saída: {arquivo_saida}")
            logger.info(f"Total de pontos extraídos: {len(df)}")
            arquivos_processados += 1
        else:
            logger.error(f"Falha ao processar o arquivo: {nome_arquivo} ou nenhum ponto extraído.")
    
    logger.info(f"Total de arquivos processados com sucesso: {arquivos_processados} de {len(arquivos_tcx)}")

#====================================================================================
def main():
    """Função principal."""
    logger.info("Iniciando processamento de arquivos TCX")
    inicio = datetime.now()
    
    criar_diretorios()
    processar_todos_arquivos()
    
    fim = datetime.now()
    duracao = fim - inicio
    logger.info(f"Processamento concluído. Tempo total: {duracao}")

#====================================================================================

# ============================
# Executa o script
# ============================
if __name__ == "__main__":
    main()