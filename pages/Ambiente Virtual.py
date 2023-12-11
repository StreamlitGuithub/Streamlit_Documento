import streamlit as st

st.title("Crie um ambiente virtual:")
st.subheader("Abra um terminal no VSCode e crie um ambiente virtual para o seu projeto. Execute os seguintes comandos:")
st.subheader("Criando seu ambiente Virtual!")
st.code("pip install virtualenv")
st.code("python3 -m venv venv source venv/bin/activate")


st.subheader("Comando para rodar a aplicação no Terminal do VSCode")
st.code('''streamlit run nome_do_app.py''')