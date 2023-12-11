# gantt_chart.py
import streamlit as st
import pandas as pd
from plotly import express as px
import random

# Exemplo de código para exibir no Streamlit
st.subheader("Instale as bibliotecas necessárias:")
st.code("pip install streamlit plotly")

st.subheader("Comandos Utilizados")
st.code('''# Função para gerar dados randômicos
def generate_random_data():
    data = []
    for task in range(1, 6):
        start_date = pd.to_datetime(f"2023-01-01") + pd.to_timedelta(random.randint(1, 30), unit='D')
        end_date = start_date + pd.to_timedelta(random.randint(5, 15), unit='D')
        data.append({
            'Task': f'Task {task}',
            'Start': start_date,
            'Finish': end_date
        })
    return data

# Criar dados randômicos
gantt_data = pd.DataFrame(generate_random_data())

# Criar gráfico de Gantt
fig = px.timeline(gantt_data, x_start='Start', x_end='Finish', y='Task', title='Gráfico de Gantt com Valores Randômicos')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)''')
# Função para gerar dados randômicos
def generate_random_data():
    data = []
    for task in range(1, 6):
        start_date = pd.to_datetime(f"2023-01-01") + pd.to_timedelta(random.randint(1, 30), unit='D')
        end_date = start_date + pd.to_timedelta(random.randint(5, 15), unit='D')
        data.append({
            'Task': f'Task {task}',
            'Start': start_date,
            'Finish': end_date
        })
    return data

# Criar dados randômicos
gantt_data = pd.DataFrame(generate_random_data())

# Criar gráfico de Gantt
fig = px.timeline(gantt_data, x_start='Start', x_end='Finish', y='Task', title='Gráfico de Gantt com Valores Randômicos')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
