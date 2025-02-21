# =======================================================
# Imports
# =======================================================
import pandas as pd

from tcc_painel_funcoes_agrupamento import *

# =======================================================
# Carregamento dos Datasets
# =======================================================
df_pessoa_acidentes_2007 = pd.read_csv('../PRF/por_pessoa/acidentes2007.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2008 = pd.read_csv('../PRF/por_pessoa/acidentes2008.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2009 = pd.read_csv('../PRF/por_pessoa/acidentes2009.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2010 = pd.read_csv('../PRF/por_pessoa/acidentes2010.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2011 = pd.read_csv('../PRF/por_pessoa/acidentes2011.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2012 = pd.read_csv('../PRF/por_pessoa/acidentes2012.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2013 = pd.read_csv('../PRF/por_pessoa/acidentes2013.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2014 = pd.read_csv('../PRF/por_pessoa/acidentes2014.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2015 = pd.read_csv('../PRF/por_pessoa/acidentes2015.csv', sep=',', encoding="ISO-8859-1")
df_pessoa_acidentes_2016 = pd.read_csv('../PRF/por_pessoa/acidentes2016.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2017 = pd.read_csv('../PRF/por_pessoa/acidentes2017.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2018 = pd.read_csv('../PRF/por_pessoa/acidentes2018.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2019 = pd.read_csv('../PRF/por_pessoa/acidentes2019.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2020 = pd.read_csv('../PRF/por_pessoa/acidentes2020.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2021 = pd.read_csv('../PRF/por_pessoa/acidentes2021.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2022 = pd.read_csv('../PRF/por_pessoa/acidentes2022.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2023 = pd.read_csv('../PRF/por_pessoa/acidentes2023.csv', sep=';', encoding="ISO-8859-1")
df_pessoa_acidentes_2024 = pd.read_csv('../PRF/por_pessoa/acidentes2024.csv', sep=';', encoding="ISO-8859-1")

# =======================================================
# Datasets por ocorrencias
# =======================================================
df_por_ocorrencia_2007 = pd.read_csv('../PRF/por_ocorrencia/datatran2007.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2008 = pd.read_csv('../PRF/por_ocorrencia/datatran2008.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2009 = pd.read_csv('../PRF/por_ocorrencia/datatran2009.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2010 = pd.read_csv('../PRF/por_ocorrencia/datatran2010.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2011 = pd.read_csv('../PRF/por_ocorrencia/datatran2011.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2012 = pd.read_csv('../PRF/por_ocorrencia/datatran2012.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2013 = pd.read_csv('../PRF/por_ocorrencia/datatran2013.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2014 = pd.read_csv('../PRF/por_ocorrencia/datatran2014.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2015 = pd.read_csv('../PRF/por_ocorrencia/datatran2015.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2016 = pd.read_csv('../PRF/por_ocorrencia/datatran2016.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2017 = pd.read_csv('../PRF/por_ocorrencia/datatran2017.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2018 = pd.read_csv('../PRF/por_ocorrencia/datatran2018.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2019 = pd.read_csv('../PRF/por_ocorrencia/datatran2019.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2020 = pd.read_csv('../PRF/por_ocorrencia/datatran2020.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2021 = pd.read_csv('../PRF/por_ocorrencia/datatran2021.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2022 = pd.read_csv('../PRF/por_ocorrencia/datatran2022.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2023 = pd.read_csv('../PRF/por_ocorrencia/datatran2023.csv', sep=';', encoding="ISO-8859-1")
df_por_ocorrencia_2024 = pd.read_csv('../PRF/por_ocorrencia/datatran2024.csv', sep=';', encoding="ISO-8859-1")


# =======================================================
# Funções
# =======================================================
def gera_dados_gerais():

  # gera dados das ufs
  gera_dados_gerais_uf()

  # tipo
  gera_dados_gerais_tipo()

  # br
  gera_dados_gerais_br()

  # causa"
  gera_dados_gerais_causa()

  # Classificação
  gera_dados_gerais_classificacao()

  # Fase do Dia
  gera_dados_gerais_fasedia()

  # Condição Metereológica
  gera_dados_gerais_condicao_metereologica()

  # Dia da Semana
  gera_dados_gerais_dia_semana()

  # Tipo de Veículo
  gera_dados_gerais_tipo_veiculo()

# =======================================================
def gera_dados_gerais_uf():
   
  processa_acidentes_geral_ufs(10)
  processa_acidentes_geral_ufs(20)
  processa_acidentes_geral_ufs(27)
# =======================================================
def gera_dados_gerais_tipo():

  processa_acidentes_geral_tipo()

# =======================================================
def gera_dados_gerais_br():

  #processa_acidentes_geral_br(10)
  #processa_acidentes_geral_br(20)
  #processa_acidentes_geral_br(30)
  processa_acidentes_geral_br(40)
  #processa_acidentes_geral_br(50)

# =======================================================
def gera_dados_gerais_causa():
  
  processa_acidentes_geral_causa()

# =======================================================
def gera_dados_gerais_classificacao():
  
  processa_acidentes_geral_classificacao()

# =======================================================
def gera_dados_gerais_fasedia():

  processa_acidentes_geral_fase_dia()

# =======================================================
def gera_dados_gerais_condicao_metereologica():
  
  processa_acidentes_geral_condicao_metereologica()

# =======================================================
def gera_dados_gerais_dia_semana():
  
  processa_acidentes_geral_dia_semana()

# =======================================================
def gera_dados_gerais_tipo_veiculo():
  
  processa_acidentes_geral_tipo_veiculo

# =======================================================

# =======================================================
# main 
# =======================================================
gera_dados_gerais()
gera_dados_gerais_br()

