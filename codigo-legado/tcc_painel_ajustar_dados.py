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

# =======================================================      
def ajusta_dia_semana(value):
    if value == 'domingo' or value == 'Domingo':
        return 'Domingo'
        
    elif value == 'segunda' or value == 'segunda-feira':    
        return 'Segunda-feira'
        
    elif value == 'terça' or value == 'terça-feira':    
        return 'Terça-feira'
        
    elif value == 'quarta' or value == 'quarta-feira':    
        return 'Quarta-feira'
        
    elif value == 'quinta' or value == 'quinta-feira':    
        return 'Quinta-feira'
        
    elif value == 'sexta' or value == 'sexta-feira':    
        return 'Sexta-feira'
        
    elif value == 'sábado' or value == 'Sábado':    
        return 'Sábado'    

    return value
# =======================================================      
def ajusta_fase_dia(value):
    if value == 'Plena noite' or value == 'Plena Noite':
        return 'Plena Noite'

    return value
# =======================================================      
# renomear 'Ceu Claro' para 'Céu Claro'
# renomear 'Ignorada' para 'Ignorado'
# renomear 'Nevoeiro/neblina' para 'Nevoeiro/Neblina'
def ajusta_condicao_metereologica(value):
    if value == 'Ceu Claro':
        return 'Céu Claro'
        
    elif value == 'Ignorada':    
        return 'Ignorado'
        
    elif value == 'Nevoeiro/neblina':    
        return 'Nevoeiro/Neblina'

    return value
# =======================================================
def ajusta_dados_dia_semana():
  df_acidentes_geral_por_dia_semana = pd.read_csv('datasets/gerais/acidentes_geral_por_dia_semana.csv', sep=',', encoding="UTF-8") 

  df = df_acidentes_geral_por_dia_semana

  df['dia_semana'] = df['dia_semana'].str.strip()
  df['dia_semana'] = df['dia_semana'].str.lstrip()
  df['dia_semana'] = df['dia_semana'].apply(ajusta_dia_semana)

  df.to_csv('datasets/gerais/acidentes_geral_por_dia_semana.csv', sep=',', encoding="UTF-8")  
# =======================================================
def ajusta_dados_fase_dia():

  df_acidentes_geral_por_fase_dia = pd.read_csv('datasets/gerais/acidentes_geral_por_fase_dia.csv', sep=',', encoding="UTF-8") 

  df = df_acidentes_geral_por_fase_dia

  df['fase_dia'] = df['fase_dia'].str.strip()
  df['fase_dia'] = df['fase_dia'].str.lstrip()
  df['fase_dia'] = df['fase_dia'].apply(ajusta_fase_dia)

  df.to_csv('datasets/gerais/acidentes_geral_por_fase_dia.csv', sep=',', encoding="UTF-8")  
# =======================================================
def ajusta_dados_condicao_metereologica():

  df_acidentes_geral_por_condicao_metereologica = pd.read_csv('datasets/gerais/acidentes_geral_por_condicao_metereologica.csv', sep=',', encoding="UTF-8") 

  df = df_acidentes_geral_por_condicao_metereologica

  # remover '(null)',
  # renomear 'Ceu Claro' para 'Céu Claro'
  # renomear 'Ignorada' para 'Ignorado'
  # renomear 'Nevoeiro/neblina' para 'Nevoeiro/Neblina'

  df_limpo = df[(df['condicao_metereologica'] != '(null)')]

  df_limpo['condicao_metereologica'] = df_limpo['condicao_metereologica'].apply(ajusta_condicao_metereologica)

  df_limpo.to_csv('datasets/gerais/acidentes_geral_por_condicao_metereologica-2.csv', sep=',', encoding="UTF-8")  

# =======================================================
def ajusta_dados_causas_acidentes():
  df_acidentes_geral_por_causa = pd.read_csv('datasets/gerais/acidentes_geral_por_causa.csv', sep=',', encoding="UTF-8") 

  df = df_acidentes_geral_por_causa

  df['causa_acidente'] = df['causa_acidente'].str.strip()
  df['causa_acidente'] = df['causa_acidente'].str.lstrip()
  df['causa_acidente'] = df['causa_acidente'].apply(ajusta_causa_acidente)

  df.to_csv('datasets/gerais/acidentes_geral_por_causa.csv', sep=',', encoding="UTF-8")  

# =======================================================      
def ajusta_causa_acidente(value):
    # Defeito mecânico em veículo / Defeito Mecânico no Veículo
    if value == 'Defeito mecânico em veículo':
        return 'Defeito Mecânico no Veículo'

    # Defeito na via
    elif value == 'Defeito na via':
        return 'Defeito na Via'

    # Falta de atenção / Falta de Atenção à Condução
    elif value == 'Falta de atenção':
        return 'Falta de Atenção à Condução'
    
    # Ingestão de álcool / Ingestão de Álcool
    elif value == 'Ingestão de álcool':
        return 'Ingestão de Álcool'
    
    # Defeito na via / Defeito na Via
    elif value == 'Defeito na via':
        return 'Defeito na Via'
    
    # Ultrapassagem indevida / Ultrapassagem Indevida
    elif value == 'Ultrapassagem indevida':
        return 'Ultrapassagem Indevida'
    
    # Velocidade incompatível / Velocidade Incompatível
    elif value == 'Velocidade incompatível':
        return 'Velocidade Incompatível'

    return value
# =======================================================
# main 
# =======================================================

ajusta_dados_dia_semana()

ajusta_dados_fase_dia()

ajusta_dados_condicao_metereologica()

ajusta_dados_causas_acidentes()