# =======================================================
# Imports
# =======================================================
import pandas as pd

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
def agrupamento_acidentes_por_ano_por_uf(df):
  contagem_por_uf = df['uf'].value_counts().reset_index()
  contagem_por_uf.columns = ['uf', 'qtd']
  return contagem_por_uf
# =======================================================
def agrupamento_acidentes_por_ano_por_br(df):
  contagem_por_br = df['br'].value_counts().reset_index()
  contagem_por_br.columns = ['br', 'qtd']
  return contagem_por_br
# =======================================================
def agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes):
  contagem_por_tipo = df_ocorrencia_acidentes['tipo_acidente'].value_counts().reset_index()
  contagem_por_tipo.columns = ['tipo_acidente', 'qtd']
  return contagem_por_tipo
# =======================================================  
def agrupamento_acidentes_por_ano_por_causa(df):
  contagem_por_causa = df['causa_acidente'].value_counts().reset_index()
  contagem_por_causa.columns = ['causa_acidente', 'qtd']
  return contagem_por_causa    
# =======================================================
def agrupamento_acidentes_por_ano_por_classificacao(df):
  contagem_por_classificacao = df['classificacao_acidente'].value_counts().reset_index()
  contagem_por_classificacao.columns = ['classificacao_acidente', 'qtd']
  return contagem_por_classificacao    
# =======================================================
def agrupamento_acidentes_por_ano_por_fase_dia(df):
  contagem_por_fase_dia = df['fase_dia'].value_counts().reset_index(name='qtd')
  contagem_por_fase_dia.columns = ['fase_dia', 'qtd']
  return contagem_por_fase_dia    
# =======================================================
def agrupamento_acidentes_por_ano_por_condicao_metereologica(df):
  contagem_por_condicao_meteorologica = df['condicao_metereologica'].value_counts().reset_index(name='qtd')
  contagem_por_condicao_meteorologica.columns = ['condicao_metereologica', 'qtd']
  return contagem_por_condicao_meteorologica       
# =======================================================
def agrupamento_acidentes_por_ano_por_dia_semana(df):
  contagem_por_dia_semana = df['dia_semana'].value_counts().reset_index(name='qtd')
  contagem_por_dia_semana.columns = ['dia_semana', 'qtd']
  return contagem_por_dia_semana         
# =======================================================
def agrupamento_acidentes_por_ano_por_tipo_veiculo(df):
  contagem_por_tipo_veiculo = df['tipo_veiculo'].value_counts().reset_index(name='qtd')
  contagem_por_tipo_veiculo.columns = ['tipo_veiculo', 'qtd']
  return contagem_por_tipo_veiculo
# =======================================================
def processa_acidentes_geral_tipo_veiculo():
    
    contagem_por_tipo_veiculo_2007 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2007)
    contagem_por_tipo_veiculo_2008 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2008)
    contagem_por_tipo_veiculo_2009 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2009)
    contagem_por_tipo_veiculo_2010 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2010)
    contagem_por_tipo_veiculo_2011 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2011)
    contagem_por_tipo_veiculo_2012 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2012)
    contagem_por_tipo_veiculo_2013 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2013)
    contagem_por_tipo_veiculo_2014 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2014)
    contagem_por_tipo_veiculo_2015 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2015)
    contagem_por_tipo_veiculo_2016 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2016)
    contagem_por_tipo_veiculo_2017 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2017)
    contagem_por_tipo_veiculo_2018 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2018)
    contagem_por_tipo_veiculo_2019 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2019)
    contagem_por_tipo_veiculo_2020 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2020)
    contagem_por_tipo_veiculo_2021 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2021)
    contagem_por_tipo_veiculo_2022 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2022)
    contagem_por_tipo_veiculo_2023 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2023)
    contagem_por_tipo_veiculo_2024 = agrupamento_acidentes_por_ano_por_tipo_veiculo(df_pessoa_acidentes_2024)
    
    contagem_por_tipo_veiculo_2007['ano'] = '2007'
    contagem_por_tipo_veiculo_2008['ano'] = '2008'
    contagem_por_tipo_veiculo_2009['ano'] = '2009'
    contagem_por_tipo_veiculo_2010['ano'] = '2010'
    contagem_por_tipo_veiculo_2011['ano'] = '2011'
    contagem_por_tipo_veiculo_2012['ano'] = '2012'
    contagem_por_tipo_veiculo_2013['ano'] = '2013'
    contagem_por_tipo_veiculo_2014['ano'] = '2014'
    contagem_por_tipo_veiculo_2015['ano'] = '2015'
    contagem_por_tipo_veiculo_2016['ano'] = '2016'
    contagem_por_tipo_veiculo_2017['ano'] = '2017'
    contagem_por_tipo_veiculo_2018['ano'] = '2018'
    contagem_por_tipo_veiculo_2019['ano'] = '2019'
    contagem_por_tipo_veiculo_2020['ano'] = '2020'
    contagem_por_tipo_veiculo_2021['ano'] = '2021'
    contagem_por_tipo_veiculo_2022['ano'] = '2022'
    contagem_por_tipo_veiculo_2023['ano'] = '2023'
    contagem_por_tipo_veiculo_2024['ano'] = '2024'

    acidentes_por_tipo_veiculo_concatenados = pd.concat(
    [
      contagem_por_tipo_veiculo_2007, contagem_por_tipo_veiculo_2008, contagem_por_tipo_veiculo_2009,
      contagem_por_tipo_veiculo_2010, contagem_por_tipo_veiculo_2011, contagem_por_tipo_veiculo_2012,
      contagem_por_tipo_veiculo_2013, contagem_por_tipo_veiculo_2014, contagem_por_tipo_veiculo_2015,
      contagem_por_tipo_veiculo_2016, contagem_por_tipo_veiculo_2017, contagem_por_tipo_veiculo_2018,
      contagem_por_tipo_veiculo_2019, contagem_por_tipo_veiculo_2020, contagem_por_tipo_veiculo_2021,
      contagem_por_tipo_veiculo_2022, contagem_por_tipo_veiculo_2023, contagem_por_tipo_veiculo_2024
    
    ], axis=0)
    
    lista_tipos_veiculos = []
    
    for item in acidentes_por_tipo_veiculo_concatenados['tipo_veiculo'].unique():
      lista_tipos_veiculos.append(item)
    lista_tipos_veiculos.remove('(null)')
    
    lista_tipos_veiculos = lista_tipos_veiculos[:10]
    df_tipo_veiculo = acidentes_por_tipo_veiculo_concatenados
    df_geral_tipo_veiculo = pd.DataFrame(columns=['tipo_veiculo','qtd','ano'])
    
    for item in lista_tipos_veiculos:
      df_filtrado_uf = df_tipo_veiculo[(df_tipo_veiculo['tipo_veiculo'] == item)]
      df_geral_tipo_veiculo = pd.concat([df_geral_tipo_veiculo, df_filtrado_uf], ignore_index=True)
        
    df_geral_tipo_veiculo.to_csv('datasets/gerais/acidentes_geral_por_tipo_veiculo.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_tipo_veiculo...')

    return df_geral_tipo_veiculo
# =======================================================
def processa_acidentes_geral_ufs(qtd_ufs):
    
    contagem_por_uf_2007 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2007)
    contagem_por_uf_2008 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2008)
    contagem_por_uf_2009 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2009)
    contagem_por_uf_2010 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2010)
    contagem_por_uf_2011 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2011)
    contagem_por_uf_2012 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2012)
    contagem_por_uf_2013 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2013)
    contagem_por_uf_2014 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2014)
    contagem_por_uf_2015 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2015)
    contagem_por_uf_2016 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2016)
    contagem_por_uf_2017 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2017)
    contagem_por_uf_2018 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2018)
    contagem_por_uf_2019 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2019)
    contagem_por_uf_2020 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2020)
    contagem_por_uf_2021 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2021)
    contagem_por_uf_2022 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2022)
    contagem_por_uf_2023 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2023)
    contagem_por_uf_2024 = agrupamento_acidentes_por_ano_por_uf(df_pessoa_acidentes_2024)
    
    contagem_por_uf_2007['ano'] = '2007'
    contagem_por_uf_2008['ano'] = '2008'
    contagem_por_uf_2009['ano'] = '2009'
    contagem_por_uf_2010['ano'] = '2010'
    contagem_por_uf_2011['ano'] = '2011'
    contagem_por_uf_2012['ano'] = '2012'
    contagem_por_uf_2013['ano'] = '2013'
    contagem_por_uf_2014['ano'] = '2014'
    contagem_por_uf_2015['ano'] = '2015'
    contagem_por_uf_2016['ano'] = '2016'
    contagem_por_uf_2017['ano'] = '2017'
    contagem_por_uf_2018['ano'] = '2018'
    contagem_por_uf_2019['ano'] = '2019'
    contagem_por_uf_2020['ano'] = '2020'
    contagem_por_uf_2021['ano'] = '2021'
    contagem_por_uf_2022['ano'] = '2022'
    contagem_por_uf_2023['ano'] = '2023'
    contagem_por_uf_2024['ano'] = '2024'

    acidentes_por_uf_concatenados = pd.concat(
    [
      contagem_por_uf_2007, contagem_por_uf_2008, contagem_por_uf_2009,
      contagem_por_uf_2010, contagem_por_uf_2011, contagem_por_uf_2012,
      contagem_por_uf_2013, contagem_por_uf_2014, contagem_por_uf_2015,
      contagem_por_uf_2016, contagem_por_uf_2017, contagem_por_uf_2018,
      contagem_por_uf_2019, contagem_por_uf_2020, contagem_por_uf_2021,
      contagem_por_uf_2022, contagem_por_uf_2023, contagem_por_uf_2024
    
    ], axis=0)
    
    lista_ufs = []
    
    for item in acidentes_por_uf_concatenados['uf'].unique():
      lista_ufs.append(item)
    lista_ufs.remove('(null)')
    
    if qtd_ufs is not None:
        lista_ufs = lista_ufs[:qtd_ufs]

    df_uf = acidentes_por_uf_concatenados
    df_geral_uf = pd.DataFrame(columns=['uf','qtd','ano'])
    
    for item in lista_ufs:
      df_filtrado_uf = df_uf[(df_uf['uf'] == item)]
      df_geral_uf = pd.concat([df_geral_uf, df_filtrado_uf], ignore_index=True)

    if qtd_ufs == 10:    
        df_geral_uf.to_csv('datasets/gerais/acidentes_geral_por_uf_10.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_uf_10...')
    elif qtd_ufs == 20:    
        df_geral_uf.to_csv('datasets/gerais/acidentes_geral_por_uf_20.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_uf_20...')
    else:    
        df_geral_uf.to_csv('datasets/gerais/acidentes_geral_por_uf_todos.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_uf_todos...')

    return df_geral_uf
# =======================================================
def processa_acidentes_geral_tipo():

    contagem_por_tipo_2007 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2007)
    contagem_por_tipo_2008 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2008)
    contagem_por_tipo_2009 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2009)
    contagem_por_tipo_2010 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2010)
    contagem_por_tipo_2011 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2011)
    contagem_por_tipo_2012 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2012)
    contagem_por_tipo_2013 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2013)
    contagem_por_tipo_2014 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2014)
    contagem_por_tipo_2015 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2015)
    contagem_por_tipo_2016 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2016)
    contagem_por_tipo_2017 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2017)
    contagem_por_tipo_2018 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2018)
    contagem_por_tipo_2019 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2019)
    contagem_por_tipo_2020 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2020)
    contagem_por_tipo_2021 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2021)
    contagem_por_tipo_2022 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2022)
    contagem_por_tipo_2023 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2023)
    contagem_por_tipo_2024 = agrupamento_acidentes_por_ano_por_tipo(df_ocorrencia_acidentes_2024)
    
    contagem_por_tipo_2007['ano'] = '2007'
    contagem_por_tipo_2008['ano'] = '2008'
    contagem_por_tipo_2009['ano'] = '2009'
    contagem_por_tipo_2010['ano'] = '2010'
    contagem_por_tipo_2011['ano'] = '2011'
    contagem_por_tipo_2012['ano'] = '2012'
    contagem_por_tipo_2013['ano'] = '2013'
    contagem_por_tipo_2014['ano'] = '2014'
    contagem_por_tipo_2015['ano'] = '2015'
    contagem_por_tipo_2016['ano'] = '2016'
    contagem_por_tipo_2017['ano'] = '2017'
    contagem_por_tipo_2018['ano'] = '2018'
    contagem_por_tipo_2019['ano'] = '2019'
    contagem_por_tipo_2020['ano'] = '2020'
    contagem_por_tipo_2021['ano'] = '2021'
    contagem_por_tipo_2022['ano'] = '2022'
    contagem_por_tipo_2023['ano'] = '2023'
    contagem_por_tipo_2024['ano'] = '2024'
    
    
    acidentes_por_tipo_concatenados = pd.concat(
    [
        contagem_por_tipo_2007, contagem_por_tipo_2008, contagem_por_tipo_2009,
        contagem_por_tipo_2010, contagem_por_tipo_2011, contagem_por_tipo_2012,
        contagem_por_tipo_2013, contagem_por_tipo_2014, contagem_por_tipo_2015,
        contagem_por_tipo_2016, contagem_por_tipo_2017, contagem_por_tipo_2018,
        contagem_por_tipo_2019, contagem_por_tipo_2020, contagem_por_tipo_2021,
        contagem_por_tipo_2022, contagem_por_tipo_2023, contagem_por_tipo_2024
    
    ], axis=0)
    
    acidentes_por_tipo_concatenados
    
    df_tipo = acidentes_por_tipo_concatenados
    df_geral_tipo = pd.DataFrame(columns=['tipo_acidente','qtd','ano'])

    lista_acidentes = contagem_por_tipo_2023['tipo_acidente'].unique()
    lista_acidentes = lista_acidentes[:15]
    lista_acidentes
    
    for item in lista_acidentes:
      df_filtrado_tipo = df_tipo[(df_tipo['tipo_acidente'] == item)]
      df_geral_tipo = pd.concat([df_geral_tipo, df_filtrado_tipo], ignore_index=True)
    
    df_geral_tipo
    
    df_geral_tipo.to_csv('datasets/gerais/acidentes_geral_por_tipo.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_tipo.csv...')
    
    return df_geral_tipo
# =======================================================
def processa_acidentes_geral_br(qtd_brs):

    acidentes_br_2007 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2007)
    acidentes_br_2008 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2008)
    acidentes_br_2009 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2009)
    acidentes_br_2010 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2010)
    acidentes_br_2011 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2011)
    acidentes_br_2012 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2012)
    acidentes_br_2013 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2013)
    acidentes_br_2014 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2014)
    acidentes_br_2015 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2015)
    acidentes_br_2016 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2016)
    acidentes_br_2017 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2017)
    acidentes_br_2018 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2018)
    acidentes_br_2019 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2019)
    acidentes_br_2020 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2020)
    acidentes_br_2021 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2021)
    acidentes_br_2022 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2022)
    acidentes_br_2023 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2023)
    acidentes_br_2024 = agrupamento_acidentes_por_ano_por_br(df_pessoa_acidentes_2024)   
   
    acidentes_br_2007['ano'] = '2007'
    acidentes_br_2008['ano'] = '2008'
    acidentes_br_2009['ano'] = '2009'
    acidentes_br_2010['ano'] = '2010'
    acidentes_br_2011['ano'] = '2011'
    acidentes_br_2012['ano'] = '2012'
    acidentes_br_2013['ano'] = '2013'
    acidentes_br_2014['ano'] = '2014'
    acidentes_br_2015['ano'] = '2015'
    acidentes_br_2016['ano'] = '2016'
    acidentes_br_2017['ano'] = '2017'
    acidentes_br_2018['ano'] = '2018'
    acidentes_br_2019['ano'] = '2019'
    acidentes_br_2020['ano'] = '2020'
    acidentes_br_2021['ano'] = '2021'
    acidentes_br_2022['ano'] = '2022'
    acidentes_br_2023['ano'] = '2023'
    acidentes_br_2024['ano'] = '2024'
    
    acidentes_brs_concatenados = pd.concat(
    [
        acidentes_br_2007, acidentes_br_2008, acidentes_br_2009,
        acidentes_br_2010, acidentes_br_2011, acidentes_br_2012,
        acidentes_br_2013, acidentes_br_2014, acidentes_br_2015,
        acidentes_br_2016, acidentes_br_2017, acidentes_br_2018,
        acidentes_br_2019, acidentes_br_2020, acidentes_br_2021,
        acidentes_br_2022, acidentes_br_2023, acidentes_br_2024
    ], axis=0)
    
    df = acidentes_brs_concatenados

    #lista_brs = ['101','116','381','40','153','163','364','227','376','262','230','470','316','282','70','60','20','158','369','50']
    grouped = df.groupby('br')['qtd'].sum().reset_index()

    # Ordena os dados pela quantidade de acidentes em ordem decrescente
    grouped = grouped.sort_values(by='qtd', ascending=False)

    # listar as brs por ordem de acidentes    
    if qtd_brs is not None:
      #lista_brs = grouped['br'].head(qtd_brs).tolist()    
      lista_brs = grouped['br'].tolist()    
      lista_brs = lista_brs[:qtd_brs]
      print(f"Lista de brs ({len(lista_brs)}) = {lista_brs}")
    
    df_geral_br = pd.DataFrame(columns=['br', 'qtd', 'ano'])
    
    for item in lista_brs:
      df_filtrado_br = df[(df['br'] == int(item))]
      df_geral_br = pd.concat([df_geral_br, df_filtrado_br], ignore_index=True)

    if qtd_brs == 10:
        df_geral_br.to_csv('datasets/gerais/acidentes_geral_por_br_10.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_br_10.csv...')
    elif qtd_brs == 20:
        df_geral_br.to_csv('datasets/gerais/acidentes_geral_por_br_20.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_br_20.csv...')
    elif qtd_brs == 30:
        df_geral_br.to_csv('datasets/gerais/acidentes_geral_por_br_30.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_br_30.csv...')
    elif qtd_brs == 40:
        df_geral_br.to_csv('datasets/gerais/acidentes_geral_por_br_40.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_br_40.csv...')
    elif qtd_brs == 50:
        df_geral_br.to_csv('datasets/gerais/acidentes_geral_por_br_50.csv', index=False)
        print('\n\nSalvando arquivo acidentes_geral_por_br_50.csv...')
    
    return df_geral_br   
# =======================================================
def processa_acidentes_geral_causa():
    
    contagem_por_causa_2007 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2007)
    contagem_por_causa_2008 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2008)
    contagem_por_causa_2009 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2009)
    contagem_por_causa_2010 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2010)
    contagem_por_causa_2011 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2011)
    contagem_por_causa_2012 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2012)
    contagem_por_causa_2013 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2013)
    contagem_por_causa_2014 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2014)
    contagem_por_causa_2015 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2015)
    contagem_por_causa_2016 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2016)
    contagem_por_causa_2017 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2017)
    contagem_por_causa_2018 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2018)
    contagem_por_causa_2019 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2019)
    contagem_por_causa_2020 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2020)
    contagem_por_causa_2021 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2021)
    contagem_por_causa_2022 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2022)
    contagem_por_causa_2023 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2023)
    contagem_por_causa_2024 = agrupamento_acidentes_por_ano_por_causa(df_pessoa_acidentes_2024)
    
    contagem_por_causa_2007['ano'] = '2007'
    contagem_por_causa_2008['ano'] = '2008'
    contagem_por_causa_2009['ano'] = '2009'
    contagem_por_causa_2010['ano'] = '2010'
    contagem_por_causa_2011['ano'] = '2011'
    contagem_por_causa_2012['ano'] = '2012'
    contagem_por_causa_2013['ano'] = '2013'
    contagem_por_causa_2014['ano'] = '2014'
    contagem_por_causa_2015['ano'] = '2015'
    contagem_por_causa_2016['ano'] = '2016'
    contagem_por_causa_2017['ano'] = '2017'
    contagem_por_causa_2018['ano'] = '2018'
    contagem_por_causa_2019['ano'] = '2019'
    contagem_por_causa_2020['ano'] = '2020'
    contagem_por_causa_2021['ano'] = '2021'
    contagem_por_causa_2022['ano'] = '2022'
    contagem_por_causa_2023['ano'] = '2023'
    contagem_por_causa_2024['ano'] = '2024'

    acidentes_por_causa_concatenados = pd.concat(
    [
      contagem_por_causa_2007, contagem_por_causa_2008, contagem_por_causa_2009,
      contagem_por_causa_2010, contagem_por_causa_2011, contagem_por_causa_2012,
      contagem_por_causa_2013, contagem_por_causa_2014, contagem_por_causa_2015,
      contagem_por_causa_2016, contagem_por_causa_2017, contagem_por_causa_2018,
      contagem_por_causa_2019, contagem_por_causa_2020, contagem_por_causa_2021,
      contagem_por_causa_2022, contagem_por_causa_2023, contagem_por_causa_2024
    
    ], axis=0)
    
    lista_causas = []
    
    for item in acidentes_por_causa_concatenados['causa_acidente'].unique():
      lista_causas.append(item)
    lista_causas.remove('(null)')
    
    lista_causas = lista_causas[:25]
    
    df_causa = acidentes_por_causa_concatenados
    df_geral_causa = pd.DataFrame(columns=['causa_acidente','qtd','ano'])
    
    for item in lista_causas:
      df_filtrado_causa = df_causa[(df_causa['causa_acidente'] == item)]
      df_geral_causa = pd.concat([df_geral_causa, df_filtrado_causa], ignore_index=True)
        
    df_geral_causa.to_csv('datasets/gerais/acidentes_geral_por_causa.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_causa.csv...')

    return df_geral_causa
# =======================================================
def processa_acidentes_geral_classificacao():
    
    contagem_por_classificacao_2007 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2007)
    contagem_por_classificacao_2008 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2008)
    contagem_por_classificacao_2009 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2009)
    contagem_por_classificacao_2010 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2010)
    contagem_por_classificacao_2011 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2011)
    contagem_por_classificacao_2012 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2012)
    contagem_por_classificacao_2013 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2013)
    contagem_por_classificacao_2014 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2014)
    contagem_por_classificacao_2015 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2015)
    contagem_por_classificacao_2016 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2016)
    contagem_por_classificacao_2017 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2017)
    contagem_por_classificacao_2018 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2018)
    contagem_por_classificacao_2019 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2019)
    contagem_por_classificacao_2020 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2020)
    contagem_por_classificacao_2021 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2021)
    contagem_por_classificacao_2022 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2022)
    contagem_por_classificacao_2023 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2023)
    contagem_por_classificacao_2024 = agrupamento_acidentes_por_ano_por_classificacao(df_pessoa_acidentes_2024)
    
    contagem_por_classificacao_2007['ano'] = '2007'
    contagem_por_classificacao_2008['ano'] = '2008'
    contagem_por_classificacao_2009['ano'] = '2009'
    contagem_por_classificacao_2010['ano'] = '2010'
    contagem_por_classificacao_2011['ano'] = '2011'
    contagem_por_classificacao_2012['ano'] = '2012'
    contagem_por_classificacao_2013['ano'] = '2013'
    contagem_por_classificacao_2014['ano'] = '2014'
    contagem_por_classificacao_2015['ano'] = '2015'
    contagem_por_classificacao_2016['ano'] = '2016'
    contagem_por_classificacao_2017['ano'] = '2017'
    contagem_por_classificacao_2018['ano'] = '2018'
    contagem_por_classificacao_2019['ano'] = '2019'
    contagem_por_classificacao_2020['ano'] = '2020'
    contagem_por_classificacao_2021['ano'] = '2021'
    contagem_por_classificacao_2022['ano'] = '2022'
    contagem_por_classificacao_2023['ano'] = '2023'
    contagem_por_classificacao_2024['ano'] = '2024'

    acidentes_por_classificacao_concatenados = pd.concat(
    [
      contagem_por_classificacao_2007, contagem_por_classificacao_2008, contagem_por_classificacao_2009,
      contagem_por_classificacao_2010, contagem_por_classificacao_2011, contagem_por_classificacao_2012,
      contagem_por_classificacao_2013, contagem_por_classificacao_2014, contagem_por_classificacao_2015,
      contagem_por_classificacao_2016, contagem_por_classificacao_2017, contagem_por_classificacao_2018,
      contagem_por_classificacao_2019, contagem_por_classificacao_2020, contagem_por_classificacao_2021,
      contagem_por_classificacao_2022, contagem_por_classificacao_2023, contagem_por_classificacao_2024
    
    ], axis=0)
    
    lista_classificacoes_antes = acidentes_por_classificacao_concatenados['classificacao_acidente'].unique()
    print(f'lista_classificacoes_antes => {lista_classificacoes_antes}')
    #acidentes_por_classificacao_concatenados.to_csv('datasets/gerais/acidentes_geral_por_classificacao_concatenados.csv', index=False)

    lista_classificacoes_depois = [item.rstrip() for item in lista_classificacoes_antes]
    lista_classificacoes_depois.remove('(null)')
    
    print(f'lista_classificacoes_depois => {lista_classificacoes_depois}')
    
    lista_sem_duplicacacoes = list(set(lista_classificacoes_depois))
    print(f'lista_sem_duplicacacoes => {lista_sem_duplicacacoes}')
    
    lista_classificacoes = lista_sem_duplicacacoes
    
    print(f'lista_classificacoes => {lista_classificacoes} ')
    
    df_classificacao = acidentes_por_classificacao_concatenados
    df_geral_classificacao = pd.DataFrame(columns=['classificacao_acidente','qtd','ano'])
    
    for item in lista_classificacoes:
      df_filtrado_classificacao = df_classificacao[(df_classificacao['classificacao_acidente'] == item)]
      df_geral_classificacao = pd.concat([df_geral_classificacao, df_filtrado_classificacao], ignore_index=True)
    
    df_geral_classificacao.to_csv('datasets/gerais/acidentes_geral_por_classificacao.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_classificacao.csv...')
    
    return df_geral_classificacao   
# =======================================================
def processa_acidentes_geral_fase_dia():
    
    contagem_por_fase_dia_2007 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2007)
    contagem_por_fase_dia_2008 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2008)
    contagem_por_fase_dia_2009 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2009)
    contagem_por_fase_dia_2010 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2010)
    contagem_por_fase_dia_2011 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2011)
    contagem_por_fase_dia_2012 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2012)
    contagem_por_fase_dia_2013 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2013)
    contagem_por_fase_dia_2014 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2014)
    contagem_por_fase_dia_2015 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2015)
    contagem_por_fase_dia_2016 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2016)
    contagem_por_fase_dia_2017 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2017)
    contagem_por_fase_dia_2018 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2018)
    contagem_por_fase_dia_2019 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2019)
    contagem_por_fase_dia_2020 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2020)
    contagem_por_fase_dia_2021 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2021)
    contagem_por_fase_dia_2022 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2022)
    contagem_por_fase_dia_2023 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2023)
    contagem_por_fase_dia_2024 = agrupamento_acidentes_por_ano_por_fase_dia(df_pessoa_acidentes_2024)
    
    contagem_por_fase_dia_2007['ano'] = '2007'
    contagem_por_fase_dia_2008['ano'] = '2008'
    contagem_por_fase_dia_2009['ano'] = '2009'
    contagem_por_fase_dia_2010['ano'] = '2010'
    contagem_por_fase_dia_2011['ano'] = '2011'
    contagem_por_fase_dia_2012['ano'] = '2012'
    contagem_por_fase_dia_2013['ano'] = '2013'
    contagem_por_fase_dia_2014['ano'] = '2014'
    contagem_por_fase_dia_2015['ano'] = '2015'
    contagem_por_fase_dia_2016['ano'] = '2016'
    contagem_por_fase_dia_2017['ano'] = '2017'
    contagem_por_fase_dia_2018['ano'] = '2018'
    contagem_por_fase_dia_2019['ano'] = '2019'
    contagem_por_fase_dia_2020['ano'] = '2020'
    contagem_por_fase_dia_2021['ano'] = '2021'
    contagem_por_fase_dia_2022['ano'] = '2022'
    contagem_por_fase_dia_2023['ano'] = '2023'
    contagem_por_fase_dia_2024['ano'] = '2024'

    acidentes_por_fase_dia_concatenados = pd.concat(
    [
      contagem_por_fase_dia_2007, contagem_por_fase_dia_2008, contagem_por_fase_dia_2009,
      contagem_por_fase_dia_2010, contagem_por_fase_dia_2011, contagem_por_fase_dia_2012,
      contagem_por_fase_dia_2013, contagem_por_fase_dia_2014, contagem_por_fase_dia_2015,
      contagem_por_fase_dia_2016, contagem_por_fase_dia_2017, contagem_por_fase_dia_2018,
      contagem_por_fase_dia_2019, contagem_por_fase_dia_2020, contagem_por_fase_dia_2021,
      contagem_por_fase_dia_2022, contagem_por_fase_dia_2023, contagem_por_fase_dia_2024
    
    ], axis=0)
    
    lista_fases = []
    
    for item in acidentes_por_fase_dia_concatenados['fase_dia'].unique():
      lista_fases.append(item)
    lista_fases.remove('(null)')
        
    df_fase = acidentes_por_fase_dia_concatenados
    df_geral_fase_dia = pd.DataFrame(columns=['fase_dia','qtd','ano'])
    
    for item in lista_fases:
      df_filtrado_fase = df_fase[(df_fase['fase_dia'] == item)]
      df_geral_fase_dia = pd.concat([df_geral_fase_dia, df_filtrado_fase], ignore_index=True)
        
    df_geral_fase_dia.to_csv('datasets/gerais/acidentes_geral_por_fase_dia.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_fase_dia.csv...')

    return df_geral_fase_dia  
# =======================================================
def processa_acidentes_geral_condicao_metereologica():

    contagem_por_condicao_metereologica_2007 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2007)
    contagem_por_condicao_metereologica_2008 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2008)
    contagem_por_condicao_metereologica_2009 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2009)
    contagem_por_condicao_metereologica_2010 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2010)
    contagem_por_condicao_metereologica_2011 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2011)
    contagem_por_condicao_metereologica_2012 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2012)
    contagem_por_condicao_metereologica_2013 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2013)
    contagem_por_condicao_metereologica_2014 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2014)
    contagem_por_condicao_metereologica_2015 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2015)
    contagem_por_condicao_metereologica_2016 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2016)
    contagem_por_condicao_metereologica_2017 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2017)
    contagem_por_condicao_metereologica_2018 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2018)
    contagem_por_condicao_metereologica_2019 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2019)
    contagem_por_condicao_metereologica_2020 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2020)
    contagem_por_condicao_metereologica_2021 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2021)
    contagem_por_condicao_metereologica_2022 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2022)
    contagem_por_condicao_metereologica_2023 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2023)
    contagem_por_condicao_metereologica_2024 = agrupamento_acidentes_por_ano_por_condicao_metereologica(df_pessoa_acidentes_2024)
    
    contagem_por_condicao_metereologica_2007['ano'] = '2007'
    contagem_por_condicao_metereologica_2008['ano'] = '2008'
    contagem_por_condicao_metereologica_2009['ano'] = '2009'
    contagem_por_condicao_metereologica_2010['ano'] = '2010'
    contagem_por_condicao_metereologica_2011['ano'] = '2011'
    contagem_por_condicao_metereologica_2012['ano'] = '2012'
    contagem_por_condicao_metereologica_2013['ano'] = '2013'
    contagem_por_condicao_metereologica_2014['ano'] = '2014'
    contagem_por_condicao_metereologica_2015['ano'] = '2015'
    contagem_por_condicao_metereologica_2016['ano'] = '2016'
    contagem_por_condicao_metereologica_2017['ano'] = '2017'
    contagem_por_condicao_metereologica_2018['ano'] = '2018'
    contagem_por_condicao_metereologica_2019['ano'] = '2019'
    contagem_por_condicao_metereologica_2020['ano'] = '2020'
    contagem_por_condicao_metereologica_2021['ano'] = '2021'
    contagem_por_condicao_metereologica_2022['ano'] = '2022'
    contagem_por_condicao_metereologica_2023['ano'] = '2023'
    contagem_por_condicao_metereologica_2024['ano'] = '2024'

    acidentes_por_condicao_metereologica_concatenados = pd.concat(
    [
      contagem_por_condicao_metereologica_2007, contagem_por_condicao_metereologica_2008, contagem_por_condicao_metereologica_2009,
      contagem_por_condicao_metereologica_2010, contagem_por_condicao_metereologica_2011, contagem_por_condicao_metereologica_2012,
      contagem_por_condicao_metereologica_2013, contagem_por_condicao_metereologica_2014, contagem_por_condicao_metereologica_2015,
      contagem_por_condicao_metereologica_2016, contagem_por_condicao_metereologica_2017, contagem_por_condicao_metereologica_2018,
      contagem_por_condicao_metereologica_2019, contagem_por_condicao_metereologica_2020, contagem_por_condicao_metereologica_2021,
      contagem_por_condicao_metereologica_2022, contagem_por_condicao_metereologica_2023, contagem_por_condicao_metereologica_2024
    
    ], axis=0)
    
    lista_condicoes = []
    
    for item in acidentes_por_condicao_metereologica_concatenados['condicao_metereologica'].unique():
      lista_condicoes.append(item)
    lista_condicoes.remove('(null)')

    df_condicao = acidentes_por_condicao_metereologica_concatenados
    df_geral_condicao_metereologica = pd.DataFrame(columns=['condicao_metereologica','qtd','ano'])
    
    for item in lista_condicoes:
      df_filtrado_classificacao = df_condicao[(df_condicao['condicao_metereologica'] == item)]
      df_geral_condicao_metereologica = pd.concat([df_geral_condicao_metereologica, df_filtrado_classificacao], ignore_index=True)
        
    df_geral_condicao_metereologica.to_csv('datasets/gerais/acidentes_geral_por_condicao_metereologica.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_condicao_metereologica.csv...')

    return df_geral_condicao_metereologica   
# =======================================================   
def processa_acidentes_geral_dia_semana():
    
    contagem_por_dia_semana_2007 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2007)
    contagem_por_dia_semana_2008 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2008)
    contagem_por_dia_semana_2009 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2009)
    contagem_por_dia_semana_2010 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2010)
    contagem_por_dia_semana_2011 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2011)
    contagem_por_dia_semana_2012 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2012)
    contagem_por_dia_semana_2013 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2013)
    contagem_por_dia_semana_2014 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2014)
    contagem_por_dia_semana_2015 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2015)
    contagem_por_dia_semana_2016 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2016)
    contagem_por_dia_semana_2017 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2017)
    contagem_por_dia_semana_2018 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2018)
    contagem_por_dia_semana_2019 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2019)
    contagem_por_dia_semana_2020 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2020)
    contagem_por_dia_semana_2021 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2021)
    contagem_por_dia_semana_2022 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2022)
    contagem_por_dia_semana_2023 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2023)
    contagem_por_dia_semana_2024 = agrupamento_acidentes_por_ano_por_dia_semana(df_pessoa_acidentes_2024)
    
    contagem_por_dia_semana_2007['ano'] = '2007'
    contagem_por_dia_semana_2008['ano'] = '2008'
    contagem_por_dia_semana_2009['ano'] = '2009'
    contagem_por_dia_semana_2010['ano'] = '2010'
    contagem_por_dia_semana_2011['ano'] = '2011'
    contagem_por_dia_semana_2012['ano'] = '2012'
    contagem_por_dia_semana_2013['ano'] = '2013'
    contagem_por_dia_semana_2014['ano'] = '2014'
    contagem_por_dia_semana_2015['ano'] = '2015'
    contagem_por_dia_semana_2016['ano'] = '2016'
    contagem_por_dia_semana_2017['ano'] = '2017'
    contagem_por_dia_semana_2018['ano'] = '2018'
    contagem_por_dia_semana_2019['ano'] = '2019'
    contagem_por_dia_semana_2020['ano'] = '2020'
    contagem_por_dia_semana_2021['ano'] = '2021'
    contagem_por_dia_semana_2022['ano'] = '2022'
    contagem_por_dia_semana_2023['ano'] = '2023'
    contagem_por_dia_semana_2024['ano'] = '2024'

    acidentes_por_dia_semana_concatenados = pd.concat(
    [
      contagem_por_dia_semana_2007, contagem_por_dia_semana_2008, contagem_por_dia_semana_2009,
      contagem_por_dia_semana_2010, contagem_por_dia_semana_2011, contagem_por_dia_semana_2012,
      contagem_por_dia_semana_2013, contagem_por_dia_semana_2014, contagem_por_dia_semana_2015,
      contagem_por_dia_semana_2016, contagem_por_dia_semana_2017, contagem_por_dia_semana_2018,
      contagem_por_dia_semana_2019, contagem_por_dia_semana_2020, contagem_por_dia_semana_2021,
      contagem_por_dia_semana_2022, contagem_por_dia_semana_2023, contagem_por_dia_semana_2024
    
    ], axis=0)
    
    lista_dias_semanas = ['dom','seg','ter','qua','qui','sex','sáb']
    
    print(f'\n\n lista_dias_semanas ({len(lista_dias_semanas)}) => {lista_dias_semanas}...')
    
    df_dias_semana = acidentes_por_dia_semana_concatenados
    df_dias_semana['dia_semana'] = df_dias_semana['dia_semana'].str.lower()
    print(f'\n df_geral_dias_semanas => {df_dias_semana}')

    df_geral_dias_semanas = pd.DataFrame(columns=['dia_semana','qtd','ano'])

    for item in lista_dias_semanas:
      df_filtrado_dias_semana = df_dias_semana[(df_dias_semana['dia_semana'].str.find(item.lower()) != -1)]
      df_geral_dias_semanas = pd.concat([df_geral_dias_semanas, df_filtrado_dias_semana], ignore_index=True)
    
    df_geral_dias_semanas.to_csv('datasets/gerais/acidentes_geral_por_dia_semana.csv', index=False)
    print('\n\nSalvando arquivo acidentes_geral_por_dia_semana...')

    return df_geral_dias_semanas
# =======================================================   
def processa_dados_mapa_calor_ano(df):
   
    lista_classificacao = ['Com Vítimas Feridas', 'Com Vítimas Fatais', 'Sem Vítimas']  
    
    df_geral_classificacao = pd.DataFrame(columns=['classificacao','pessoas','mortos','feridos_leves','feridos_graves','ilesos','ignorados','feridos','veiculos'])

    correlacao_classificacao_pessoas = df.groupby('classificacao_acidente')['pessoas'].agg(['count', 'sum'])
    print('pessoas', correlacao_classificacao_pessoas)
    
    correlacao_classificacao_mortos = df.groupby('classificacao_acidente')['mortos'].agg(['count', 'sum'])
    print('mortos',correlacao_classificacao_mortos)
    
    correlacao_classificacao_feridos_leves = df.groupby('classificacao_acidente')['feridos_leves'].agg(['count', 'sum'])
    print('feridos_leves',correlacao_classificacao_feridos_leves)
    
    correlacao_classificacao_feridos_graves = df.groupby('classificacao_acidente')['feridos_graves'].agg(['count', 'sum'])
    print('feridos_graves',correlacao_classificacao_feridos_graves)
    
    correlacao_classificacao_ilesos = df.groupby('classificacao_acidente')['ilesos'].agg(['count', 'sum'])
    print('ilesos', correlacao_classificacao_ilesos)
    
    correlacao_classificacao_ignorados = df.groupby('classificacao_acidente')['ignorados'].agg(['count', 'sum'])
    print('ignorados',correlacao_classificacao_ignorados)
    
    correlacao_classificacao_feridos = df.groupby('classificacao_acidente')['feridos'].agg(['count', 'sum'])
    print('feridos',correlacao_classificacao_feridos)
    
    correlacao_classificacao_veiculos = df.groupby('classificacao_acidente')['veiculos'].agg(['count', 'sum'])
    print('veiculos',correlacao_classificacao_veiculos)

    for (indice,item) in enumerate(lista_classificacao):
        
        # Linha para Classificação
        novo_registro = pd.DataFrame(
            {
             'classificacao': item, 
             'pessoas': [correlacao_classificacao_pessoas.iloc[indice]['sum']], 
             'mortos': [correlacao_classificacao_mortos.iloc[indice]['sum']], 
             'feridos_leves': [correlacao_classificacao_feridos_leves.iloc[indice]['sum']], 
             'feridos_graves': [correlacao_classificacao_feridos_graves.iloc[indice]['sum']], 
             'ilesos': [correlacao_classificacao_ilesos.iloc[indice]['sum']], 
             'ignorados': [correlacao_classificacao_ignorados.iloc[indice]['sum']], 
             'feridos': [correlacao_classificacao_feridos.iloc[indice]['sum']], 
             'veiculos': [correlacao_classificacao_veiculos.iloc[indice]['sum']],      
            }
        )

        df_geral_classificacao = pd.concat([df_geral_classificacao, novo_registro], ignore_index=True)   
    
    return df_geral_classificacao
# =========================================
def salva_mapa_calor_ano(ano, df):    
    nome_arquivo = f'mapa_calor/mapa_calor_classificacao_{str(ano)}.csv'
    df.to_csv(nome_arquivo, index=False)
    print(f'\n\nSalvando arquivo {nome_arquivo}...')
# =========================================        
