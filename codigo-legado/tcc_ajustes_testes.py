
import pandas as pd

df_br_20 = pd.read_csv('datasets/gerais/acidentes_geral_por_br_20.csv')
lista_brs = df_br_20['br'].unique()
print(len(lista_brs))

df_br_30 = pd.read_csv('datasets/gerais/acidentes_geral_por_br_30.csv')
lista_brs = df_br_30['br'].unique()
print(len(lista_brs))
