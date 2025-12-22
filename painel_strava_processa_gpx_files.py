# =======================================================
# Imports
# =======================================================
#import pandas as pd
import os

from datetime import datetime
from painel_strava_funcoes import *
from tcx2gpx.tcx2gpx import TCX2GPX

# ==================================
# Funções
# ==================================
"""
Converte um arquivo TCX para GPX.
"""
def convert_tcx_to_gpx(file_to_convert):

    # Cria um objeto TCX2GPX e converte o arquivo
    gps_object = TCX2GPX(tcx_path=file_to_convert)
    gps_object.convert()

# ==================================
def converte_arquivos_tcx():
    """
    Busca todos os arquivos TCX na pasta 'activities-tcx' e os converte para GPX.
    """
    # Pasta com os arquivos TCX
    tcx_folder = "teste-convert"
    
    # Verifica se a pasta existe
    if not os.path.exists(tcx_folder):
        print(f"A pasta '{tcx_folder}' não existe.")
        return
    
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(tcx_folder)
    
    # Filtra apenas os arquivos TCX
    arquivos_tcx = [arquivo for arquivo in arquivos if arquivo.lower().endswith('.tcx')]
    
    if len(arquivos_tcx) == 0:
        print(f"Nenhum arquivo TCX encontrado na pasta '{tcx_folder}'.")
        return
    
    print(f"Encontrados {len(arquivos_tcx)} arquivos TCX para conversão.")
    
    # Contador de arquivos convertidos
    convertidos = 0
    
    # Converte cada arquivo TCX
    for arquivo in arquivos_tcx:
        caminho_completo = os.path.join(tcx_folder, arquivo)
        try:
            print(f"Convertendo {arquivo}...")
            convert_tcx_to_gpx(caminho_completo)
            convertidos += 1
        except Exception as e:
            print(f"Erro ao converter {arquivo}: {str(e)}")
    
    print(f"Processo concluído. {convertidos} de {len(arquivos_tcx)} arquivos convertidos com sucesso.")

# ==================================
def move_arquivos_gpx_pasta_correta():
  # lista os arquivos GPX da pasta
  arquivos_gpx = os.listdir('activities-tcx')
  # Verifica se a pasta existe
  if not os.path.exists('activities-gpx'):
    os.makedirs('activities-gpx')
  # Move os arquivos GPX para a pasta correta
  for arquivo in arquivos_gpx:
    if arquivo.lower().endswith('.gpx'):
      caminho_origem = os.path.join('activities-tcx', arquivo)
      caminho_destino = os.path.join('teste-convert/convertidos', arquivo)
      os.rename(caminho_origem, caminho_destino)
      print(f"Arquivo {arquivo} movido para a pasta 'activities-gpx'.")

# ==================================
# ATENÇÂO
# ==================================

# ==================================
if __name__ == "__main__":
  # Executa o código
  converte_arquivos_tcx()
  #move_arquivos_gpx_pasta_correta()
# ==================================
