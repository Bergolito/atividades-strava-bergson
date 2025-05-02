#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para processar arquivos GPX do Strava e extrair coordenadas.

Este script lê todos os arquivos GPX da pasta 'mapas-gpx', extrai as coordenadas
de latitude, longitude e elevação, e salva os resultados em arquivos CSV
na pasta 'datasets/mapas'.
"""

import os
import glob
import gpxpy
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('log_processamento_gpx.txt')
    ]
)
logger = logging.getLogger(__name__)

# Diretórios
INPUT_DIR = 'activities-gpx'
OUTPUT_DIR = 'datasets/mapas'

#====================================================================================
def criar_diretorios():
    """Cria os diretórios necessários para o processamento."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    logger.info(f"Verificação de diretórios concluída. Diretório de saída: {OUTPUT_DIR}")
#====================================================================================
def processar_arquivo_gpx(arquivo_gpx):
    """
    Processa um arquivo GPX e extrai coordenadas de latitude, longitude e elevação.
    
    Args:
        arquivo_gpx: Caminho para o arquivo GPX
        
    Returns:
        DataFrame pandas com as coordenadas extraídas
    """
    try:
        with open(arquivo_gpx, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
            
        route_info = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    # Extrair informações de cada ponto
                    info = {
                        'latitude': point.latitude,
                        'longitude': point.longitude,
                        'elevation': point.elevation,
                    }
                    
                    # Adicionar data/hora se disponível
                    if point.time:
                        info['timestamp'] = point.time
                        
                    # Adicionar dados de extensão se disponíveis
                    if hasattr(point, 'extensions') and point.extensions:
                        for ext in point.extensions:
                            for child in ext:
                                if '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}' in child.tag:
                                    tag = child.tag.split('}')[1]
                                    info[tag] = child.text
                    
                    route_info.append(info)
                    
        return pd.DataFrame(route_info)
    
    except Exception as e:
        logger.error(f"Erro ao processar o arquivo {arquivo_gpx}: {str(e)}")
        return None
#====================================================================================
def processar_todos_arquivos():
    """Processa todos os arquivos GPX no diretório de entrada."""
    arquivos_gpx = glob.glob(os.path.join(INPUT_DIR, '*.gpx'))
    
    if not arquivos_gpx:
        logger.warning(f"Nenhum arquivo GPX encontrado no diretório: {INPUT_DIR}")
        return
    
    logger.info(f"Encontrados {len(arquivos_gpx)} arquivos GPX para processamento")
    
    for arquivo_gpx in arquivos_gpx:
        nome_arquivo = os.path.basename(arquivo_gpx)
        nome_base = os.path.splitext(nome_arquivo)[0]
        arquivo_saida = os.path.join(OUTPUT_DIR, f"{nome_base}.csv")
        
        logger.info(f"Processando arquivo: {nome_arquivo}")
        
        df = processar_arquivo_gpx(arquivo_gpx)
        
        if df is not None:
            # Calcular distância entre pontos consecutivos (em metros)
            if len(df) > 1:
                try:
                    from geopy.distance import distance
                    
                    # Lista para armazenar as distâncias
                    distances = [0]  # O primeiro ponto tem distância 0
                    
                    # Calcular a distância entre pontos consecutivos
                    for i in range(1, len(df)):
                        ponto_anterior = (df['latitude'].iloc[i-1], df['longitude'].iloc[i-1])
                        ponto_atual = (df['latitude'].iloc[i], df['longitude'].iloc[i])
                        dist = distance(ponto_anterior, ponto_atual).meters
                        distances.append(dist)
                    
                    # Adicionar a coluna de distância ao DataFrame
                    df['distance'] = distances
                    
                    # Adicionar distância acumulada
                    df['distance_cumulative'] = df['distance'].cumsum()
                    
                except ImportError:
                    logger.warning("Biblioteca geopy não encontrada. A distância entre pontos não será calculada.")
            
            # Salvar DataFrame como CSV
            df.to_csv(arquivo_saida, index=False)
            logger.info(f"Arquivo processado com sucesso. Saída: {arquivo_saida}")
            logger.info(f"Total de pontos extraídos: {len(df)}")
        else:
            logger.error(f"Falha ao processar o arquivo: {nome_arquivo}")
#====================================================================================
def main():
    """Função principal."""
    logger.info("Iniciando processamento de arquivos GPX")
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
