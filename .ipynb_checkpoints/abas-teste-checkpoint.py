import streamlit as st

st.title("Meu Aplicativo com Abas e Subabas")

# Criando as abas
tab1, tab2 = st.tabs(["Aba 1", "Aba 2"])

# Conteúdo da Aba 1 com subabas
with tab1:
    tab1_sub1, tab1_sub2, tab1_sub3, tab1_sub4 = st.tabs(["Ranking A", "Ranking B", "Ranking C", "Ranking D"])
    with tab1_sub1:
        st.write("Conteúdo do Ranking A\nConteúdo do Ranking A\nConteúdo do Ranking A")
    with tab1_sub2:
        st.write("Conteúdo do Ranking B\nConteúdo do Ranking B\nConteúdo do Ranking B")
    with tab1_sub3:
        st.write("Conteúdo do Ranking C\nConteúdo do Ranking C\nConteúdo do Ranking C")
    with tab1_sub4:
        st.write("Conteúdo do Ranking D\nConteúdo do Ranking D\nConteúdo do Ranking D")

# Conteúdo da Aba 2
with tab2:
    st.write("Conteúdo da Aba 2")