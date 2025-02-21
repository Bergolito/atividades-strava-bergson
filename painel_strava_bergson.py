# =======================================================
# Imports
# =======================================================
import pandas as pd
import streamlit as st

from painel_strava_funcoes import *
from painel_strava_graficos import *

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


df_atvs_tipo_todos = pd.read_csv('datasets/gerais/atividades_geral_por_tipo.csv', sep=',', encoding="UTF-8")

# =======================================================
# Constantes do dashboard
# =======================================================
#OPCAO_TODOS = 'Todos'
OPCAO_NONE = None
COLUNA_ANO = 'ano'

OPCAO_FILTRO_POR_UM_ANO = "Filtro por Um Ano"
OPCAO_FILTRO_POR_PERIODO = "Filtro por Período"
opcoes = [OPCAO_FILTRO_POR_UM_ANO, OPCAO_FILTRO_POR_PERIODO]

ano_inicio = None
ano_fim = None

st.set_page_config(
    page_title="Atividades Físicas Strava",
    page_icon="🧊",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded",  # or "collapsed"
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# This is a header',
    }
)

# Definir o título fixo para o painel
st.title("Atividades Físicas Bergson (Strava)")

exibir_filtro_periodo_anos = False

with st.sidebar:
    st.header("Filtros:")
    
    opcao_selecionada = st.radio(
        "Selecione uma opção:",
        opcoes,
        index=0,
        disabled=False # Inicialmente habilitado
    )
    indice_selecionado = opcoes.index(opcao_selecionada)
    print(f'indice_selecionado => {indice_selecionado}')

    st.session_state.opcao_selecionada = opcao_selecionada

    if st.session_state.opcao_selecionada == OPCAO_FILTRO_POR_UM_ANO:

        ano_selecionado = st.sidebar.selectbox(
            'Qual o ano deseja visualizar?',
            ('2025','2024', '2023', '2022', '2021', '2020'), index=1,
            key="ano_selecionado"
        )

        print(f'Ano Selecionado = {ano_selecionado}')

        exibir_filtro_periodo_anos = False

    else:
        exibir_filtro_periodo_anos = True
        st.sidebar.title("Filtro por Período de Anos:")
        ano_selecionado = None

        col1, col2 = st.sidebar.columns(2)  # Divide a linha em duas colunas para melhor layout

        with col1:
            ano_inicio = st.sidebar.number_input("Ano de Início", key=ano_inicio, min_value=2020, max_value=2025, step=1, value=2020)
        with col2:
            ano_fim = st.sidebar.number_input("Ano de Fim", key=ano_fim, min_value=2020, max_value=2025, step=1, value=2024)

        # Validação básica para garantir que o ano de início não seja posterior ao ano de fim
        if ano_inicio > ano_fim:
            st.sidebar.error("Erro: O ano de início não pode ser posterior ao ano de fim.")
            ano_inicio = None  # Reseta os valores para evitar processamento incorreto
            ano_fim = None


st.sidebar.write(f"Opção selecionada: {st.session_state.opcao_selecionada}")

if 'ano_selecionado' not in st.session_state:
    st.session_state.ano_selecionado = None

# Definição de abas
tab_01, tab_02, tab_03, tab_04, tab_05 = st.tabs(
  [
    "Atividades Físicas por Critérios",
    "Atividades Físicas 02",
    "Atividades Físicas por Ranking",
    "Atividades Físicas por Barras Empilhadas",
    "Atividades Físicas por Fluxo",
  ]
)

# filtro
df_selecionado = df_atividades_simplificado_2024
ano_selecionado1 = 2024
if st.session_state.ano_selecionado is None:
    df_selecionado = df_atividades_simplificado_2024
else:

    if st.session_state.ano_selecionado == '2020':
        ano_selecionado1 = 2020
        df_selecionado = df_atividades_simplificado_2020

    elif st.session_state.ano_selecionado == '2021':
        ano_selecionado1 = 2021
        df_selecionado = df_atividades_simplificado_2021    

    elif st.session_state.ano_selecionado == '2022':
        ano_selecionado1 = 2022
        df_selecionado = df_atividades_simplificado_2022    

    elif st.session_state.ano_selecionado == '2023':
        ano_selecionado1 = 2023
        df_selecionado = df_atividades_simplificado_2023    

    elif st.session_state.ano_selecionado == '2024':
        ano_selecionado1 = 2024
        df_selecionado = df_atividades_simplificado_2024    

    elif st.session_state.ano_selecionado == '2025':
        ano_selecionado1 = 2025
        df_selecionado = df_atividades_simplificado_2025    

# ==============================================================================
with tab_01:

    # =======================================================
    # aba 
    # =======================================================
    titulo = f'<h3> Atividades por Tipo'
    st.markdown(titulo, unsafe_allow_html=True)  

    #lista_dfs = retorna_atividades_df_por_mes(df_selecionado)

    titulo = f'Atividades Físicas em {ano_selecionado1}'
    df_filtro = df_atvs_tipo_todos[(df_atvs_tipo_todos['ano'] == ano_selecionado1)]
    st.table(df_filtro)

    grafico_pizza = grafico_pizza_tipo_atv(df_filtro)
    st.altair_chart(grafico_pizza, use_container_width=False)

    grafico_ano = gera_grafico_barras_tipo_exercicio(df_filtro, titulo)
    st.altair_chart(grafico_ano, use_container_width=False)

# ==============================================================================
with tab_02:

    # =======================================================
    # aba tab_bbb_01
    # =======================================================
    titulo = f'<h3> Atividades Físicas'
    st.markdown(titulo, unsafe_allow_html=True)  

    # filtro
    df_selecionado = df_atividades_simplificado_2024
    ano_selecionado1 = 2024
    if st.session_state.ano_selecionado is None:
        df_selecionado = df_atividades_simplificado_2024
    else:

        if st.session_state.ano_selecionado == '2020':
            ano_selecionado1 = 2020
            df_selecionado = df_atividades_simplificado_2020

        elif st.session_state.ano_selecionado == '2021':
            ano_selecionado1 = 2021
            df_selecionado = df_atividades_simplificado_2021    

        elif st.session_state.ano_selecionado == '2022':
            ano_selecionado1 = 2022
            df_selecionado = df_atividades_simplificado_2022    

        elif st.session_state.ano_selecionado == '2023':
            ano_selecionado1 = 2023
            df_selecionado = df_atividades_simplificado_2023    

        elif st.session_state.ano_selecionado == '2024':
            ano_selecionado1 = 2024
            df_selecionado = df_atividades_simplificado_2024    

        elif st.session_state.ano_selecionado == '2025':
            ano_selecionado1 = 2025
            df_selecionado = df_atividades_simplificado_2025    

        for mes in range(0, 12):
            print(f'ano => {ano_selecionado1} | mes => {mes}')
            nome_mes = obter_mes_por_numero(mes)
            titulo = f'Atividades Físicas em {nome_mes} de {ano_selecionado1}'
            df_filtro = agrupamento_atividade_por_tipo_por_ano_mes(df_selecionado, ano_selecionado1, mes)
            st.write(titulo) 
            st.table(df_filtro)
            grafico_ano_mes = gera_grafico_barras_tipo_exercicio(df_filtro, titulo)
            st.altair_chart(grafico_ano_mes, use_container_width=False)

# ==============================================================================
with tab_03:

    # =======================================================
    # aba 
    # =======================================================
    titulo = f'<h3> Atividades por Ranking'
    st.markdown(titulo, unsafe_allow_html=True)  

    titulo =f'Gráfico de Ranking de Atividades em {ano_selecionado1}'
    grafico_ranking = gera_grafico_ranking_tipo_01(df_atvs_tipo_todos, titulo)    
    st.altair_chart(grafico_ranking, use_container_width=False)

# ==============================================================================
with tab_04:

    # =======================================================
    # aba 
    # =======================================================
    titulo = f'<h3> Atividades por Barras Empilhadas'
    st.markdown(titulo, unsafe_allow_html=True)  

    titulo =f'Gráfico de Barras Empilhadas de Atividades em {ano_selecionado1}'
    grafico_barras_emp = grafico_barras_empilhadas_por_tupo(titulo, df_atvs_tipo_todos)    
    st.altair_chart(grafico_barras_emp, use_container_width=False)

# ==============================================================================
with tab_05:

    # =======================================================
    # aba 
    # =======================================================
    titulo = f'<h3> Atividades por Fluxo de Dados'
    st.markdown(titulo, unsafe_allow_html=True)  

    titulo =f'Gráfico de Fluxo de Atividades em {ano_selecionado1}'
    grafico_fluxo = gera_graficos_fluxo_por_tipo(titulo, df_atvs_tipo_todos)    
    st.altair_chart(grafico_fluxo, use_container_width=False)
