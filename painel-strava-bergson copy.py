# =======================================================
# Imports
# =======================================================
import pandas as pd
import streamlit as st

from PIL import Image
from painel_strava_graficos import *

# ==================================
# Funções
# ==================================

# ==================================
def retorna_ano_data(data_string):
    from datetime import datetime

    formato = "%b %d, %Y, %I:%M:%S %p"  # Formato da sua string de data

    data_objeto = datetime.strptime(data_string, formato)
    ano = data_objeto.year

    return ano
# ==================================
def retorna_mes_data(data_string):
    from datetime import datetime

    formato = "%b %d, %Y, %I:%M:%S %p"  # Formato da sua string de data

    data_objeto = datetime.strptime(data_string, formato)
    mes = data_objeto.month

    return mes
# ==================================
def retorna_atividades_mes_ano(df2, ano, mes):
    df_lista_mes_ano = df2[(df2['data_ano'] == int(ano)) & (df2['data_mes'] == int(mes)) ]
    return df_lista_mes_ano    
# ==================================
def retorna_atividades_ano(df2, ano):
    lista_dfs_mes = []

    for mes in range(1,13):
        df_lista_mes = df2[(df2['data_ano'] == int(ano)) & (df2['data_mes'] == int(mes)) ]
        lista_dfs_mes.append(df_lista_mes)

    return lista_dfs_mes    
# ==================================

# =======================================================
# Datasets
# =======================================================
df_atividades_todos = pd.read_csv('atividades.csv', sep=',', encoding="ISO-8859-1")
#df_atividades_todos

df_atv_v2 = pd.read_csv('atividades_fisicas_bergson_v2.csv', sep=',', encoding="ISO-8859-1")

# =======================================================
# Constantes do dashboard
# =======================================================
OPCAO_TODOS = 'Todos'
OPCAO_NONE = None
COLUNA_ANO = 'ano'

OPCAO_FILTRO_POR_UM_ANO = "Filtro por Um Ano"
OPCAO_FILTRO_POR_PERIODO = "Filtro por Período"
opcoes = [OPCAO_FILTRO_POR_UM_ANO, OPCAO_FILTRO_POR_PERIODO]

ano_inicio = None
ano_fim = None

#st.set_page_config(layout="wide")
st.set_page_config(
    page_title="My Streamlit App",
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

if 'opcao_selecionada' not in st.session_state:
    st.session_state.opcao_selecionada = OPCAO_FILTRO_POR_UM_ANO  # Define "opcao1" como padrão

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
            (OPCAO_TODOS, '2025','2024', '2023', '2022', '2021', '2020'),
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
            ano_inicio = st.sidebar.number_input("Ano de Início", key=ano_inicio, min_value=2007, max_value=2024, step=1, value=2020)
        with col2:
            ano_fim = st.sidebar.number_input("Ano de Fim", key=ano_fim, min_value=2007, max_value=2024, step=1, value=2024)

        # Validação básica para garantir que o ano de início não seja posterior ao ano de fim
        if ano_inicio > ano_fim:
            st.sidebar.error("Erro: O ano de início não pode ser posterior ao ano de fim.")
            ano_inicio = None  # Reseta os valores para evitar processamento incorreto
            ano_fim = None


st.sidebar.write(f"Opção selecionada: {st.session_state.opcao_selecionada}")

# Definição de abas
tab_bbb_01,tab01, tab02, tab03, tab06, tab07, tab09, tab04 = st.tabs(
  [
    "Atividades",  
    "Acidentes por Critérios",
    "Rankings Diversos",   
    "Gráficos de Fluxo",
    "Gráficos de Barras Empilhadas",
    "Gráficos de Distribuição",    
    "Mapa dos Acidentes",
    "Mapa de Calor",  
  ]
)

lista_cores_graficos = [
    '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
    '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
    '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
]

lista_novas_cores = [
  # Tons pastel
  '#F8B195', '#F4DCCF', '#B7C9E2', '#A7D1F8', '#FDEBD0',
  # Tons vibrantes
  '#FF5733', '#C70039', '#900C3F', '#581845', '#F24E1C',
  # Tons neutros
  '#969696', '#707070', '#595959', '#404040', '#262626',
  # Tons terrosos
  '#8B4513', '#A0522D', '#D2691E', '#B22222', '#800000',
  # Tons frios
  '#1E90FF', '#4169E1', '#6495ED', '#7B68EE', '#008B8B',
  # Tons quentes
  '#FF8C00', '#FFA500', '#FF4500', '#FF6347', '#FF8C69',
  # Tons pastel suaves
  '#E1F5FE', '#F0FFF0', '#F5F5DC', '#FFF8DC', '#F0E68C'
]

# ==============================================================================
with tab_bbb_01:

    # =======================================================
    # aba tab_bbb_01
    # =======================================================
    titulo = f'<h3> Atividades Físicas'
    st.markdown(titulo, unsafe_allow_html=True)  

    titulo2 = f'<h4> ano_selecionado => {ano_selecionado} | exibir_filtro_periodo_anos => {exibir_filtro_periodo_anos} | ano_inicio => {ano_inicio} | ano_fim => {ano_fim}'
    print(f'titulo2 = {titulo2}')

    lista_dfs = retorna_atividades_ano(df_atv_v2, 2024)

    #for mes in range(0, 12):
    #    st.title(f' Atividades Físicas do mês {mes}')
    #    st.table(lista_dfs[mes])

    st.markdown('Janeiro', unsafe_allow_html=True)  
    #st.table(lista_dfs[0])    

    st.markdown('Fevereiro', unsafe_allow_html=True)  
    #st.table(lista_dfs[1])    

# ==============================================================================
with tab01:

    # =======================================================
    # aba 01
    # =======================================================
    titulo = f'<h3> Acidentes por UF / Tipo / BR / Causa / Classificação / Fase do Dia / Condição Metereológica / Dia da Semana / Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)  

    titulo2 = f'<h4> ano_selecionado => {ano_selecionado} | exibir_filtro_periodo_anos => {exibir_filtro_periodo_anos} | ano_inicio => {ano_inicio} | ano_fim => {ano_fim}'
    print(f'titulo2 = {titulo2}')

    tab1_sub1, tab1_sub2, tab1_sub3, tab1_sub4, tab1_sub5, tab1_sub6, tab1_sub7, tab1_sub8, tab1_sub9  = st.tabs(
        [
            "Acidentes por UF", "Acidentes por Tipo", "Acidentes por BR", 
            "Acidentes por Causa", "Acidentes por Classificação", "Acidentes por Fase do Dia", 
            "Acidentes por Condição Metereológica", "Acidentes por Dia da Semana",
            "Acidentes por Tipo de Veículo"
        ])

    # =====================================
    # Filtro para a aba tab1_sub1 de UF
    # =====================================
    qtd_ufs_selecionadas = tab1_sub1.radio(
        "Selecione a quantidade de UF deseja visaulizar:",
        ("Top 10 UFs", "Top 20 UFs", "Todas as UFs"), index=0, horizontal=True, key='radio_uf'
    )
    print(f'qtd_ufs_selecionadas = {qtd_ufs_selecionadas}')

    if qtd_ufs_selecionadas == "Top 10 UFs":
        df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_10
    elif qtd_ufs_selecionadas == "Top 20 UFs":
        df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_20
    elif qtd_ufs_selecionadas == "Todas as UFs":    
        df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_todos

    # =====================================
    # Filtro para a aba tab1_sub3 de BR
    # =====================================
    qtd_brs_selecionadas = tab1_sub3.radio(
        "Selecione a quantidade de BR deseja visaulizar:",
        ("Top 10 BRs", "Top 20 BRs", "Top 30 BRs", "Top 40 BRs", "Top 50 BRs"), index=0, horizontal=True, key='radio_br'
    )
    print(f'qtd_brs_selecionadas = {qtd_brs_selecionadas}')

    if qtd_brs_selecionadas == "Top 10 BRs":
        df_acidentes_geral_por_br = df_acidentes_geral_por_br_10
    elif qtd_brs_selecionadas == "Top 20 BRs":
        df_acidentes_geral_por_br = df_acidentes_geral_por_br_20
    elif qtd_brs_selecionadas == "Top 30 BRs":
        df_acidentes_geral_por_br = df_acidentes_geral_por_br_30
    elif qtd_brs_selecionadas == "Top 40 BRs":
        df_acidentes_geral_por_br = df_acidentes_geral_por_br_40
    elif qtd_brs_selecionadas == "Top 50 BRs":
        df_acidentes_geral_por_br = df_acidentes_geral_por_br_50

    if ano_selecionado != OPCAO_TODOS and ano_selecionado != None:

      df_filtrado_uf = df_acidentes_geral_por_uf[(df_acidentes_geral_por_uf[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por UF em {ano_selecionado}'
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_filtrado_uf)

      df_filtrado_tipo = df_acidentes_geral_por_tipo[(df_acidentes_geral_por_tipo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Tipo em {ano_selecionado}'  
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_filtrado_tipo)

      df_filtrado_br = df_acidentes_geral_por_br[(df_acidentes_geral_por_br[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por BR em {ano_selecionado}'  
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_filtrado_br)

      df_filtrado_causa = df_acidentes_geral_por_causa[(df_acidentes_geral_por_causa[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Causa em {ano_selecionado}'  
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_filtrado_causa)

      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[(df_acidentes_geral_por_classificacao[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Classificacao em {ano_selecionado}'  
      grafico_aba_05 = gera_grafico_por_classificacao(titulo, df_filtrado_classificacao)

      df_filtrado_fasedia = df_acidentes_geral_por_fasedia[(df_acidentes_geral_por_fasedia[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Fase do Dia em {ano_selecionado}'  
      grafico_aba_06 = gera_grafico_por_fase_dia(titulo, df_filtrado_fasedia)

      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicao_metereologica[(df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Condição Metereológica em {ano_selecionado}'  
      grafico_aba_07 = gera_grafico_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)

      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[(df_acidentes_geral_por_dia_semana[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Dia da Semana em {ano_selecionado}'  
      grafico_aba_08 = gera_grafico_por_dia_semana(titulo, df_filtrado_dia_semana)

      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[(df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Tipo de Veículo em {ano_selecionado}'  
      grafico_aba_09 = gera_grafico_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)
    
    elif ano_selecionado == OPCAO_TODOS:

      titulo = f'Acidentes por UF (Geral)'    
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_acidentes_geral_por_uf)

      titulo = f'Acidentes por Tipo (Geral)'    
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_acidentes_geral_por_tipo)

      titulo = f'Acidentes por BR (Geral)'    
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_acidentes_geral_por_br)

      titulo = f'Acidentes por Causa (Geral)'    
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_acidentes_geral_por_causa)

      titulo = f'Acidentes por Classificacao (Geral)'    
      grafico_aba_05 = gera_grafico_por_classificacao(titulo, df_acidentes_geral_por_classificacao)

      titulo = f'Acidentes por Fase do Dia (Geral)'    
      grafico_aba_06 = gera_grafico_por_fase_dia(titulo, df_acidentes_geral_por_fasedia)

      titulo = f'Acidentes por Condição Metereológica (Geral)'    
      grafico_aba_07 = gera_grafico_por_condicao_metereologica(titulo, df_acidentes_geral_por_condicao_metereologica)

      titulo = f'Acidentes por Dia da Semana (Geral)'  
      grafico_aba_08 = gera_grafico_por_dia_semana(titulo, df_acidentes_geral_por_dia_semana)

      titulo = f'Acidentes por Tipo de Veículo (Geral)'  
      grafico_aba_09 = gera_grafico_por_tipo_veiculo(titulo, df_acidentes_geral_por_tipo_veiculo)

    elif exibir_filtro_periodo_anos and (ano_inicio is not None and ano_fim is not None):

      df_filtrado_uf = df_acidentes_geral_por_uf[
          (df_acidentes_geral_por_uf[COLUNA_ANO] >= int(ano_inicio)) & 
          (df_acidentes_geral_por_uf[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por UF entre {ano_inicio} e {ano_fim}'
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_filtrado_uf)

      df_filtrado_tipo = df_acidentes_geral_por_tipo[
          (df_acidentes_geral_por_tipo[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_tipo[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por Tipo entre {ano_inicio} e {ano_fim}'  
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_filtrado_tipo)

      df_filtrado_br = df_acidentes_geral_por_br[
          (df_acidentes_geral_por_br[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_br[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por BR entre {ano_inicio} e {ano_fim}'  
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_filtrado_br)

      df_filtrado_causa = df_acidentes_geral_por_causa[
          (df_acidentes_geral_por_causa[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_causa[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por Causa entre {ano_inicio} e {ano_fim}'  
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_filtrado_causa)

      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] <= int(ano_fim)) 
      ]
      titulo = f'Acidentes por Classificacao entre {ano_inicio} e {ano_fim}'  
      grafico_aba_05 = gera_grafico_por_classificacao(titulo, df_filtrado_classificacao)

      df_filtrado_fasedia = df_acidentes_geral_por_fasedia[
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] <= int(ano_fim))
      ] 
      titulo = f'Acidentes por Fase do Dia entre {ano_inicio} e {ano_fim}'  
      grafico_aba_06 = gera_grafico_por_fase_dia(titulo, df_filtrado_fasedia)

      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicao_metereologica[
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por Condição Metereológica entre {ano_inicio} e {ano_fim}'  
      grafico_aba_07 = gera_grafico_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)

      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Acidentes por Dia da Semana entre {ano_inicio} e {ano_fim}'  
      grafico_aba_08 = gera_grafico_por_dia_semana(titulo, df_filtrado_dia_semana)

      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[
          (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] >= int(ano_inicio))  &
            (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] <= int(ano_fim))  
      ]
      titulo = f'Acidentes por Tipo de Veículo entre {ano_inicio} e {ano_fim}'  
      grafico_aba_09 = gera_grafico_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)
    # =====================================================================================

    # Exibir o gráfico de barras empilhadas
    with tab1_sub1:
        st.altair_chart(grafico_aba_01)
    with tab1_sub2:    
        st.altair_chart(grafico_aba_02)
    with tab1_sub3:            
        st.altair_chart(grafico_aba_03)
    with tab1_sub4:    
        st.altair_chart(grafico_aba_04)
    with tab1_sub5:        
        st.altair_chart(grafico_aba_05)
    with tab1_sub6:        
        st.altair_chart(grafico_aba_06)
    with tab1_sub7:        
        st.altair_chart(grafico_aba_07)
    with tab1_sub8:        
        st.altair_chart(grafico_aba_08)
    with tab1_sub9:        
        st.altair_chart(grafico_aba_09)

# ==============================================================================
with tab02:    

    tab2_sub1, tab2_sub2, tab2_sub3, tab2_sub8, tab2_sub4, tab2_sub5, tab2_sub9, tab2_sub6, tab2_sub7 = st.tabs(
        ["Ranking por UF", "Ranking por Tipo", 
         "Ranking por BR", "Ranking por Causa", 
         "Ranking por Classificação", 
         "Ranking por Fase do Dia", "Ranking por Condição Metereológica", 
         "Ranking por Dia da Semana",
         "Ranking por Tipo de Veículo"
        ]
    )
    
    with tab2_sub1:

        # ========================================================
        # Aba 02 - Acidentes por UF
        # ========================================================        
        titulo = f'<h2> Ranking dos Acidentes por UF (2007 a 2024)'
        st.markdown(titulo, unsafe_allow_html=True)  
       
        qtd_ufs_selecionadas = tab2_sub1.radio(
            "Selecione a quantidade de UFs deseja no Ranking:",
            ("Top 10 UFs", "Top 20 UFs", "Todas as UFs"), index=0, horizontal=True
        )
        print(f'qtd_ufs_selecionadas = {qtd_ufs_selecionadas}')

        if qtd_ufs_selecionadas == "Top 10 UFs":
            df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_10
        elif qtd_ufs_selecionadas == "Top 20 UFs":
            df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_20
        elif qtd_ufs_selecionadas == "Todas as UFs":    
            df_acidentes_geral_por_uf = df_acidentes_geral_por_uf_todos

        st.altair_chart(gera_grafico_ranking_uf_01_interativo(df_acidentes_geral_por_uf))   
        st.altair_chart(gera_grafico_ranking_uf_02(df_acidentes_geral_por_uf))
    
    with tab2_sub2:

        # ========================================================
        # Aba 02 - Acidentes por Tipo
        # ========================================================               
        titulo = f'<h2> Ranking dos Acidentes por Tipo (2007 e 2024)'
        st.markdown(titulo, unsafe_allow_html=True)   
       
        st.altair_chart(gera_grafico_ranking_tipo_01_interativo(df_acidentes_geral_por_tipo))   
        st.altair_chart(gera_grafico_ranking_tipo_02(df_acidentes_geral_por_tipo))
    
    with tab2_sub3:

        # =====================================
        # Filtro para a aba tab1_sub3 de BR
        # =====================================
        qtd_brs_selecionadas = tab2_sub3.radio(
            "Selecione a quantidade de BR deseja visaulizar:",
            ("Top 10 BRs", "Top 20 BRs", "Top 30 BRs", "Top 40 BRs", "Top 50 BRs"), index=0, horizontal=True, key='radio_br_ranking'
        )
        print(f'qtd_brs_selecionadas = {qtd_brs_selecionadas}')

        if qtd_brs_selecionadas == "Top 10 BRs":
            df_acidentes_geral_por_br = df_acidentes_geral_por_br_10
        elif qtd_brs_selecionadas == "Top 20 BRs":
            df_acidentes_geral_por_br = df_acidentes_geral_por_br_20
        elif qtd_brs_selecionadas == "Top 30 BRs":
            df_acidentes_geral_por_br = df_acidentes_geral_por_br_30
        elif qtd_brs_selecionadas == "Top 40 BRs":
            df_acidentes_geral_por_br = df_acidentes_geral_por_br_40
        elif qtd_brs_selecionadas == "Top 50 BRs":
            df_acidentes_geral_por_br = df_acidentes_geral_por_br_50

        # ========================================================
        # Aba 02 - Acidentes por BR
        # ========================================================               
        titulo = f'<h2> Ranking dos Acidentes por BR (2007 e 2024)'
        st.markdown(titulo, unsafe_allow_html=True)
      
        st.altair_chart(gera_grafico_ranking_br_01(qtd_brs_selecionadas, df_acidentes_geral_por_br))   
        st.altair_chart(gera_grafico_ranking_br_02(qtd_brs_selecionadas, df_acidentes_geral_por_br))
    
    with tab2_sub8:

        # ========================================================
        # Aba 02 - Acidentes por Dia da Semana
        # ========================================================               
        titulo = f'<H2> Ranking por Causa de Acidente'
        st.markdown(titulo, unsafe_allow_html=True)
    
        #st.altair_chart(gera_grafico_ranking_causa_01(df_acidentes_geral_por_causa))   
        st.altair_chart(gera_grafico_ranking_causa_01_interativo(df_acidentes_geral_por_causa))   
        st.altair_chart(gera_grafico_ranking_causa_02(df_acidentes_geral_por_causa))

    with tab2_sub4:

        # ========================================================
        # Aba 02 - Acidentes por Classificação
        # ========================================================        
        titulo = f'<H2> Ranking por Classificação'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_classificacao_01(df_acidentes_geral_por_classificacao))
        st.altair_chart(gera_grafico_ranking_classificacao_02(df_acidentes_geral_por_classificacao))
    
    with tab2_sub5:

        # ========================================================
        # Aba 02 - Acidentes por Fase do Dia
        # ========================================================               
        titulo = f'<H2> Ranking por Fase do Dia'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_fasedia_01(df_acidentes_geral_por_fasedia))   
        st.altair_chart(gera_grafico_ranking_fasedia_02(df_acidentes_geral_por_fasedia))

    with tab2_sub9:

        # ========================================================
        # Aba 02 - Acidentes por Condição Metereológica
        # ========================================================               
        titulo = f'<H2> Ranking por Condicao Metereológica'
        st.markdown(titulo, unsafe_allow_html=True)
    
        #st.altair_chart(gera_grafico_ranking_condicao_metereologica_01(df_acidentes_geral_por_condicao_metereologica))   
        st.altair_chart(gera_grafico_ranking_condicao_metereologica_01_interativo(df_acidentes_geral_por_condicao_metereologica))   
        st.altair_chart(gera_grafico_ranking_condicao_metereologica_02(df_acidentes_geral_por_condicao_metereologica))

    with tab2_sub6:

        # ========================================================
        # Aba 02 - Acidentes por Dia da Semana
        # ========================================================               
        titulo = f'<H2> Ranking por Dia da Semana'
        st.markdown(titulo, unsafe_allow_html=True)
    
        #st.altair_chart(gera_grafico_ranking_diasemana_01(df_acidentes_geral_por_dia_semana))   
        st.altair_chart(gera_grafico_ranking_diasemana_01_interativo(df_acidentes_geral_por_dia_semana))   
        st.altair_chart(gera_grafico_ranking_diasemana_02(df_acidentes_geral_por_dia_semana))

    with tab2_sub7:

        # ========================================================
        # Aba 02 - Acidentes por Dia da Semana
        # ========================================================               
        titulo = f'<H2> Ranking por Tipo de Veículo'
        st.markdown(titulo, unsafe_allow_html=True)
    
        #st.altair_chart(gera_grafico_ranking_tipoveiculo_01(df_acidentes_geral_por_tipo_veiculo))   
        st.altair_chart(gera_grafico_ranking_tipoveiculo_01_interativo(df_acidentes_geral_por_tipo_veiculo))   
        st.altair_chart(gera_grafico_ranking_tipoveiculo_02(df_acidentes_geral_por_tipo_veiculo))

# ==========================================================================
def gera_grafico_ranking_classificacao_01(df_acidentes_geral_por_classificacao):

    grafico_ranking_classif_01 = alt.Chart(df_acidentes_geral_por_classificacao).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("classificacao_acidente:N", title='Classificação')
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das Classificações dos Acidentes (2007 a 2024)",
        width=800, height=600,
    )
    return grafico_ranking_classif_01
# ==========================================================================
def gera_grafico_ranking_classificacao_02(df_acidentes_geral_por_classificacao):

    grafico_ranking_classif_02 = alt.Chart(df_acidentes_geral_por_classificacao).mark_line(point=True).encode(
        x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
        y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
        color=alt.Color("classificacao_acidente:N", title='Classificação'),
        tooltip=['classificacao_acidente', 'qtd', 'ano']
    ).properties(
        title='Evolução da Quantidade de Acidentes por Classificação (2007-2024)',
        width=800, height=600
    ).add_selection(
        alt.selection_single(fields=['ano'], bind='legend')
    ).interactive()

    return grafico_ranking_classif_02
# ==========================================================================

# ==============================================================================
with tab03:

    titulo = f'<H2> Gráficos de Fluxo por UF / Tipo / BR / Causa / Classificação / Fase do Dia / Condição Metereológica / Dia da Semana / Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)
    
    tab5_sub1, tab5_sub2, tab5_sub3, tab5_sub4, tab5_sub5, tab5_sub6, tab5_sub7, tab5_sub8, tab5_sub9 = st.tabs(
        [
            "Fluxo por UF", "Fluxo por Tipo",
            "Fluxo por BR", "Fluxo por Causa",
            "Fluxo por Classificação", "Fluxo por Fase do Dia",
            "Fluxo por Condição Metereológica",
            "Fluxo por Dia da Semana",
            "Fluxo por Tipo de Veículo",
        ])   

    # Exibir o gráfico de fluxo
    if ano_selecionado != None:
        print(f'Entrou no Grafico de Fluxo')        
        with tab5_sub1:
            titulo='Fluxo de Acidentes por UF (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_uf(titulo, df_acidentes_geral_por_uf))
        with tab5_sub2:    
            titulo='Fluxo de Acidentes por Tipo (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_tipo(titulo, df_acidentes_geral_por_tipo))
        with tab5_sub3: 
            titulo='Fluxo Acidentes por BR (2007 a 2024)'           
            st.altair_chart(gera_graficos_fluxo_por_br(titulo, df_acidentes_geral_por_br))
        with tab5_sub4:    
            titulo='Fluxo Acidentes por Causa (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_causa(titulo, df_acidentes_geral_por_causa))
        with tab5_sub5:        
            titulo='Fluxo Acidentes por Classificação (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_classificacao(titulo, df_acidentes_geral_por_classificacao))
        with tab5_sub6:        
            titulo='Fluxo Acidentes por Fase do Dia (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_fasedia(titulo, df_acidentes_geral_por_fasedia))
        with tab5_sub7:        
            titulo='Fluxo Acidentes por Condição Metereológica (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_condicao_metereologica(titulo, df_acidentes_geral_por_condicao_metereologica))
        with tab5_sub8:        
            titulo='Fluxo Acidentes por Dia da Semana (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_dia_semana(titulo, df_acidentes_geral_por_dia_semana))
        with tab5_sub9:        
            titulo='Fluxo Acidentes por Tipo de Veículo (2007 a 2024)'
            st.altair_chart(gera_graficos_fluxo_por_tipo_veiculo(titulo, df_acidentes_geral_por_tipo_veiculo))

    elif exibir_filtro_periodo_anos and (ano_inicio is not None and ano_fim is not None):

      df_filtrado_uf = df_acidentes_geral_por_uf[
          (df_acidentes_geral_por_uf[COLUNA_ANO] >= int(ano_inicio)) & 
          (df_acidentes_geral_por_uf[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por UF entre {ano_inicio} e {ano_fim}'
      grafico_aba_01 = gera_graficos_fluxo_por_uf(titulo, df_filtrado_uf)

      df_filtrado_tipo = df_acidentes_geral_por_tipo[
          (df_acidentes_geral_por_tipo[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_tipo[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por Tipo entre {ano_inicio} e {ano_fim}'
      grafico_aba_02 = gera_graficos_fluxo_por_tipo(titulo, df_filtrado_tipo)

      df_filtrado_br = df_acidentes_geral_por_br[
          (df_acidentes_geral_por_br[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_br[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por BR entre {ano_inicio} e {ano_fim}'
      grafico_aba_03 = gera_graficos_fluxo_por_br(titulo, df_filtrado_br)

      df_filtrado_causa = df_acidentes_geral_por_causa[
          (df_acidentes_geral_por_causa[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_causa[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por Causa entre {ano_inicio} e {ano_fim}'
      grafico_aba_04 = gera_graficos_fluxo_por_causa(titulo, df_filtrado_causa)

      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] <= int(ano_fim)) 
      ]
      titulo=f'Fluxo de Acidentes por Classificação entre {ano_inicio} e {ano_fim}'
      grafico_aba_05 = gera_graficos_fluxo_por_classificacao(titulo, df_filtrado_classificacao)

      df_filtrado_fasedia = df_acidentes_geral_por_fasedia[
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] <= int(ano_fim))
      ] 
      titulo=f'Fluxo de Acidentes por Fase do Dia entre {ano_inicio} e {ano_fim}'
      grafico_aba_06 = gera_graficos_fluxo_por_fasedia(titulo, df_filtrado_fasedia)

      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicao_metereologica[
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por Condição Metereológica entre {ano_inicio} e {ano_fim}'
      grafico_aba_07 = gera_graficos_fluxo_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)

      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo=f'Fluxo de Acidentes por Dia da Semana entre {ano_inicio} e {ano_fim}'
      grafico_aba_08 = gera_graficos_fluxo_por_dia_semana(titulo, df_filtrado_dia_semana)

      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[
          (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] >= int(ano_inicio))  &
            (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] <= int(ano_fim))  
      ]
      titulo=f'Fluxo de Acidentes por Tipo de Veículo entre {ano_inicio} e {ano_fim}'
      grafico_aba_09 = gera_graficos_fluxo_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)

      # Exibir o gráfico de barras empilhadas
      with tab5_sub1:
            st.altair_chart(grafico_aba_01)
      with tab5_sub2:    
            st.altair_chart(grafico_aba_02)
      with tab5_sub3: 
            st.altair_chart(grafico_aba_03)
      with tab5_sub4:    
            st.altair_chart(grafico_aba_04)
      with tab5_sub5:        
            st.altair_chart(grafico_aba_05)
      with tab5_sub6:        
            st.altair_chart(grafico_aba_06)
      with tab5_sub7:        
            st.altair_chart(grafico_aba_07)
      with tab5_sub8:        
            st.altair_chart(grafico_aba_08)
      with tab5_sub9:        
            st.altair_chart(grafico_aba_09)

    # =====================================================================================

    
# ==============================================================================  
with tab06:
    
    titulo = f'<H2> Gráficos de Barras Empilhadas'
    st.markdown(titulo, unsafe_allow_html=True)    

    if ano_selecionado != OPCAO_TODOS and ano_selecionado != None:

      # por UF      
      df_filtrado_uf = df_acidentes_geral_por_uf[(df_acidentes_geral_por_uf[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por UF em {ano_selecionado}'
      grafico1 = grafico_barras_empilhadas_por_uf(titulo, df_filtrado_uf)        

      # por BR    
      df_filtrado_br = df_acidentes_geral_por_br[(df_acidentes_geral_por_br[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por BR em {ano_selecionado}'
      grafico2 = grafico_barras_empilhadas_por_br(titulo, df_filtrado_br)  

      # por Tipo 
      df_filtrado_tipo = df_acidentes_geral_por_tipo[(df_acidentes_geral_por_tipo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Tipo em {ano_selecionado}'
      grafico3 = grafico_barras_empilhadas_por_tipo(titulo, df_filtrado_tipo)  

      # por Causa 
      df_filtrado_causa = df_acidentes_geral_por_causa[(df_acidentes_geral_por_causa[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Causa de Acidente em {ano_selecionado}'
      grafico4 = grafico_barras_empilhadas_por_causa(titulo, df_filtrado_causa)  

      # por Classificacao
      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[(df_acidentes_geral_por_classificacao[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Classificação de Acidente em {ano_selecionado}'
      grafico5 = grafico_barras_empilhadas_por_classificacao(titulo, df_filtrado_classificacao)  

      # por Fase do Dia
      df_filtrado_fase_dia = df_acidentes_geral_por_fasedia[(df_acidentes_geral_por_fasedia[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Fase do Dia de Acidente em {ano_selecionado}'
      grafico6 = grafico_barras_empilhadas_por_fase_dia(titulo, df_filtrado_fase_dia)  

      # Condição Metereológica
      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicao_metereologica[(df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Condição Metereológica em {ano_selecionado}'
      grafico7 = grafico_barras_empilhadas_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)  

      # Dia da Semana
      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[(df_acidentes_geral_por_dia_semana[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Dia da Semana em {ano_selecionado}'
      grafico8 = grafico_barras_empilhadas_por_dia_semana(titulo, df_filtrado_dia_semana)  

      # Tipo de Veículo
      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[(df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Dia da Semana em {ano_selecionado}'
      grafico9 = grafico_barras_empilhadas_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)  
    
    elif ano_selecionado == OPCAO_TODOS:
      grafico1 = grafico_barras_empilhadas_por_uf('Barras Empilhadas por UF (2007 a 2024)', df_acidentes_geral_por_uf)            
      grafico2 = grafico_barras_empilhadas_por_br('Barras Empilhadas por BR (2007 a 2024)', df_acidentes_geral_por_br)  
      grafico3 = grafico_barras_empilhadas_por_tipo('Barras Empilhadas por Tipos de Acidentes (2007-2024)', df_acidentes_geral_por_tipo)    
      grafico4 = grafico_barras_empilhadas_por_causa('Barras Empilhadas por Causa de Acidentes (2007-2024)', df_acidentes_geral_por_causa)      
      grafico5 = grafico_barras_empilhadas_por_classificacao('Barras Empilhadas por Classificação de Acidentes (2007-2024)', df_acidentes_geral_por_classificacao)      
      grafico6 = grafico_barras_empilhadas_por_fase_dia('Barras Empilhadas por Fase do Dia de Acidentes (2007-2024)', df_acidentes_geral_por_fasedia)      
      grafico7 = grafico_barras_empilhadas_por_condicao_metereologica('Barras Empilhadas por Condição Metereológica de Acidentes (2007-2024)',                                                          df_acidentes_geral_por_condicao_metereologica)      
      grafico8 = grafico_barras_empilhadas_por_dia_semana('Barras Empilhadas por Dia da Semana de Acidentes (2007-2024)', df_acidentes_geral_por_dia_semana)      
      grafico9 = grafico_barras_empilhadas_por_tipo_veiculo('Barras Empilhadas por Tipo de Veículo (2007-2024)', df_acidentes_geral_por_tipo_veiculo)      

    if exibir_filtro_periodo_anos and (ano_inicio is not None and ano_fim is not None):

      # por UF      
      df_filtrado_uf = df_acidentes_geral_por_uf[
          (df_acidentes_geral_por_uf[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_uf[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por UF entre {ano_inicio} e {ano_fim}'
      grafico1 = grafico_barras_empilhadas_por_uf(titulo, df_filtrado_uf)        

      # por BR    
      df_filtrado_br = df_acidentes_geral_por_br[
          (df_acidentes_geral_por_br[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_br[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por BR entre {ano_inicio} e {ano_fim}'
      grafico2 = grafico_barras_empilhadas_por_br(titulo, df_filtrado_br)  

      # por Tipo 
      df_filtrado_tipo = df_acidentes_geral_por_tipo[
          (df_acidentes_geral_por_tipo[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_tipo[COLUNA_ANO] <= int(ano_fim))  
      ]
      titulo = f'Barras Empilhadas por Tipo entre {ano_inicio} e {ano_fim}'
      grafico3 = grafico_barras_empilhadas_por_tipo(titulo, df_filtrado_tipo)  

      # por Causa 
      df_filtrado_causa = df_acidentes_geral_por_causa[
          (df_acidentes_geral_por_causa[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_causa[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por Causa de Acidente entre {ano_inicio} e {ano_fim}'
      grafico4 = grafico_barras_empilhadas_por_causa(titulo, df_filtrado_causa)  

      # por Classificacao
      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_classificacao[COLUNA_ANO] <= int(ano_fim))
      ]    
      titulo = f'Barras Empilhadas por Classificação de Acidente entre {ano_inicio} e {ano_fim}'
      grafico5 = grafico_barras_empilhadas_por_classificacao(titulo, df_filtrado_classificacao)  

      # por Fase do Dia
      df_filtrado_fase_dia = df_acidentes_geral_por_fasedia[
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_fasedia[COLUNA_ANO] <= int(ano_fim))   
      ]
      titulo = f'Barras Empilhadas por Fase do Dia de Acidente entre {ano_inicio} e {ano_fim}'
      grafico6 = grafico_barras_empilhadas_por_fase_dia(titulo, df_filtrado_fase_dia)  

      # Condição Metereológica
      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicao_metereologica[
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_condicao_metereologica[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por Condição Metereológica entre {ano_inicio} e {ano_fim}'
      grafico7 = grafico_barras_empilhadas_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)  

      # Dia da Semana
      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_dia_semana[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por Dia da Semana entre {ano_inicio} e {ano_fim}'
      grafico8 = grafico_barras_empilhadas_por_dia_semana(titulo, df_filtrado_dia_semana)  

      # Tipo de Veículo
      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[
          (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] >= int(ano_inicio)) &
          (df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] <= int(ano_fim))
      ]
      titulo = f'Barras Empilhadas por Dia da Semana entre {ano_inicio} e {ano_fim}'
      grafico9 = grafico_barras_empilhadas_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)  


    tab6_sub1, tab6_sub2, tab6_sub3, tab6_sub4, tab6_sub5, tab6_sub6, tab6_sub7, tab6_sub8, tab6_sub9  = st.tabs(
        [
            "por UF", "por BR", 
            "por Tipo", "por Causa", 
            "por Classificação", 
            "por Fase do Dia", 
            "por Condição Metereológica", "por Dia da Semana",
            "por Tipo de Veículo",
        ]
    )

    with tab6_sub1:
        st.altair_chart(grafico1)                  
    with tab6_sub2:        
        st.altair_chart(grafico2)    
    with tab6_sub3:        
        st.altair_chart(grafico3)        
    with tab6_sub4:        
        st.altair_chart(grafico4)           
    with tab6_sub5:        
        st.altair_chart(grafico5)           
    with tab6_sub6:        
        st.altair_chart(grafico6)           
    with tab6_sub7:        
        st.altair_chart(grafico7)           
    with tab6_sub8:        
        st.altair_chart(grafico8) 
    with tab6_sub9:        
        st.altair_chart(grafico9)           

# ==============================================================================
with tab07:

    titulo = f'<H2> Distribuição de Acidentes por UF / por Tipo / por BR / por Classificação / por Causa / por Fase do Dia / por Condição Metereológica / por Dia da Semana / por Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)

    tab7_sub1, tab7_sub2, tab7_sub3, tab7_sub4, tab7_sub5, tab7_sub6, tab7_sub7, tab7_sub8, tab7_sub9  = st.tabs(
        [
            "por UF", "por Tipo", 
            "por BR", "por Classificação", 
            "por Causa", "por Fase do Dia", 
            "por Condição Metereológica", 
            'por Dia da Semana', 'por Tipo de Veículo'
        ]
    )

    with tab7_sub1:
        st.altair_chart(gera_graficos_distribuicao_por_uf(df_acidentes_geral_por_uf))
    with tab7_sub2:    
        st.altair_chart(gera_graficos_distribuicao_por_tipo(df_acidentes_geral_por_tipo))
    with tab7_sub3:    
        st.altair_chart(gera_graficos_distribuicao_por_br(df_acidentes_geral_por_br))
    with tab7_sub4:    
        st.altair_chart(gera_graficos_distribuicao_por_classificacao(df_acidentes_geral_por_classificacao))
    with tab7_sub5:        
        st.altair_chart(gera_graficos_distribuicao_por_causa(df_acidentes_geral_por_causa))
    with tab7_sub6:    
        st.altair_chart(gera_graficos_distribuicao_por_fasedia(df_acidentes_geral_por_fasedia))
    with tab7_sub7:    
        st.altair_chart(gera_graficos_distribuicao_por_condicao_metereologica(df_acidentes_geral_por_condicao_metereologica))
    with tab7_sub8:    
        st.altair_chart(gera_graficos_distribuicao_por_dia_semana(df_acidentes_geral_por_dia_semana))
    with tab7_sub9:    
        st.altair_chart(gera_graficos_distribuicao_por_tipo_veiculo(df_acidentes_geral_por_tipo_veiculo))
    
# ==============================================================================  
with tab09:    

    titulo = f'<H2> Mapa dos Acidentes'
    st.markdown(titulo, unsafe_allow_html=True)

    tab09_sub1, tab09_sub2, tab09_sub3, tab09_sub4  = st.tabs(
        [
            "Por Ano / Por Rodovia", 
            "Por Ano / Por Rodovia / Por UF", 
            "Mapa BRs do Brasil", "Mapa Top 10 Brs", 
        ]
    )

    lista_brs = [101, 116, 381,  40, 153, 163, 364, 376, 262, 230, 470, 316, 282, 70,  60,  20, 158, 369,  50]

    # ================================
    # Aba 09 - constantes
    # ================================

    escala_cores_mapa = [
        '#f0f9e8', '#bae4bc', '#7bccc4', '#43a2ca', '#0868ac'
    ]

    # ===========================
    # Funções
    # ===========================
    def retorna_cor_ponto(qtd_acidentes, min, max):

        dif = int((max-min) // 5)

        faixa1_min = min
        faixa1_max = min+dif

        faixa2_min = faixa1_max+1
        faixa2_max = faixa2_min+dif

        faixa3_min = faixa2_max+1
        faixa3_max = faixa3_min+dif

        faixa4_min = faixa3_max+1
        faixa4_max = faixa4_min+dif

        faixa5_min = faixa4_max+1
        faixa5_max = max

        cor_secionada = ''
        if faixa1_min <= qtd_acidentes <= faixa1_max:
            cor_secionada = escala_cores_mapa[0]
        elif faixa2_min <= qtd_acidentes <= faixa2_max:
            cor_secionada = escala_cores_mapa[1]
        elif faixa3_min <= qtd_acidentes <= faixa3_max:
            cor_secionada = escala_cores_mapa[2]
        elif faixa4_min <= qtd_acidentes <= faixa4_max:
            cor_secionada = escala_cores_mapa[3]
        elif faixa5_min <= qtd_acidentes <= faixa5_max:
            cor_secionada = escala_cores_mapa[4]

        return cor_secionada
    # ===========================
    def monta_legenda_dinamica(min, max):

        dif = int((max-min) // 5)

        faixa1_min = min
        faixa1_max = min+dif

        faixa2_min = faixa1_max+1
        faixa2_max = faixa2_min+dif

        faixa3_min = faixa2_max+1
        faixa3_max = faixa3_min+dif

        faixa4_min = faixa3_max+1
        faixa4_max = faixa4_min+dif

        faixa5_min = faixa4_max+1
        faixa5_max = max

        texto_legendas = [
            '<br><br>', 
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#f0f9e8;margin-right:5px;"></span> Entre {faixa1_min} e {faixa1_max} acidentes',
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#bae4bc;margin-right:5px;"></span> Entre {faixa2_min} e {faixa2_max} acidentes',
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#7bccc4;margin-right:5px;"></span> Entre {faixa3_min} e {faixa3_max} acidentes',
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#43a2ca;margin-right:5px;"></span> Entre {faixa4_min} e {faixa4_max} acidentes',
            f'<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#0868ac;margin-right:5px;"></span> Entre {faixa5_min} e {faixa5_max} acidentes',
        ]
        return texto_legendas
    # ===========================

    with tab09_sub1:


        left, middle, right = st.columns(3)
        
        # Filtro de ano
        mapa_ano_selecionado = left.selectbox(
            'Selecione o ano:', ('2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', OPCAO_TODOS), key='aba09_sub01_selecao_ano')
        print(f'Mapa - Ano Selecionado = {mapa_ano_selecionado}')

        if mapa_ano_selecionado == '2017':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2017.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2018':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2018.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2019':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2019.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2020':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2020.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2021':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2021.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2022':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2022.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2023':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2023.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2024':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2024.csv', sep=';', decimal='.')       
            
        mapa_br_selecionada = middle.selectbox('Selecione a rodovia:', (lista_brs), key='aba09_selecao_br')       
        
        # Exibir o quadro com as legendas
        titulo = f'<H2>Acidentes reportados na BR {mapa_br_selecionada} no ano de {mapa_ano_selecionado}'
        st.markdown(titulo, unsafe_allow_html=True)    

        df_coordenadas_filtrado = df_coordenadas[(df_coordenadas['br'] == int(mapa_br_selecionada))]     

        min = df_coordenadas_filtrado['acidentes'].min()
        max = df_coordenadas_filtrado['acidentes'].max()

        for index, row in df_coordenadas_filtrado.iterrows():
            qtd_acidentes = row['acidentes']
            cor = retorna_cor_ponto(qtd_acidentes, min, max)
            df_coordenadas_filtrado.at[index, 'cor'] = cor
            df_coordenadas_filtrado.at[index, 'tamanho'] = qtd_acidentes * 10

        # Criar duas colunas para colocar os componentes lado a lado
        col1, col2 = st.columns([8,2])
        
        # Adicionar o gráfico à primeira coluna
        with col1:

            st.map(df_coordenadas_filtrado,
                latitude='latitude',
                longitude='longitude',
                size='tamanho',
                color='cor',
                use_container_width=False)

        with col2:

            legendas = monta_legenda_dinamica(min, max)
            # Exibir o quadro com as legendas
            st.markdown('<br>'.join(legendas), unsafe_allow_html=True)     

    with tab09_sub2:

        # ===========================
        # Funções
        # ===========================
        def lista_ufs_por_br(br, df):
            df_filtrado = df[(df['br'] == int(br))]
            lista_ufs = df_filtrado['uf'].unique()

            return lista_ufs
        # ===========================

        left, middle, right = st.columns(3)
        
        # Filtro de ano
        mapa_ano_selecionado = left.selectbox(
            'Selecione o ano:', ('2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', OPCAO_TODOS), key='aba09_01_selecao_ano')
        print(f'Mapa - Ano Selecionado = {mapa_ano_selecionado}')

        if mapa_ano_selecionado == '2017':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2017.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2018':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2018.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2019':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2019.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2020':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2020.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2021':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2021.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2022':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2022.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2023':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2023.csv', sep=';', decimal='.')   
        elif mapa_ano_selecionado == '2024':
            df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2024.csv', sep=';', decimal='.')       
            
        mapa_br_selecionada = middle.selectbox('Selecione a rodovia:', (lista_brs), index=0, key='aba09_sub01_selecao_br')       

        df_coordenadas_filtrado = df_coordenadas[(df_coordenadas['br'] == int(mapa_br_selecionada))]       
        lista_ufs_br = lista_ufs_por_br(mapa_br_selecionada, df_coordenadas_filtrado)
        mapa_uf_selecionada = right.selectbox('Selecione a UF:', (lista_ufs_br), index=0, key='aba09_sub01_selecao_uf')

        # Exibir o quadro com as legendas
        titulo = f'<H2>Acidentes reportados na BR {mapa_br_selecionada}, na UF {mapa_uf_selecionada}, no ano de {mapa_ano_selecionado}'
        st.markdown(titulo, unsafe_allow_html=True)    

        df_br_uf = df_coordenadas_filtrado[(df_coordenadas_filtrado['br'] == int(mapa_br_selecionada)) & (df_coordenadas_filtrado['uf'] == mapa_uf_selecionada)]

        min = df_br_uf['acidentes'].min()
        max = df_br_uf['acidentes'].max()

        for index, row in df_br_uf.iterrows():

            qtd_acidentes = row['acidentes']
            cor = retorna_cor_ponto(qtd_acidentes, min, max)
            df_br_uf.at[index, 'cor'] = cor
            df_br_uf.at[index, 'tamanho'] = qtd_acidentes * 10

        # Criar duas colunas para colocar os componentes lado a lado
        col1, col2 = st.columns([8,2])
        
        # Adicionar o gráfico à primeira coluna
        with col1:

            st.map(df_br_uf,
                latitude='latitude',
                longitude='longitude',
                size='tamanho',
                color='cor',
                use_container_width=False)

        with col2:

            min = df_br_uf['acidentes'].min()
            max = df_br_uf['acidentes'].max()
            legendas = monta_legenda_dinamica(min, max)

            # Exibir o quadro com as legendas
            st.markdown('<br>'.join(legendas), unsafe_allow_html=True)     

    with tab09_sub3:

        # Título da aplicação
        st.title("Mapa das BRs do Brasil")

        # Caminho da imagem
        image_path = "mapas/mapa_rodovias_federais.png"
        image = Image.open(image_path)
        st.image(image, caption='Mapa das BRs do Brasil', use_container_width=True)

    with tab09_sub4:

        image_path = 'mapas/mapa_brasil_brs_10.png'
        image = Image.open(image_path)
        st.image(image, caption='Mapa das BRs do Brasil', use_container_width=True)

# ==============================================================================  
with tab04:

    titulo = f'<H2> Mapa de Calor por UF / por Tipo / por BR / por Classificação / por Causa / por Fase do Dia / por Condição Metereológica / por Dia da Semana / por Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)

    tab4_sub1, tab4_sub2, tab4_sub3, tab4_sub4, tab4_sub5, tab4_sub6, tab4_sub7, tab4_sub8, tab4_sub9  = st.tabs(
        [
            "por UF", "por Tipo", 
            "por BR", "por Classificação", 
            "por Causa", "por Fase do Dia", 
            "por Condição Metereológica", 
            'por Dia da Semana', 'por Tipo de Veículo'
        ]
    )    

    with tab4_sub1:
        st.altair_chart(gera_graficos_mapa_calor_por_uf(df_acidentes_geral_por_uf))
    with tab4_sub2:        
        st.altair_chart(gera_graficos_mapa_calor_por_tipo(df_acidentes_geral_por_tipo))
    with tab4_sub3:        
        st.altair_chart(gera_graficos_mapa_calor_por_br(df_acidentes_geral_por_br))    
    with tab4_sub4:        
        st.altair_chart(gera_graficos_mapa_calor_por_classificacao(df_acidentes_geral_por_classificacao))
    with tab4_sub5:        
        st.altair_chart(gera_graficos_mapa_calor_por_causa(df_acidentes_geral_por_causa))
    with tab4_sub6:        
        st.altair_chart(gera_graficos_mapa_calor_por_fasedia(df_acidentes_geral_por_fasedia))
    with tab4_sub7:        
        st.altair_chart(gera_graficos_mapa_calor_por_condicao_metereologica(df_acidentes_geral_por_condicao_metereologica))
    with tab4_sub8:        
        st.altair_chart(gera_graficos_mapa_calor_por_dia_semana(df_acidentes_geral_por_dia_semana))
    with tab4_sub9:        
        st.altair_chart(gera_graficos_mapa_calor_por_tipo_veiculo(df_acidentes_geral_por_tipo_veiculo))                               

# ==============================================================================      
