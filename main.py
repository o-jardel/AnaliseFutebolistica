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



st.title("Análise futeboslistica, mando de campo ganha jogo?")
st.subheader("Dados do brasileirão entre os anos de 2003 e 2023")
st.text(" ")
st.markdown("Realizei esta análise para identificar qual é a relação entre resultado das partidas e time mandante.")
st.markdown("Aqui neste dashboard, exibimos os gráficos de relação entre essas grandezas para comprovarmos que esta relação é sim, bem presente.")
st.markdown("Para saber mais sobre nossa pesquisa, clique no link a seguir para acessar nosso material com mais dados sobre o projeto: https://drive.google.com/file/d/10s9gvnuWKkdBHc7U-UlPV4vmN_UFIc24/view?usp=sharing")


#aparece as colunas
#dados_treino.columns

#tratamento de dados

dados_treino = dados_treino[dados_treino.idade_media_titular_mandante  <40]
dados_treino = dados_treino[dados_treino.idade_media_titular_visitante  <40]
dados_treino = dados_treino[dados_treino.faltas_mandante  <50]
dados_treino = dados_treino[dados_treino.faltas_visitante  <50]

#criar variável resultado
dados_treino['resultado'] = dados_treino.apply(
    lambda row: 1 if row['gols_mandante'] > row['gols_visitante']
                else (-1 if row['gols_mandante'] < row['gols_visitante']
                      else 0), axis=1)


#primeiro botão
if st.button("Gerar gráfico de resultados dos times mandantes"):

    # Contagem de resultados para times mandantes
    contagem_mandante = dados_treino.groupby('time_mandante')['resultado'].value_counts().unstack().fillna(0)
    print("Contagem de Resultados para Times Mandantes:")
    print(contagem_mandante)



    taxa_mandante = contagem_mandante.div(contagem_mandante.sum(axis=1), axis=0)
    print("Taxa de Resultados para Times Mandantes:")
    print(taxa_mandante)


    plt.figure(figsize=(12, 8))
    sns.heatmap(contagem_mandante, annot=True, cmap="Blues", fmt=".0f")
    plt.title("Frequência de Resultados para Times Mandantes")
    plt.xlabel("Resultado")
    plt.ylabel("Time Mandante")
    plt.show()
    st.pyplot()



    from scipy.stats import chi2_contingency

    tabela_contingencia_mandante = pd.crosstab(dados_treino['time_mandante'], dados_treino['resultado'])

    chi2_mandante, p_mandante, _, _ = chi2_contingency(tabela_contingencia_mandante)
    #print(f"Teste Qui-Quadrado para Time Mandante: Chi2 = {chi2_mandante:.2f}, p-valor = {p_mandante:.4f}")



    # Supondo que a tabela de contingência já esteja criada como tabela_contingencia_mandante
    # Se ainda não tiver, você pode criar assim:
    # tabela_contingencia_mandante = pd.crosstab(dados_treino['time_mandante'], dados_treino['resultado'])

    # Plotando o gráfico de barras empilhadas
    tabela_contingencia_mandante.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')

    # Títulos e rótulos
    plt.title('Distribuição dos Resultados por Time Mandante')
    plt.xlabel('Time Mandante')
    plt.ylabel('Número de Partidas')

    # Alterando a legenda para refletir os valores de -1, 0, 1
    plt.legend(title='Resultado', labels=['Derrota do Time Mandante', 'Empate', 'Vitória do Time Mandante'], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=90)  # Rotaciona os nomes dos times no eixo x para melhor leitura
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()
    st.pyplot()















st.text("Jardel Ferreira - GRR20231834")

