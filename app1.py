import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly.graph_objects as go

from painel_strava_funcoes import *
from painel_strava_graficos import *

st.set_page_config(page_title="Dashboard", layout="wide")

# CSS para cor de fundo do sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #1c9ea0 !important;
    }
	[data-testid="stAppViewContainer"] {
        background-color: #dcdddf;
    }
	[data-testid="stVerticalBlock"] {
        background-color: #fff;
        border-radius: 8px;
        padding: 8px;
    }	
    </style>
    """,
    unsafe_allow_html=True
)

# =======================================================
# Datasets
# =======================================================
df_atividades_todos = pd.read_csv('datasets/predados/atividades_fisicas_todos.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2020 = pd.read_csv('datasets/predados/atividades_fisicas_2020.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2021 = pd.read_csv('datasets/predados/atividades_fisicas_2021.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2022 = pd.read_csv('datasets/predados/atividades_fisicas_2022.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2023 = pd.read_csv('datasets/predados/atividades_fisicas_2023.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2024 = pd.read_csv('datasets/predados/atividades_fisicas_2024.csv', sep=',', encoding="ISO-8859-1")
df_atividades_completo_2025 = pd.read_csv('datasets/predados/atividades_fisicas_2025.csv', sep=',', encoding="ISO-8859-1")

df_atividades_simplificado_todos = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_todos.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2020 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2020.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2021 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2021.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2022 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2022.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2023 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2023.csv', sep=',', encoding="ISO-8859-1")
df_atividades_simplificado_2024 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2024.csv', sep=',', encoding="UTF-8")
df_atividades_simplificado_2025 = pd.read_csv('datasets/predados/atividades_fisicas_simplificado_2025.csv', sep=',', encoding="ISO-8859-1")

df_sumario_2024 = pd.read_csv('datasets/gerais/sumario_atividades_2024.csv', sep=',', encoding="UTF-8")

df_atvs_tipo_todos = pd.read_csv('datasets/gerais/atividades_geral_por_tipo.csv', sep=',', encoding="UTF-8")
df_atvs_dia_semana_todos = pd.read_csv('datasets/gerais/atividades_geral_por_dia_semana.csv', sep=',', encoding="UTF-8")

df_sumario_atvs_2020 = pd.read_csv('datasets/gerais/sumario_atividades_2020.csv', sep=',', encoding="UTF-8")
df_sumario_atvs_2021 = pd.read_csv('datasets/gerais/sumario_atividades_2021.csv', sep=',', encoding="UTF-8")
df_sumario_atvs_2022 = pd.read_csv('datasets/gerais/sumario_atividades_2022.csv', sep=',', encoding="UTF-8")
df_sumario_atvs_2023 = pd.read_csv('datasets/gerais/sumario_atividades_2023.csv', sep=',', encoding="UTF-8")
df_sumario_atvs_2024 = pd.read_csv('datasets/gerais/sumario_atividades_2024.csv', sep=',', encoding="UTF-8")
df_sumario_atvs_2025 = pd.read_csv('datasets/gerais/sumario_atividades_2025.csv', sep=',', encoding="UTF-8")


# Carregar os anos do dataset
df_atividades = pd.read_csv('datasets/predados/atividades_fisicas_todos.csv', sep=',', encoding='utf-8')
anos = sorted(df_atividades['data_ano'].unique(), reverse=True)

if 'ano_selecionado' not in st.session_state:
    st.session_state.ano_selecionado = 2025

with st.sidebar:
    st.title("Painel de Atividades")
    st.write("Lista de Itens")
    ano_selecionado = st.selectbox("Selecione o ano da atividade:", anos, key="ano_selecionado")
    st.write("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
    st.image("images/logotipo.png", width=240)
    st.write("<br><br><br><br><br><br><br>", unsafe_allow_html=True)

df_selecionado = df_atividades_simplificado_2024

# ====== Topbar ======
with st.container():

    colA, colB, colC = st.columns([2,6,3])
    with colA:
        st.image("images/logotipo.png", width=120)
		
    with colB:
        st.text_input("Pesquisar", placeholder="Pesquisar...", label_visibility="collapsed")
    with colC:
        st.markdown("**📅 15 Mar 2024 • 15:00**")

    #st.write("ano selecionado:", ano_selecionado)
    #st.write("qtd:", df_selecionado.shape[0])
    st.markdown("---")

# ====== Linha 1 ======
with st.container():
	
	## Linha 1 - Gauges
	#- Gauge: Qtd Total de Atividades
	#- Gauge: Distância em Km das Atividades
	#- Gauge: Qtd de Calorias Gastas das Atividades
	#- Gauge: Tempo em min das Atividades
	col1, col2, col3, col4 = st.columns(4)
	with col1:
        st.metric("Qtd Total de Atividades", df_selecionado.shape[0], "")
	with col2:		
		st.metric("Distância em Km", round(df_selecionado["Distance"].sum(), 1), "")
	with col3:
		st.metric("Qtd de Calorias Gastas", round(df_selecionado["Calories"].sum(), 1), "")
	with col4:
		st.metric("Tempo em min", round(df_selecionado["tempo_min"].sum(), 1), "")
		
st.markdown("---")

# ====== Linha 2 ====== 
col4, col5, col20 = st.columns(2)

#- Pie/Donut - Atividades por Tipo
#- Barras: Atividades Físicas por Ano
with col4:
    # Gráfico de pizza para distribuição por tipo
    st.subheader("Distribuição de Atividades por Tipo")
    df_filtro = df_atvs_tipo_todos[(df_atvs_tipo_todos['ano'] == 2024)]
    grafico_pizza = grafico_pizza_tipo_atv(df_filtro)
    st.altair_chart(grafico_pizza, use_container_width=True)

# Vertical columns mock
with col5:
	st.subheader("Barras: Atividades Físicas por Ano")
	grafico_atividades_ano_mes = gera_grafico_barras_atividades_mes(df_sumario_atvs_2024, 'Atv em 2024')
	st.altair_chart(grafico_atividades_ano_mes, use_container_width=False)
with col20:
    import plotly.graph_objects as go

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 270,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Speed"}))

    #fig.show()
    st.plotly_chart(fig, use_container_width=True)

# ====== Linha 2 ======
col6, col7 = st.columns(2)

#- Ranking das atividades por Tipo
#- Ranking das atividades por Dia da Semana

# Horizontal bar mock
with col6:
    st.subheader("Ranking das Atividades Por Tipo")
    titulo =f'Ranking de Atividades por tipo (2020 a 2025)'
    grafico_ranking_01 = gera_grafico_ranking_tipo_01(df_atvs_tipo_todos, titulo)    
    st.altair_chart(grafico_ranking_01, use_container_width=False)

# Vertical columns mock
with col7:
    st.subheader("Ranking das Atividades Por Dia Da Semana")
    titulo =f'Ranking de Atividades por dia da semana (2020 a 2025)'
    grafico_ranking_02 = gera_grafico_ranking_dia_semana_01(df_atvs_dia_semana_todos, titulo)
    st.altair_chart(grafico_ranking_02, use_container_width=False)
