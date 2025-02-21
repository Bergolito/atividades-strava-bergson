# =======================================================
# Imports
# =======================================================

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
#import matplotlib.pyplot as plt

# =======================================================
# Datasets
# =======================================================
df_acidentes_uf_geral = pd.read_csv('acidentes_por_uf_geral.csv', sep=',', encoding="ISO-8859-1")
df_acidentes_tipo_geral = pd.read_csv('acidentes_por_tipo_geral.csv', sep=',', encoding="UTF-8")
df_acidentes_br_geral = pd.read_csv('acidentes_por_br_geral.csv', sep=',', encoding="ISO-8859-1")
df_acidentes_causa_geral = pd.read_csv('acidentes_por_causa_geral.csv', sep=',', encoding="UTF-8")

# =======================================================
# Rankings
# =======================================================

df_ranking_uf = pd.read_csv('ranking_acidentes_uf.csv', sep=',', encoding="UTF-8")
df_ranking_tipo = pd.read_csv('ranking_acidentes_tipo.csv', sep=',', encoding="UTF-8")
df_ranking_br = pd.read_csv('ranking_acidentes_br.csv', sep=',', encoding="UTF-8")

# =======================================================
# Pré-Processamento dos dataframes
# =======================================================

# Removendo as linhas que tem o valor '(null)' na coluna 'UF'
#print(f'Antes = {df_acidentes_uf_geral.shape[0]}')
#df_acidentes_uf_geral = df_acidentes_uf_geral.loc[df_acidentes_uf_geral['UF'] != '(null)']
#print(f'Depois = {df_acidentes_uf_geral.shape[0]}')
#df_acidentes_uf_geral.to_csv('acidentes_por_uf_geral2.csv')




# =======================================================
# Funções
# =======================================================
def agrupamento_acidentes_por_ano_por_uf(df):
  contagem_por_uf = df['uf'].value_counts().reset_index()
  contagem_por_uf.columns = ['UF', 'Qtd']
  return contagem_por_uf
# =======================================================
def agrupamento_acidentes_por_ano_por_br(df):
  contagem_por_br = df['br'].value_counts().reset_index()
  contagem_por_br.columns = ['br', 'qtd']
  return contagem_por_br
# =======================================================
def gera_grafico_por_uf(ano, contagem_por_uf_ano):

  lista_cores = alt.Scale(domain= contagem_por_uf_ano['UF'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_uf = alt.Chart(contagem_por_uf_ano).mark_bar().encode(
      y=alt.Y('UF:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('Qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['UF', 'Qtd'],
      color=alt.Color('UF:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por UF em {ano}'
  ).interactive()

  return chart_uf
# =======================================================
def contagem_por_tipo_acidente(df_ocorrencia_acidentes):
  contagem_por_tipo = df_ocorrencia_acidentes['tipo_acidente'].value_counts().reset_index(name='qtd').rename(columns={'index': 'UF'})
  contagem_por_tipo.columns = ['tipo_acidente', 'qtd']

  return contagem_por_tipo
# =======================================================
def gera_grafico_por_tipo(ano, contagem_por_tipo_ano):

  lista_cores = alt.Scale(domain=contagem_por_tipo_ano['tipo_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_tipo = alt.Chart(contagem_por_tipo_ano).mark_bar().encode(
      y=alt.Y('tipo_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['tipo_acidente', 'qtd'],
      color=alt.Color('tipo_acidente:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por Tipo no Ano de {ano}',
      width=1024  # Defina a largura em pixels
  ).interactive()

  return chart_tipo
# =======================================================
def gera_grafico_por_br(ano, contagem_por_br_ano):

  lista_cores = alt.Scale(domain=contagem_por_br_ano['br'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_br = alt.Chart(contagem_por_br_ano).mark_bar().encode(
      y=alt.Y('br:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['br', 'qtd'],
      color=alt.Color('br:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por BR no Ano de {ano}'
  ).interactive()

  return chart_br
# =======================================================
def gera_grafico_por_causa(ano, contagem_por_causa_ano):

  lista_cores = alt.Scale(domain=contagem_por_causa_ano['causa_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_causa_ano).mark_bar().encode(
      y=alt.Y('causa_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['causa_acidente', 'qtd'],
      color=alt.Color('causa_acidente:N', scale=lista_cores)

  ).properties(
      title=f'Acidentes por Causa no Ano de {ano}',
      width=1024  # Defina a largura em pixels
  ).interactive()


  return chart
# =======================================================

contagem_br_geral = agrupamento_acidentes_por_ano_por_br(df_acidentes_br_geral)
contagem_br_geral.head()


