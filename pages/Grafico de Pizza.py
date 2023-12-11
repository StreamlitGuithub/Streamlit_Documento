# gantt_chart.py
import streamlit as st
import pandas as pd
from plotly import express as px
import random

# Exemplo de código para exibir no Streamlit
st.subheader("Instale as bibliotecas necessárias:")
st.code("pip install streamlit plotly")

st.subheader("Comandos Utilizados")
st.code('''# pie_chart.py
import streamlit as st
from plotly import express as px

# Dados de exemplo para o gráfico de pizza
data = {'Categorias': ['Categoria A', 'Categoria B', 'Categoria C'],
        'Valores': [25, 40, 35]}

df = px.data.tips()

# Criar gráfico de pizza
fig = px.pie(data, names='Categorias', values='Valores', title='Gráfico de Pizza')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
''')

# pie_chart.py
import streamlit as st
from plotly import express as px

# Dados de exemplo para o gráfico de pizza
data = {'Categorias': ['Categoria A', 'Categoria B', 'Categoria C'],
        'Valores': [25, 40, 35]}

df = px.data.tips()

# Criar gráfico de pizza
fig = px.pie(data, names='Categorias', values='Valores', title='Gráfico de Pizza')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
