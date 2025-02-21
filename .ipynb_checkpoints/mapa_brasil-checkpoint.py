import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json

#Layout da página
st.set_page_config(
    page_title="Título da Página",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon = "🗳️"
)
alt.themes.enable("dark")

##########################################################################################
##                                     Funções úteis                                    ##
##########################################################################################
#Baixa os arquivos do drive e converte em dataframe
def get_df(url):
    url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    return pd.read_csv(url, sep=",")

@st.cache_data
def get_estados():    
    #df_estados= get_df("https://drive.google.com/file/d/1qPMUuto04pQVnxaayg7Ubs9ZlxfiDwcX/view?usp=sharing")
    df_estados= pd.read_csv("mapa_brasil/estados.csv", sep=",")
    df_estados.rename(columns={"nome":"NM_UF"}, inplace=True)
    return df_estados

@st.cache_data    
def get_municipios_ibge():
    #df_municipios_ibge = get_df("https://drive.google.com/file/d/1gcbOM3S0un4xTUxgXxp0be1MzyFHWRoi/view?usp=sharing")
    df_municipios_ibge = pd.read_csv("mapa_brasil/municipios_ibge_lat_long.csv", sep=",")
    return df_municipios_ibge

@st.cache_data    
def get_municipios_tse():
    #df_municipios_tse = get_df("https://drive.google.com/file/d/1NJvtXR9BBMSi-Y5511RS5nObbgLQdsSm/view?usp=sharing")
    df_municipios_tse = pd.read_csv("mapa_brasil/municipios_brasileiros_tse.csv", sep=",")
    return df_municipios_tse
##########################################################################################
##                               Carga de dados regionais                               ##
##########################################################################################
#Estados brasileiros
df_estados = get_estados()

#Municípios código tse
df_municipios_tse = get_municipios_tse()

#municípios do ibge
df_municipios_ibge = get_municipios_ibge()
df_municipios = pd.merge(df_municipios_tse, df_municipios_ibge, on=['codigo_ibge'], how="inner")
df_municipios = df_municipios[['codigo_tse','nome_municipio','uf','capital_x','latitude','longitude']]

#apenas as capitais 
df_capitais= pd.merge(
    df_municipios_tse, 
    df_municipios_ibge[df_municipios_ibge['capital'] == 1], 
    on=['codigo_ibge'], 
    how="inner")[['uf','codigo_tse','nome_municipio','latitude','longitude']]


@st.cache_data
def plot_br_map(title="Título do Mapa"):
    map = alt.Chart(alt.Data(
            url="https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/main/geojson/br_states.json",
            format=alt.DataFormat(property='features')
        )) \
    .mark_geoshape(
        # 
        #stroke='#fff', strokeWidth=1.5
        stroke='#bdb15b', strokeWidth=1.5
    ).project(
        type="equirectangular"  
    ).properties(
        title="Mapa do Brasil",
        width=1024,
        height=768
    )
    
    text_est = alt.Chart(df_capitais) \
        .mark_text(
            dx=alt.expr(
                alt.expr.if_(
                    alt.datum.uf == 'PA', -50, 
                        alt.expr.if_(alt.datum.uf == 'RO',10,
                            alt.expr.if_(alt.datum.uf == 'AC',-40,
                                alt.expr.if_(alt.datum.uf == 'AM',-60,
                                    alt.expr.if_(alt.datum.uf == 'RR',-5,                                            
                                        alt.expr.if_(alt.datum.uf == 'AP',-10,
                                            alt.expr.if_(alt.datum.uf == 'MT',0,
                                                alt.expr.if_(alt.datum.uf == 'MA',-10,
                                                    alt.expr.if_(alt.datum.uf == 'PI',8,
                                                        alt.expr.if_(alt.datum.uf == 'CE',-12,
                                                            alt.expr.if_(alt.datum.uf == 'RN',-20,
                                                                alt.expr.if_(alt.datum.uf == 'PB',-30,
                                                                    alt.expr.if_(alt.datum.uf == 'PE',-40,
                                                                        alt.expr.if_(alt.datum.uf == 'AL',14,
                                                                            alt.expr.if_(alt.datum.uf == 'SE',15,
                                                                                alt.expr.if_(alt.datum.uf == 'BA',-40,
                                                                                    alt.expr.if_(alt.datum.uf == 'TO',0,
                                                                                        alt.expr.if_(alt.datum.uf == 'GO',-15,
                                                                                            alt.expr.if_(alt.datum.uf == 'DF',5,
                                                                                                alt.expr.if_(alt.datum.uf == 'RJ',10,
                                                                                                    alt.expr.if_(alt.datum.uf == 'SP',-25,
                                                                                                        alt.expr.if_(alt.datum.uf == 'PR',-25,
                                                                                                            alt.expr.if_(alt.datum.uf == 'SC',-25,
                                                                                                                alt.expr.if_(alt.datum.uf == 'RS',-20,-5)
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ), 
            dy=alt.expr(
                alt.expr.if_(alt.datum.uf == 'PA', 50, 
                    alt.expr.if_(alt.datum.uf == 'RO',30,
                        alt.expr.if_(alt.datum.uf == 'AC',-15,
                            alt.expr.if_(alt.datum.uf == 'AM',10,
                                alt.expr.if_(alt.datum.uf == 'RR',20,
                                    alt.expr.if_(alt.datum.uf == 'AP',-15,
                                        alt.expr.if_(alt.datum.uf == 'MT',-30,
                                            alt.expr.if_(alt.datum.uf == 'MA',30,
                                                alt.expr.if_(alt.datum.uf == 'PI',30,
                                                    alt.expr.if_(alt.datum.uf == 'CE',20,
                                                        alt.expr.if_(alt.datum.uf == 'RN',-2,
                                                            alt.expr.if_(alt.datum.uf == 'PB',0,
                                                                alt.expr.if_(alt.datum.uf == 'PE',5,
                                                                    alt.expr.if_(alt.datum.uf == 'AL',0,
                                                                        alt.expr.if_(alt.datum.uf == 'SE',2,
                                                                            alt.expr.if_(alt.datum.uf == 'BA',0,
                                                                                alt.expr.if_(alt.datum.uf == 'TO',-10,
                                                                                    alt.expr.if_(alt.datum.uf == 'GO',-10,
                                                                                        alt.expr.if_(alt.datum.uf == 'DF',-10,
                                                                                            alt.expr.if_(alt.datum.uf == 'SC',-5,
                                                                                                alt.expr.if_(alt.datum.uf == 'RS',-10,
                                                                                                    alt.expr.if_(alt.datum.uf == 'MS',-17,-5)
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )            
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ), 
            fontSize=12
        ) \
        .encode(
            latitude="latitude:Q",
            longitude="longitude:Q",
            text="uf:N"
        )
    
    text_munic = alt.Chart(df_capitais) \
        .mark_text(dx=-6, dy=8, fontSize=7) \
        .encode(
            latitude="latitude:Q",
            longitude="longitude:Q",
            text="nome_municipio:N"
        )
    
    point = alt.Chart(df_capitais) \
        .mark_circle(dx=-5, size=25) \
        .encode(        
            latitude="latitude:Q",
            longitude="longitude:Q",
            color=alt.value("orange"),
        )

    return (map + text_est + text_munic + point).configure_title(fontSize=15)
    #return (map2 + text_est + text_munic + point).configure_title(fontSize=15)

##########################################################################################
##                                       Layout                                         ##
##########################################################################################
st.title("Mapa do Brasil")

topo = st.columns(1)
with topo[0]:
    st.altair_chart(plot_br_map(title="Mapa do Brasil"), use_container_width=True)
