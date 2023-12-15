import pandas as pd
import streamlit as st
import plotly.express as px

# Load data from CSV
file_path = "student_math_clean.csv"  # Replace with the actual file path
try:
    df_student_math = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"File not found: {file_path}")
    st.stop()

# Display the data
st.title("Student Performance Analysis")
st.subheader("Preview of the Data:")
st.write(df_student_math.head())

# Filter by Age
selected_age = st.slider("Select Age:", min_value=int(df_student_math['age'].min()), max_value=int(df_student_math['age'].max()))
filtered_data_by_age = df_student_math[df_student_math['age'] == selected_age]

# Display filtered data
st.subheader(f"Data for Students with Age {selected_age}:")
st.write(filtered_data_by_age)

# Average ages by school
average_age_by_school = df_student_math.groupby('school')['age'].mean()
st.subheader("Average Ages by School:")
st.bar_chart(average_age_by_school)

# Average final grades by different groups
groups_to_analyze = ['parent_status', 'address_type', 'family_size', 'study_time']

for group in groups_to_analyze:
    average_final_grade_by_group = filtered_data_by_age.groupby(group)['final_grade'].mean()
    st.subheader(f"Average Final Grade by {group} for Age {selected_age}:")
    st.bar_chart(average_final_grade_by_group)

# Scatter plot
st.subheader("Scatter Plot: Health vs. Social with Bubble Size as Final Grade for Age {selected_age}")
scatter_plot_fig = px.scatter(
    filtered_data_by_age,
    x='health',
    y='social',
    size='final_grade',
    color='free_time',
    title=f'Health vs. Social with Bubble Size as Final Grade for Age {selected_age}'
)
st.plotly_chart(scatter_plot_fig)

# Summary statistics
st.subheader(f"Summary Statistics for Age {selected_age}:")
selected_columns = st.multiselect("Select Columns for Summary Statistics:", filtered_data_by_age.columns)
if selected_columns:
    st.write(filtered_data_by_age[selected_columns].describe())
else:
    st.warning("Please select at least one column for summary statistics.")