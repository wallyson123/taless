import streamlit as st
import pandas as pd

# Link para o conjunto de dados no Kaggle
dataset_link = "https://www.kaggle.com/datasets/everydaycodings/student-performance-dataset/"

df_student_performance = pd.read_csv('student_math_clean.csv')

st.title("Análise de Desempenho dos Alunos")
st.write(
    "Esta análise utiliza dados sobre o desempenho dos alunos. "
    "Os dados contêm informações sobre o ID do aluno, escola, sexo, idade, tipo de endereço, tamanho da família, "
    "estado dos pais, educação da mãe, educação do pai, ocupação da mãe, ocupação do pai, motivo de escolha da escola, "
    "guardião, tempo de viagem, tempo de estudo, falhas nas notas, apoio da escola, apoio da família, aulas extras pagas, "
    "atividades extracurriculares, frequência à creche, aspiração para ensino superior, acesso à internet, relacionamento romântico, "
    "relacionamento familiar, tempo livre, interação social, consumo de álcool durante a semana, consumo de álcool no fim de semana, "
    "saúde, faltas, nota no primeiro período, nota no segundo período, nota final."
)

total_tables = 1
total_columns = df_student_performance.shape[1]
total_students = df_student_performance.shape[0]

st.subheader("Informações Gerais")
st.write(f"Total de tabelas: {total_tables}")
st.write(f"Total de colunas na tabela: {total_columns}")
st.write(f"Total de alunos: {total_students}")

st.header("Dados Completos de Desempenho dos Alunos")
st.write(df_student_performance)

# Separando por séries
st.header("Análise por Séries")
series = df_student_performance['school'].unique()
serie_selecionada = st.selectbox("Selecione uma série:", series)

df_serie_selecionada = df_student_performance[df_student_performance['school'] == serie_selecionada]

st.subheader(f"Informações sobre a Série {serie_selecionada}")
st.write(df_serie_selecionada)

# Adicionando um pouco sobre a importância da educação
st.header("Importância da Educação:")
st.write(
    "A educação é uma ferramenta crucial para o desenvolvimento humano. "
    "O desempenho dos alunos reflete não apenas o aprendizado individual, mas também o sistema educacional como um todo. "
    "Investir na educação é investir no futuro, proporcionando oportunidades para o crescimento pessoal e profissional."
)

# Adicionando link para o Kaggle
st.subheader("Conjunto de Dados no Kaggle:")
st.write(f"O conjunto de dados foi obtido no Kaggle. Você pode acessá-lo [aqui]({dataset_link}).")