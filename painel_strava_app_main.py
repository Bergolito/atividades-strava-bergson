# =======================================================
# Imports
# =======================================================
import pandas as pd
import streamlit as st
import folium
import gpxpy
import plotly.express as px
import numpy as np

from streamlit_folium import st_folium
from painel_strava_funcoes import *
from painel_strava_graficos import *

st.set_page_config(
    page_title="Atividades Físicas Strava",
    page_icon="🏃",

    layout="wide",  # or "centered"
    initial_sidebar_state="expanded",  # or "collapsed"
    menu_items={
        'Get Help': 'https://www.streamlit.io/help',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# This is a header',
    }
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
df_sumario_atvs_todos = pd.concat(
    [
        df_sumario_atvs_2020, df_sumario_atvs_2021, df_sumario_atvs_2022, df_sumario_atvs_2023, df_sumario_atvs_2024, df_sumario_atvs_2025
    ], ignore_index=True) 

# adicionado
df_tipo_todos = pd.read_csv('datasets/gerais/atividades_geral_por_tipo_ano_mes.csv', sep=',', encoding="UTF-8")
df_dia_semana_todos = pd.read_csv('datasets/gerais/atividades_geral_por_dia_semana_ano_mes.csv', sep=',', encoding="UTF-8")

# =======================================================
# Constantes do dashboard
# =======================================================

# CSS para estilizar a tabela
css = """
    <style>
    [data-testid="stAppHeader"] {
        background-color: #1c9ea0 !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #1c9ea0 !important;
    }
    [data-testid="stVerticalBlock"] {
        background-color: #fff;
        border-radius: 8px;
        padding: 8px;
    } 
    </style>
"""

st.markdown(css, unsafe_allow_html=True)

OPCAO_TODOS = 'Todos'
OPCAO_NONE = None
COLUNA_ANO = 'ano'
PULA_LINHAS = '<br><br><br><br><br><br><br>'

lista_anos = sorted(df_atividades_simplificado_todos['data_ano'].unique(), reverse=True)    
ano_inicio = lista_anos[-1]
ano_fim = lista_anos[0]

opcoes_anos = [OPCAO_TODOS] + [str(ano) for ano in lista_anos]

# ===============================================================================
# Cabeçalho do dashboard
with st.container():

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/logotipo.png", width=180)
    with col2:
        # Definir o título fixo para o painel
        st.title("Painel de Atividades Físicas Bergson")
    with col3:
        ano_selecionado = st.selectbox(
            'Qual o ano deseja visualizar?',
            opcoes_anos, index=1,
            key="ano_selecionado"
        )

# ===============================================================================
if 'ano_selecionado' not in st.session_state:
    st.session_state.ano_selecionado = None

# Definição de abas
nova_aba, tab_detalhamento, tab_corrida = st.tabs(
  [ "Gráficos - Visão Geral", "Atvs - Detalhamento", "Corrida"]
)

# filtro
df_selecionado = df_atividades_simplificado_2024
ano_selecionado1 = 2025
if st.session_state.ano_selecionado is None:
    df_selecionado = df_atividades_simplificado_2024
else:

    if st.session_state.ano_selecionado == '2020':
        ano_selecionado1 = 2020
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == '2021':
        ano_selecionado1 = 2021
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == '2022':
        ano_selecionado1 = 2022
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == '2023':
        ano_selecionado1 = 2023
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == '2024':
        ano_selecionado1 = 2024
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == '2025':
        ano_selecionado1 = 2025
        df_selecionado = df_atividades_simplificado_todos[df_atividades_simplificado_todos['data_ano'] == ano_selecionado1]
    elif st.session_state.ano_selecionado == OPCAO_TODOS:
        ano_selecionado1 = OPCAO_TODOS
        df_selecionado = df_atividades_simplificado_todos


# ==============================================================================
with nova_aba:

    # ====== Linha 1 ======
    with st.container():

        ## Linha 1 - Gauges
        #- Gauge: Qtd Total de Atividades
        #- Gauge: Distância em Km das Atividades
        #- Gauge: Qtd de Calorias Gastas das Atividades
        #- Gauge: Tempo em min das Atividades
        col1, col2, col3, col4, col5, col51 = st.columns(6)
        with col1:
            st.metric("Qtd Total de Atividades", df_selecionado.shape[0], "")

        with col2:
            if ano_selecionado1 != 'Todos':
                st.metric("Média Mensal", round(df_selecionado.shape[0]/12,1), "")
            elif ano_selecionado1 == 'Todos':
                st.metric("Média Anual", round(df_selecionado.shape[0]/len(opcoes_anos),1), "")

        with col3:		
            st.metric("Distância em Km", round(df_selecionado["Distance"].sum(), 1), "")

        with col4:
            st.metric("Qtd de Calorias Gastas", round(df_selecionado["Calories"].sum(), 1), "")

        with col5:
            st.metric("Tempo em min", round(df_selecionado["tempo_min"].sum(), 1), "")

        with col51:
            st.metric("Tempo em horas", round(df_selecionado["tempo_min"].sum()/60, 1), "")
            
    st.markdown("---")

    # ====== Linha 2 ====== 
    col4, col5 = st.columns(2)

    if ano_selecionado1 != 'Todos':
        df_filtro_pizza = df_atvs_tipo_todos[(df_atvs_tipo_todos['ano'] == ano_selecionado1)]
        df_filtro_barras = df_sumario_atvs_todos[(df_sumario_atvs_todos['ano'] == ano_selecionado1)]
        titulo_barras = f'Atividades Físicas em {ano_selecionado1}'
    elif ano_selecionado1 == 'Todos':
        df_filtro_pizza = df_atvs_tipo_todos
        df_filtro_barras = df_sumario_atvs_todos
        titulo_barras = f'Atividades Físicas entre 2020 e 2025'

    with col4:
        # Gráfico de pizza para distribuição por tipo
        st.subheader("Distribuição de Atividades por Tipo")
        grafico_pizza = grafico_pizza_tipo_atv(df_filtro_pizza)
        #st.altair_chart(grafico_pizza, width="use_container")
        st.altair_chart(grafico_pizza, use_container_width=True)

    with col5:
        st.subheader("Barras: Atividades Físicas por Ano")
        grafico_atividades_ano_mes = gera_grafico_barras_atividades_mes(df_filtro_barras, titulo_barras)
        #st.altair_chart(grafico_atividades_ano_mes, width="use_container")
        st.altair_chart(grafico_atividades_ano_mes, use_container_width=True)

    # ====== Linha 3 ======
    col6, col7 = st.columns(2)

    #- Ranking das atividades por Tipo
    with col6:

        st.subheader("Ranking das Atividades Por Tipo")
        titulo =f'Ranking de Atividades em {ano_selecionado1} por tipo'

        if ano_selecionado1 != 'Todos':
            df_filtro_ranking_tipo = df_tipo_todos[(df_tipo_todos['ano'] == ano_selecionado1)]
            grafico_ranking_01 = gera_grafico_ranking_tipo_02_ano_mes(df_filtro_ranking_tipo, titulo)    
            
        elif ano_selecionado1 == 'Todos':
            titulo =f'Ranking de Atividades por tipo (2020 a 2025)'
            grafico_ranking_01 = gera_grafico_ranking_tipo_01(df_atvs_tipo_todos, titulo)    

        st.altair_chart(grafico_ranking_01, use_container_width=True)

    #- Ranking das atividades por Dia da Semana
    with col7:

        st.subheader("Ranking das Atividades Por Dia Da Semana")
        titulo =f'Ranking de Atividades em {ano_selecionado1} por dia da semana'

        if ano_selecionado1 != 'Todos':
            df_filtro_ranking_dia_semana = df_dia_semana_todos[(df_dia_semana_todos['ano'] == ano_selecionado1)]
            grafico_ranking_02 = gera_grafico_ranking_dia_semana_02_ano_mes(df_filtro_ranking_dia_semana, titulo)

        elif ano_selecionado1 == 'Todos':
            titulo =f'Ranking de Atividades por dia da semana entre {ano_inicio} e {ano_fim}'
            grafico_ranking_02 = gera_grafico_ranking_dia_semana_01(df_atvs_dia_semana_todos, titulo)

        st.altair_chart(grafico_ranking_02, use_container_width=True)

    # ====== Linha 4 ======
    col8, col9 = st.columns(2)

    if ano_selecionado1 != 'Todos':
        df_filtro_tipo = df_atvs_tipo_todos[(df_atvs_tipo_todos['ano'] == ano_selecionado1)]
        df_dia_semana = df_atvs_dia_semana_todos[(df_atvs_dia_semana_todos['ano'] == ano_selecionado1)]
    elif ano_selecionado1 == 'Todos':
        df_filtro_tipo = df_atvs_tipo_todos
        df_dia_semana = df_atvs_dia_semana_todos

    with col8:
        st.subheader(f"Atividades Por Tipo em {ano_selecionado1}")
        titulo =f'Atividades Por Tipo em {ano_selecionado1}'
        grafico_barras_emp_01 = grafico_barras_empilhadas_por_tipo(titulo, df_filtro_tipo)    
        st.altair_chart(grafico_barras_emp_01, use_container_width=True)

    with col9:
        st.subheader(f"Atividades Por Dia da Semana em {ano_selecionado1}")
        titulo =f'Atividades Por Dia da Semana em {ano_selecionado1}'
        grafico_barras_emp_02 = grafico_barras_empilhadas_por_dia_semana(titulo, df_dia_semana)    
        st.altair_chart(grafico_barras_emp_02, use_container_width=True)


    # ====== Linha 4 ======
    col10, col11 = st.columns(2)

    if st.session_state.ano_selecionado == OPCAO_TODOS:
        df_filtro_mapa_tipo = df_atvs_tipo_todos
        df_filtro_mapa_dia_semana = df_atvs_dia_semana_todos
        titulo_tipo =f'Mapa de Calor por Tipo de Atividades entre 2020 e 2025'
        titulo_dia_semana =f'Mapa de Calor por Dia da Semana entre 2020 e 2025'

    elif st.session_state.ano_selecionado != OPCAO_TODOS:
        df_filtro_mapa_tipo = df_atvs_tipo_todos[(df_atvs_tipo_todos['ano'] == ano_selecionado1)]
        df_filtro_mapa_dia_semana = df_atvs_dia_semana_todos[(df_atvs_dia_semana_todos['ano'] == ano_selecionado1)]
        titulo_tipo =f'Mapa de Calor por Tipo de Atividades em {ano_selecionado1}'
        titulo_dia_semana =f'Mapa de Calor por Dia da Semana em {ano_selecionado1}'

    with col10:
        st.subheader(f'Mapa de Calor por Tipo de Atividades em {ano_selecionado1}')
        grafico_mapa_calor_01 = gera_graficos_mapa_calor_por_tipo_atv(df_filtro_mapa_tipo, titulo_tipo)
        st.altair_chart(grafico_mapa_calor_01, use_container_width=True)

    with col11:
        st.subheader(f'Mapa de Calor por Dia da Semana em {ano_selecionado1}')
        grafico_mapa_calor_02 = gera_graficos_mapa_calor_por_dia_semana_atv(df_filtro_mapa_dia_semana, titulo_dia_semana)
        st.altair_chart(grafico_mapa_calor_02, use_container_width=True)
# ==============================================================================
with tab_detalhamento:

    # =======================================================
    # aba Detalhamento das Atividades
    # =======================================================
    titulo = f'<h3>Detalhamento das Atividades</h3>'
    st.markdown(titulo, unsafe_allow_html=True)

    # CSS adicional para botão e layout do detalhamento
    st.markdown("""
    <style>
    .btn-detalhar {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 5px 10px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 2px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    .detalhe-atividade {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Definindo os anos disponíveis para seleção
    anos_disponiveis = ['2020', '2021', '2022', '2023', '2024', '2025']
    
    # Organizando os filtros em 3 colunas
    col1, col2, col3 = st.columns(3)
    
    # Coluna 1: Filtro de ano
    with col1:
        filtro_ano = st.selectbox('Selecione o ano:', anos_disponiveis, index=5)  # Default para 2025
    
    # Coluna 2: Checkbox para habilitar filtro por mês
    with col2:
        filtrar_por_mes = st.checkbox('Filtrar por mês')
    
    # Coluna 3: Filtro de mês (aparece somente se o checkbox estiver marcado)
    with col3:
        if filtrar_por_mes:
            meses = {
                '01 - Janeiro': 1, 
                '02 - Fevereiro': 2, 
                '03 - Março': 3, 
                '04 - Abril': 4,
                '05 - Maio': 5, 
                '06 - Junho': 6, 
                '07 - Julho': 7, 
                '08 - Agosto': 8,
                '09 - Setembro': 9, 
                '10 - Outubro': 10, 
                '11 - Novembro': 11, 
                '12 - Dezembro': 12
            }
            filtro_mes = st.selectbox('Selecione o mês:', list(meses.keys()))
            mes_selecionado = meses[filtro_mes]
        else:
            mes_selecionado = None
            st.empty()  # Espaço vazio para manter alinhamento
    
    # Definir o DataFrame baseado no ano selecionado
    df_completo = None
    if filtro_ano == '2020':
        df_completo = df_atividades_completo_2020.copy()
    elif filtro_ano == '2021':
        df_completo = df_atividades_completo_2021.copy()
    elif filtro_ano == '2022':
        df_completo = df_atividades_completo_2022.copy()
    elif filtro_ano == '2023':
        df_completo = df_atividades_completo_2023.copy()
    elif filtro_ano == '2024':
        df_completo = df_atividades_completo_2024.copy()
    elif filtro_ano == '2025':
        df_completo = df_atividades_completo_2025.copy()
    
    # Filtrar por mês se necessário
    if filtrar_por_mes and mes_selecionado is not None and df_completo is not None:
        # Verificar se 'Activity Date' está no formato correto
        if 'Activity Date' in df_completo.columns:
            try:
                # Converter para datetime
                df_completo['Activity Date'] = pd.to_datetime(df_completo['Activity Date'], format='%b %d, %Y, %I:%M:%S %p', errors='coerce')
                # Extrair mês e filtrar
                df_completo = df_completo[df_completo['Activity Date'].dt.month == mes_selecionado]
            except Exception as e:
                st.error(f"Erro ao filtrar por mês: {str(e)}")
        else:
            # Tentar usar a coluna data_mes se disponível
            if 'data_mes' in df_completo.columns:
                df_completo = df_completo[df_completo['data_mes'] == mes_selecionado]
    
    # Verificar se temos dados para exibir
    if df_completo is not None and not df_completo.empty:
        # Preparar dados para a tabela
        df_tabela = df_completo.copy()
        
        # Verificar e converter 'Activity Date' para datetime
        if 'Activity Date' in df_tabela.columns:
            df_tabela['Activity Date'] = pd.to_datetime(df_tabela['Activity Date'], format='%b %d, %Y, %I:%M:%S %p', errors='coerce')
            # Criar coluna formatada para exibição
            df_tabela['Data Formatada'] = df_tabela['Activity Date'].dt.strftime('%d/%m/%Y')
            
            # Adicionar dia da semana
            df_tabela['Dia da Semana'] = df_tabela['Activity Date'].apply(
                lambda x: retorna_dia_da_semana(x.strftime('%b %d, %Y, %I:%M:%S %p')) if not pd.isna(x) else "")
        else:
            st.warning("Coluna 'Activity Date' não encontrada no conjunto de dados.")
            # Criar colunas vazias para manter a estrutura
            df_tabela['Data Formatada'] = ""
            df_tabela['Dia da Semana'] = ""
        
        # Selecionar colunas essenciais para exibição
        colunas_essenciais = ['Data Formatada', 'Dia da Semana', 'Activity Name', 'Activity Type','Filename']
        
        # Verificar se todas as colunas essenciais existem
        colunas_existentes = [col for col in colunas_essenciais if col in df_tabela.columns]
        
        # Criar dataframe para exibição
        if len(colunas_existentes) > 0:
            df_exibicao = df_tabela[colunas_existentes].copy()
            
            # Renomear colunas para português
            renomear_colunas = {
                'Data Formatada': 'Data',
                'Dia da Semana': 'Dia da Semana',
                'Activity Name': 'Nome da Atividade',
                'Activity Type': 'Tipo da Atividade',
                'Filename': 'Arquivo GPX',
                'Distance': 'Distância (km)',
                'Elapsed Time': 'Tempo (min)',
                'Average Speed': 'Velocidade Média (km/h)',
                'Max Speed': 'Velocidade Máxima (km/h)',
                'Calories': 'Calorias',
                'Elevation Gain': 'Ganho de Elevação (m)',
                'Max Heart Rate': 'FC Máxima (bpm)',
                'Average Heart Rate': 'FC Média (bpm)'
            }
            
            # Aplicar renomeação apenas para colunas que existem
            renomear = {k: v for k, v in renomear_colunas.items() if k in df_exibicao.columns}
            df_exibicao = df_exibicao.rename(columns=renomear)
            
            # Exibir a tabela usando o método dataframe do Streamlit
            st.dataframe(df_exibicao, use_container_width=True)
            
            # Área para exibir detalhes de uma atividade específica
            st.markdown('### Detalhes da Atividade')
            
            # Permitir ao usuário selecionar uma atividade para ver detalhes
            id_atividades = df_tabela['Activity ID'].astype(str).tolist()
            id_atividades_dict = {f"{row['Data Formatada']} - {row['Activity Type']} - {row['Activity ID']}": row['Activity ID'] 
                              for _, row in df_tabela.iterrows() if 'Activity Name' in row and 'Activity ID' in row}
            
            if id_atividades_dict:
                atividade_selecionada = st.selectbox('Selecione uma atividade para ver detalhes:', 
                                                 list(id_atividades_dict.keys()))
                
                id_selecionado = id_atividades_dict[atividade_selecionada]
                
                # Filtrar dados da atividade selecionada
                atividade_detalhes = df_tabela[df_tabela['Activity ID'] == id_selecionado].iloc[0]
                
                # Criar layout em duas colunas para os detalhes
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Informações Básicas")
                    st.write(f"**ID:** {atividade_detalhes.get('Activity ID', 'N/A')}")
                    st.write(f"**Nome:** {atividade_detalhes.get('Activity Name', 'N/A')}")
                    st.write(f"**Tipo:** {atividade_detalhes.get('Activity Type', 'N/A')}")
                    st.write(f"**Data:** {atividade_detalhes.get('Data Formatada', 'N/A')}")
                    st.write(f"**Dia da Semana:** {atividade_detalhes.get('Dia da Semana', 'N/A')}")
                    st.write(f"**GPX File:** {atividade_detalhes.get('Filename', 'N/A')}")

                    if 'Activity Description' in atividade_detalhes and not pd.isna(atividade_detalhes['Activity Description']):
                        st.write(f"**Descrição:** {atividade_detalhes['Activity Description']}")
                
                with col2:
                    st.subheader("Métricas da Atividade")
                    
                    # Verificar e exibir métricas disponíveis
                    if 'Distance' in atividade_detalhes and not pd.isna(atividade_detalhes['Distance']):
                        st.metric("Distância", f"{float(atividade_detalhes['Distance']):.2f} km")
                    
                    if 'Elapsed Time' in atividade_detalhes and not pd.isna(atividade_detalhes['Elapsed Time']):
                        tempo_seg = float(atividade_detalhes['Elapsed Time'])
                        tempo_min = tempo_seg / 60  # Convertendo segundos para minutos
                        st.metric("Tempo", f"{tempo_min:.2f} min")
                    
                    if 'Average Speed' in atividade_detalhes and not pd.isna(atividade_detalhes['Average Speed']):
                        st.metric("Velocidade Média", f"{float(atividade_detalhes['Average Speed']):.2f} km/h")
                    
                    if 'Max Speed' in atividade_detalhes and not pd.isna(atividade_detalhes['Max Speed']):
                        st.metric("Velocidade Máxima", f"{float(atividade_detalhes['Max Speed']):.2f} km/h")
                    
                    if 'Calories' in atividade_detalhes and not pd.isna(atividade_detalhes['Calories']):
                        st.metric("Calorias", f"{float(atividade_detalhes['Calories']):.0f}")
                
                # Verificar se existe arquivo GPX para a atividade
                filename = atividade_detalhes.get('Filename', '')
                tcx_id = None
                
                if isinstance(filename, str) and filename.startswith('activities/'):
                    # Extrair ID do arquivo
                    tcx_id = filename.replace('activities/', '').split('.')[0]
                    #print(f"tcx_id => {tcx_id}")
                
                # Verificar se existe arquivo TCX na pasta 'arquivos-ok'
                if tcx_id:
                    import os
                    tcx_filepath_ok = f"activities-tcx/arquivos-ok/{tcx_id}.tcx"
                    csv_filepath = f"activities-tcx/arquivos-csv/{tcx_id}.csv"
                    
                    if os.path.exists(tcx_filepath_ok):
                        st.success(f"Arquivo TCX encontrado: {tcx_id}.tcx")
                        
                        # Verificar se existe o CSV correspondente
                        if os.path.exists(csv_filepath):
                            try:
                                # Carregar o dataframe do CSV
                                df_rota = pd.read_csv(csv_filepath)
                                st.success(f"Dados da rota carregados com sucesso! ({df_rota.shape[0]} pontos)")
                                
                                # Verificar se o DataFrame tem colunas de latitude e longitude
                                if 'latitude' in df_rota.columns and 'longitude' in df_rota.columns:
                                    # Criar um mapa com os pontos da rota
                                    st.subheader("Mapa da Rota")
                                    
                                    # Calcular o centro do mapa
                                    lat_medio = df_rota['latitude'].mean()
                                    lon_medio = df_rota['longitude'].mean()
                                    
                                    # Criar o mapa
                                    m = folium.Map(location=[lat_medio, lon_medio], zoom_start=14)
                                    
                                    # Adicionar os pontos como uma linha
                                    points = list(zip(df_rota['latitude'], df_rota['longitude']))
                                    
                                    # Adicionar uma linha conectando os pontos (traçar a rota)
                                    folium.PolyLine(
                                        points,
                                        weight=5,
                                        color='blue',
                                        opacity=0.7
                                    ).add_to(m)
                                    
                                    # Adicionar marcadores para o início e o fim da rota
                                    folium.Marker(
                                        location=[df_rota['latitude'].iloc[0], df_rota['longitude'].iloc[0]],
                                        popup='Início',
                                        icon=folium.Icon(color='green')
                                    ).add_to(m)
                                    
                                    folium.Marker(
                                        location=[df_rota['latitude'].iloc[-1], df_rota['longitude'].iloc[-1]],
                                        popup='Fim',
                                        icon=folium.Icon(color='red')
                                    ).add_to(m)
                                    
                                    # Exibir o mapa
                                    st_folium(m, width=900, returned_objects=[])
                                    
                                else:
                                    st.warning("O arquivo CSV não contém coordenadas de latitude e longitude.")
                            
                            except Exception as e:
                                st.error(f"Erro ao carregar o arquivo CSV: {str(e)}")
                        else:
                            st.warning(f"Arquivo CSV correspondente não encontrado: {csv_filepath}")
                    else:
                        st.info(f"Arquivo TCX não encontrado na pasta 'arquivos-ok': {tcx_filepath_ok}")
        else:
            st.error("Não foi possível exibir os dados. Nenhuma coluna essencial encontrada.")
    else:
        st.warning("Não há dados disponíveis para os filtros selecionados.")

# ==============================================================================
with tab_corrida:
    
    # =======================================================
    # Aba Corrida - Análise do Evening Run
    # =======================================================
    st.title("🏃 Análise da Corrida - Evening Run")
    
    # Função para processar arquivo GPX
    def processar_gpx(caminho_arquivo):
        """Processa arquivo GPX e retorna dataframe com os dados"""
        try:
            with open(caminho_arquivo, 'r') as gpx_file:
                gpx = gpxpy.parse(gpx_file)
            
            dados = []
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        # Extrair dados básicos
                        row = {
                            'latitude': point.latitude,
                            'longitude': point.longitude,
                            'elevation': point.elevation if point.elevation else 0,
                            'time': point.time
                        }
                        
                        # Extrair extensões (frequência cardíaca e cadência)
                        if point.extensions:
                            for extension in point.extensions:
                                for child in extension:
                                    if 'hr' in child.tag:
                                        row['heart_rate'] = int(child.text) if child.text else None
                                    elif 'cad' in child.tag:
                                        row['cadence'] = int(child.text) if child.text else None
                        
                        dados.append(row)
            
            df = pd.DataFrame(dados)
            
            # Calcular métricas adicionais
            if len(df) > 1:
                # Calcular distâncias entre pontos consecutivos
                distances = []
                speeds = []
                time_diffs = []
                
                for i in range(1, len(df)):
                    # Distância usando fórmula de Haversine
                    lat1, lon1 = df.iloc[i-1]['latitude'], df.iloc[i-1]['longitude']
                    lat2, lon2 = df.iloc[i]['latitude'], df.iloc[i]['longitude']
                    
                    # Conversão para radianos
                    lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
                    lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)
                    
                    # Fórmula de Haversine
                    dlat = lat2_rad - lat1_rad
                    dlon = lon2_rad - lon1_rad
                    a = np.sin(dlat/2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon/2)**2
                    c = 2 * np.arcsin(np.sqrt(a))
                    distance = 6371 * c * 1000  # Distância em metros
                    
                    distances.append(distance)
                    
                    # Calcular diferença de tempo
                    if df.iloc[i]['time'] and df.iloc[i-1]['time']:
                        time_diff = (df.iloc[i]['time'] - df.iloc[i-1]['time']).total_seconds()
                        time_diffs.append(time_diff)
                        
                        # Calcular velocidade (m/s -> km/h)
                        if time_diff > 0:
                            speed = (distance / time_diff) * 3.6
                            speeds.append(speed)
                        else:
                            speeds.append(0)
                    else:
                        time_diffs.append(0)
                        speeds.append(0)
                
                # Adicionar dados ao DataFrame
                df['distance_m'] = [0] + distances
                df['speed_kmh'] = [0] + speeds
                df['time_diff'] = [0] + time_diffs
                df['cumulative_distance'] = df['distance_m'].cumsum() / 1000  # km
                df['cumulative_time'] = df['time_diff'].cumsum() / 60  # minutos
            
            return df
            
        except Exception as e:
            st.error(f"Erro ao processar arquivo GPX: {str(e)}")
            return None
    
    # Carregar dados do GPX
    caminho_gpx = "dados-corrida/Evening_Run.gpx"
    df_corrida = processar_gpx(caminho_gpx)
    
    if df_corrida is not None and not df_corrida.empty:
        
        # Mostrar informações das imagens de referência
        st.subheader("📊 Visualizações baseadas nos dados de referência:")
        col_img1, col_img2, col_img3, col_img4 = st.columns(4)
        
        with col_img1:
            st.image("dados-corrida/dados-01.jpeg", caption="Referência 01", use_container_width=True)
        with col_img2:
            st.image("dados-corrida/dados-02.jpeg", caption="Referência 02", use_container_width=True)
        with col_img3:
            st.image("dados-corrida/dados-03.jpeg", caption="Referência 03", use_container_width=True)
        with col_img4:
            st.image("dados-corrida/dados-04.jpeg", caption="Referência 04", use_container_width=True)
        
        st.markdown("---")
        
        # Métricas principais
        st.subheader("📈 Métricas da Corrida")
        
        # Calcular métricas
        distancia_total = df_corrida['cumulative_distance'].max()
        tempo_total = df_corrida['cumulative_time'].max()
        velocidade_media = df_corrida[df_corrida['speed_kmh'] > 0]['speed_kmh'].mean()
        velocidade_maxima = df_corrida['speed_kmh'].max()
        
        # Frequência cardíaca
        fc_media = df_corrida[df_corrida['heart_rate'].notna()]['heart_rate'].mean() if 'heart_rate' in df_corrida.columns else None
        fc_maxima = df_corrida[df_corrida['heart_rate'].notna()]['heart_rate'].max() if 'heart_rate' in df_corrida.columns else None
        
        # Elevação
        elevacao_min = df_corrida['elevation'].min()
        elevacao_max = df_corrida['elevation'].max()
        ganho_elevacao = elevacao_max - elevacao_min
        
        # Exibir métricas em colunas
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Distância Total", f"{distancia_total:.2f} km")
        with col2:
            st.metric("Tempo Total", f"{tempo_total:.1f} min")
        with col3:
            st.metric("Velocidade Média", f"{velocidade_media:.1f} km/h" if not np.isnan(velocidade_media) else "N/A")
        with col4:
            if fc_media:
                st.metric("FC Média", f"{fc_media:.0f} bpm")
            else:
                st.metric("FC Média", "N/A")
        with col5:
            st.metric("Ganho Elevação", f"{ganho_elevacao:.1f} m")
        
        st.markdown("---")
        
        # Gráficos baseados nas imagens de referência
        st.subheader("📊 Visualizações da Corrida")
        
        # Gráfico 1: Velocidade ao longo do tempo (inspirado na imagem 01)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Velocidade ao Longo do Tempo")
            fig_speed = px.line(df_corrida, x='cumulative_time', y='speed_kmh',
                               title='Velocidade (km/h) vs Tempo (min)',
                               labels={'cumulative_time': 'Tempo (min)', 'speed_kmh': 'Velocidade (km/h)'})
            fig_speed.update_traces(line_color='blue')
            st.plotly_chart(fig_speed, width="use_container")
        
        with col2:
            st.subheader("Frequência Cardíaca")
            if 'heart_rate' in df_corrida.columns and df_corrida['heart_rate'].notna().any():
                fig_hr = px.line(df_corrida, x='cumulative_time', y='heart_rate',
                                title='Frequência Cardíaca (bpm) vs Tempo (min)',
                                labels={'cumulative_time': 'Tempo (min)', 'heart_rate': 'FC (bpm)'})
                fig_hr.update_traces(line_color='red')
                st.plotly_chart(fig_hr, width="use_container")
            else:
                st.info("Dados de frequência cardíaca não disponíveis")
        
        # Gráfico 2: Perfil de elevação (inspirado na imagem 02)
        st.subheader("Perfil de Elevação")
        fig_elevation = px.area(df_corrida, x='cumulative_distance', y='elevation',
                               title='Perfil de Elevação ao Longo da Corrida',
                               labels={'cumulative_distance': 'Distância (km)', 'elevation': 'Elevação (m)'})
        fig_elevation.update_traces(fill='tonexty', fillcolor='rgba(0,100,80,0.2)', line_color='green')
        st.plotly_chart(fig_elevation, width="use_container")
        
        # Gráfico 3: Pace vs Distância (inspirado na imagem 03)
        st.subheader("Ritmo ao Longo da Corrida")
        # Calcular pace (min/km)
        df_corrida['pace'] = np.where(df_corrida['speed_kmh'] > 0, 60 / df_corrida['speed_kmh'], 0)
        df_corrida['pace'] = np.where(df_corrida['pace'] > 15, 15, df_corrida['pace'])  # Limitar valores extremos
        
        fig_pace = px.line(df_corrida, x='cumulative_distance', y='pace',
                          title='Ritmo (min/km) vs Distância (km)',
                          labels={'cumulative_distance': 'Distância (km)', 'pace': 'Ritmo (min/km)'})
        fig_pace.update_traces(line_color='orange')
        st.plotly_chart(fig_pace, width="use_container")
        
        # Gráfico 4: Cadência (inspirado na imagem 04)
        if 'cadence' in df_corrida.columns and df_corrida['cadence'].notna().any():
            st.subheader("Cadência ao Longo do Tempo")
            fig_cadence = px.line(df_corrida, x='cumulative_time', y='cadence',
                                 title='Cadência (passos/min) vs Tempo (min)',
                                 labels={'cumulative_time': 'Tempo (min)', 'cadence': 'Cadência (spm)'})
            fig_cadence.update_traces(line_color='purple')
            st.plotly_chart(fig_cadence, width="use_container")
        
        # Mapa da rota
        st.subheader("🗺️ Mapa da Rota")
        
        # Criar mapa
        lat_centro = df_corrida['latitude'].mean()
        lon_centro = df_corrida['longitude'].mean()
        
        m = folium.Map(location=[lat_centro, lon_centro], zoom_start=14)
        
        # Adicionar rota como linha
        pontos_rota = list(zip(df_corrida['latitude'], df_corrida['longitude']))
        
        folium.PolyLine(
            pontos_rota,
            weight=4,
            color='blue',
            opacity=0.8,
            popup='Rota da Corrida'
        ).add_to(m)
        
        # Marcadores de início e fim
        folium.Marker(
            location=[df_corrida['latitude'].iloc[0], df_corrida['longitude'].iloc[0]],
            popup='Início da Corrida',
            icon=folium.Icon(color='green', icon='play')
        ).add_to(m)
        
        folium.Marker(
            location=[df_corrida['latitude'].iloc[-1], df_corrida['longitude'].iloc[-1]],
            popup='Fim da Corrida',
            icon=folium.Icon(color='red', icon='stop')
        ).add_to(m)
        
        # Exibir mapa
        st_folium(m, width=1000, height=600, returned_objects=[])
        
        # Análise estatística adicional
        st.subheader("📋 Análise Estatística Detalhada")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Resumo da Velocidade:**")
            st.write(f"• Velocidade Média: {velocidade_media:.2f} km/h")
            st.write(f"• Velocidade Máxima: {velocidade_maxima:.2f} km/h")
            st.write(f"• Velocidade Mínima: {df_corrida[df_corrida['speed_kmh'] > 0]['speed_kmh'].min():.2f} km/h")
            
            if 'pace' in df_corrida.columns:
                pace_medio = df_corrida[df_corrida['pace'] > 0]['pace'].mean()
                st.write(f"• Ritmo Médio: {pace_medio:.2f} min/km")
        
        with col2:
            if fc_media:
                st.write("**Resumo da Frequência Cardíaca:**")
                st.write(f"• FC Média: {fc_media:.0f} bpm")
                st.write(f"• FC Máxima: {fc_maxima:.0f} bpm")
                fc_minima = df_corrida[df_corrida['heart_rate'].notna()]['heart_rate'].min()
                st.write(f"• FC Mínima: {fc_minima:.0f} bpm")
            
            st.write("**Resumo da Elevação:**")
            st.write(f"• Elevação Mínima: {elevacao_min:.1f} m")
            st.write(f"• Elevação Máxima: {elevacao_max:.1f} m")
            st.write(f"• Ganho de Elevação: {ganho_elevacao:.1f} m")
        
        # Tabela com dados brutos (amostra)
        if st.checkbox("Mostrar dados brutos (primeiros 100 pontos)"):
            st.subheader("Dados do GPX (Amostra)")
            colunas_mostrar = ['time', 'latitude', 'longitude', 'elevation', 'speed_kmh', 'cumulative_distance']
            if 'heart_rate' in df_corrida.columns:
                colunas_mostrar.append('heart_rate')
            if 'cadence' in df_corrida.columns:
                colunas_mostrar.append('cadence')
            
            st.dataframe(df_corrida[colunas_mostrar].head(100), width="use_container")
    
    else:
        st.error("Não foi possível carregar os dados do arquivo GPX. Verifique se o arquivo existe e está no formato correto.")

# ==============================================================================