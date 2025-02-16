import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv ()

import streamlit as st
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key no encontrada. Configúrala en Streamlit Secrets o en un archivo .env.")
else:
    st.success("✅ API Key cargada correctamente")




def load_css():
    try:
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass
load_css()

st.title("Expansión Game: Meta Visión")
st.markdown("""
### Asistente IA para la selección de componentes de computación
Expansión Game: Meta Visión te ayuda a elegir los mejores componentes de hardware según tus necesidades, 
validando compatibilidades y optimizando configuraciones.
""")

st.subheader("Describe tu necesidad:")
uso = st.text_area("Describe el uso principal de tu PC, tu presupuesto y los componentes que ya tienes o que deseas comprar.")

if st.button("Obtener Recomendación"):
    if uso:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(uso)

        st.subheader("Recomendación de IA")
        st.write(response.text)
    else:
        st.warning("Por favor, proporciona una descripción para generar recomendaciones.")

st.subheader("Iniciar selección guiada")

if "uso_principal" not in st.session_state:
    st.session_state.uso_principal = "Gaming"

if "presupuesto" not in st.session_state:
    st.session_state.presupuesto = "Medio"

st.session_state.uso_principal = st.radio("¿Para qué usarás la PC?", ["Gaming", "Edición de video", "Trabajo de oficina"], index=["Gaming", "Edición de video", "Trabajo de oficina"].index(st.session_state.uso_principal))

st.session_state.presupuesto = st.radio("Selecciona tu presupuesto", ["Bajo", "Medio", "Alto"], index=["Bajo", "Medio", "Alto"].index(st.session_state.presupuesto))

if st.button("Obtener Configuración Recomendada"):
    prompt_guiado = f"Quiero armar una PC para {st.session_state.uso_principal} con un presupuesto {st.session_state.presupuesto}."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt_guiado)
    
    st.subheader("Configuración Recomendada")
    st.write(response.text)

st.sidebar.title("Cómo funciona")
st.sidebar.markdown("""
- **Ingresa tu necesidad**: Escribe cómo planeas usar tu PC y tu presupuesto.
- **Generación IA**: Usamos inteligencia artificial para analizar tu solicitud.
- **Recibe una recomendación**: Obtén una lista de componentes compatibles.
- **Selección guiada**: Si no sabes qué escribir, sigue nuestra guía paso a paso.
""")