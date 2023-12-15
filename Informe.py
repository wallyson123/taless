import streamlit as st
import pandas as pd

# Link para o conjunto de dados no Kaggle
dataset_link = "https://www.kaggle.com/datasets/dillonmyrick/high-school-student-performance-and-demographics"

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

# Sidebar filters
st.sidebar.header("Filtros")
selected_school = st.sidebar.selectbox("Selecione uma Escola:", df_student_performance['school'].unique())
selected_age = st.sidebar.slider("Selecione uma Idade:", int(df_student_performance['age'].min()), int(df_student_performance['age'].max()))

# Apply filters
filtered_data = df_student_performance[
    (df_student_performance['school'] == selected_school) &
    (df_student_performance['age'] == selected_age)
]

# General information
total_tables = 1
total_columns = df_student_performance.shape[1]
total_students = df_student_performance.shape[0]

st.subheader("Informações Gerais")
st.write(f"Total de tabelas: {total_tables}")
st.write(f"Total de colunas na tabela: {total_columns}")
st.write(f"Total de alunos: {total_students}")

# Dados Completos de Desempenho dos Alunos
st.header("Dados Completos de Desempenho dos Alunos")
st.write(filtered_data)

# Análise por Séries
st.header("Análise por Séries")
df_serie_selecionada = filtered_data[filtered_data['school'] == selected_school]
st.subheader(f"Informações sobre a Série {selected_school}")
st.write(df_serie_selecionada)

# Importância da Educação
st.header("Importância da Educação:")
st.write(
    "A educação é uma ferramenta crucial para o desenvolvimento humano. "
    "O desempenho dos alunos reflete não apenas o aprendizado individual, mas também o sistema educacional como um todo. "
    "Investir na educação é investir no futuro, proporcionando oportunidades para o crescimento pessoal e profissional."
)

# Link para o Kaggle
st.subheader("Conjunto de Dados no Kaggle:")
st.write(f"O conjunto de dados foi obtido no Kaggle. Você pode acessá-lo [aqui]({dataset_link}).")