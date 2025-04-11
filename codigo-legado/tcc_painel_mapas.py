# =======================================================
# Imports
# =======================================================
import altair as alt
import random
import streamlit as st

alt.data_transformers.enable("vegafusion")

@st.cache_data
def plotar_brs(lista_brs):

    #import pandas as pd
    import geopandas as gpd
    import altair as alt
    from altair_saver import save
    #import altair_viewer
    import json

    # Carregando os dados do arquivo JSON
    with open('br_states.json') as f:
        geojson = json.load(f)
        
    # Convertendo para um GeoDataFrame
    gdf = gpd.GeoDataFrame.from_features(geojson['features'])

    # Criando o mapa
    chart1 = alt.Chart(gdf).mark_geoshape(
        filled=True,
        stroke='black'
    ).properties(
        width=1024,
        height=768,
        title='Mapa das BRs do Brasil'
    ).project(
        type='mercator'  # Altere para a projeção desejada
    )

    # Carregar o arquivo SHP
    df_info = gpd.read_file('coordenadas-rodovias/SNV_202404A.dbf')
    #https://github.com/Bergolito/tcc-painel-jupyter-notebook/blob/main/202404A/SNV_202404A.dbf
    #df_info = gpd.read_file('https://github.com/Bergolito/tcc-painel-jupyter-notebook/blob/main/202404A/SNV_202404A.dbf')

    grafs = []

    for item in lista_brs:
        df_info_filtrado_br = df_info[(df_info['ds_jurisdi'] == 'Federal') & (df_info['vl_br'] == str(item))]

        df_info_filtrado_br_geometry = df_info_filtrado_br[['geometry','vl_br']]
        serie_br_geometry = df_info_filtrado_br['geometry'].simplify(tolerance=0.01)
        df_info_filtrado_br_geometry['geometry'] = serie_br_geometry
        df_info_filtrado_br_geometry['br'] = 'BR-'+str(item)
        grafico = gera_grafico_uma_br(df_info_filtrado_br_geometry)
        grafs.append(grafico)

    print(f'lista_graficos = {len(grafs)}')

    juntos = chart1
    if len(grafs) == 1:
        juntos = chart1 + grafs[0] 
    elif len(grafs) == 2:
        juntos = chart1 + grafs[0] + grafs[1] 
    elif len(grafs) == 3:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] 
    elif len(grafs) == 4:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] 
    elif len(grafs) == 5:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] 
    elif len(grafs) == 6:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] + grafs[5] 
    elif len(grafs) == 7:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] + grafs[5] + grafs[6] 
    elif len(grafs) == 8:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] + grafs[5] + grafs[6] + grafs[7]  
    elif len(grafs) == 9:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] + grafs[5] + grafs[6] + grafs[7] + grafs[8] 
    elif len(grafs) == 10:
        juntos = chart1 + grafs[0] + grafs[1] + grafs[2] + grafs[3] + grafs[4] + grafs[5] + grafs[6] + grafs[7] + grafs[8] + grafs[9]

    juntos.save('mapas/brs_concatenadas_teste.png')

    return juntos

# ==================================================
def gera_grafico_uma_br(df_geometry_br):

    cores = [
        'black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green', 'lime', 'olive', 'yellow', 
        'navy', 'blue', 'teal', 'aqua', 'orange', 'aliceblue', 'antiquewhite', 'aquamarine', 'azure', 'beige', 'bisque',
        'blanchedalmond', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 
        'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 
        'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 
        'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 
        'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'greenyellow', 'grey', 
        'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 
        'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 
        'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 
        'limegreen', 'linen', 'magenta', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 
        'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 
        'moccasin', 'navajowhite', 'oldlace', 'olivedrab', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 
        'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'rosybrown', 'royalblue', 'saddlebrown', 
        'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 
        'steelblue', 'tan', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'whitesmoke', 'yellowgreen', 'rebeccapurple'
    ]    

    indice = random.randint(0, len(cores)-1 )
    cor_selecionada = cores[indice]

    chart = alt.Chart(df_geometry_br).mark_geoshape(
        filled=True,
        strokeWidth=2.0,
        stroke=cor_selecionada,
    ).properties(
        width=1024,
        height=768,
    ).encode(
        color='br:N',
        tooltip=['br:N']
    ).project(
        type='mercator'  # Altere para a projeção desejada
    )

    return chart
# ==================================================

#Layout da página
st.set_page_config(
    page_title="Título da Página",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon = "🗳️"
)
alt.themes.enable("dark")


#lista_brs = ['101', '116', '381', '040', '153', '163', '364', '376', '262', '230', '470', '316', '282', '070', '060', '020', '158', '369', '050']
lista_brs = ['101']
grafico = plotar_brs(lista_brs)

st.title("Mapa do Brasil")

st.altair_chart(grafico, use_container_width=True)
