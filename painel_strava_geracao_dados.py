# =======================================================
# Imports
# =======================================================
import pandas as pd

from painel_strava_agrupamentos import *

# =======================================================
# Carregamento dos Datasets
# =======================================================

# =======================================================
# Datasets
# =======================================================
df_atividades_todos = pd.read_csv('datasets/atividades_fisicas_todos.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2020 = pd.read_csv('datasets/atividades_fisicas_2020.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2021 = pd.read_csv('datasets/atividades_fisicas_2021.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2022 = pd.read_csv('datasets/atividades_fisicas_2022.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2023 = pd.read_csv('datasets/atividades_fisicas_2023.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2024 = pd.read_csv('datasets/atividades_fisicas_2024.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2025 = pd.read_csv('datasets/atividades_fisicas_2025.csv', sep=',', encoding="ISO-8859-1")

df_atividades_simplificado_todos = pd.read_csv('datasets/atividades_fisicas_simplificado_todos.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2020 = pd.read_csv('datasets/atividades_fisicas_simplificado_2020.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2021 = pd.read_csv('datasets/atividades_fisicas_simplificado_2021.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2022 = pd.read_csv('datasets/atividades_fisicas_simplificado_2022.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2023 = pd.read_csv('datasets/atividades_fisicas_simplificado_2023.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2024 = pd.read_csv('datasets/atividades_fisicas_simplificado_2024.csv', sep=',', encoding="UTF-8")
df_atividades_simplificado_2025 = pd.read_csv('datasets/atividades_fisicas_simplificado_2025.csv', sep=',', encoding="ISO-8859-1")

# =======================================================
# Funções
# =======================================================
def gera_dados_gerais():

  # gera dados dos tipos de atividades
  gera_dados_gerais_tipo_atividades()

  # gera dados dos dias da semana 
  gera_dados_gerais_dia_semana_atividades()

# =======================================================
def gera_dados_gerais_tipo_atividades():

  processa_atividades_geral_tipo_ano_mes()
  processa_atividades_geral_tipo_ano_mes()

# =======================================================
def gera_dados_gerais_dia_semana_atividades():

  processa_atividades_geral_dia_semana_ano()
  processa_atividades_geral_dia_semana_ano_mes()
# =======================================================



# =======================================================
# main 
# =======================================================

gera_dados_gerais()

