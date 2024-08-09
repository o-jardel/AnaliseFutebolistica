import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Carregar dados
dados = pd.read_csv('brasileirao_serie_a.csv')

dados.describe()

dados_treino, dados_val = train_test_split(dados, test_size=0.3, random_state=42, shuffle=True)

sns.set()



st.title("Análise futeboslistica, idade ganha jogo?")
st.subheader("Dados do brasileirão entre os anos de 2003 e 2023")
st.text(" ")
st.markdown("Realizei esta análise para identificar qual é a média de idade ideal para um time de futebol marcar mais gols, e por consequência, ganhar mais jogos.")
st.markdown("Aqui neste dashboard, exibimos os gráficos de relação entre gols marcados e a média de idade de jogos que ocorreram no futebol brasileiro.")
st.markdown("Para saber mais sobre nossa pesquisa, clique no link a seguir para acessar nosso material com mais dados sobre o projeto: https://drive.google.com/file/d/10s9gvnuWKkdBHc7U-UlPV4vmN_UFIc24/view?usp=sharing")


#aparece as colunas
#dados_treino.columns

#tratamento de dados

dados_treino = dados_treino[dados_treino.idade_media_titular_mandante  <40]
dados_treino = dados_treino[dados_treino.idade_media_titular_visitante  <40]
dados_treino = dados_treino[dados_treino.faltas_mandante  <50]
dados_treino = dados_treino[dados_treino.faltas_visitante  <50]



#primeiro botão
if st.button("Gerar Gráfico de relação entre média de idade e gols marcados por times mandantes"):
    plt.figure(figsize=(8,8))
    sns.regplot(dados_treino, y='idade_media_titular_mandante', x='gols_mandante')
    #plt.scatter('idade_media_titular_mandante', 'gols_mandante')
    plt.xlabel('Gols Mandante')
    plt.ylabel('Idade Média Titular Mandante')
    st.pyplot()
if st.button("Gerar Gráfico de relação entre média de idade e gols marcados por times visitantes"):
    plt.figure(figsize=(8,8))
    sns.regplot(dados_treino, y='idade_media_titular_visitante', x='gols_visitante')
    plt.xlabel('Gols Visitante')
    plt.ylabel('Idade Média Titular Visitante')
    st.pyplot()


st.text("Jardel Ferreira - GRR20231834")

