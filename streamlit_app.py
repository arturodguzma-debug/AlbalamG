import streamlit as st
import pandas as pd
import time
import requests
from gtts import gTTS
import base64
from langdetect import detect

st.set_page_config(page_title="AlbalamG Imperio Universal", page_icon="🐆", layout="wide")

# --- MEMORIA DEL FARO ---
if 'bitacora' not in st.session_state:
    st.session_state['bitacora'] = []
if 'inicio' not in st.session_state:
    st.session_state['inicio'] = time.time()

# --- RASTREADOR DE NACIONES ---
def rastrear_origen():
    try:
        d = requests.get('https://ipapi.co/json/').json()
        return f"{d.get('country_name')} ({d.get('city')})"
    except: return "Desconocido"

# --- VOZ Y TRADUCCIÓN ---
def hablar(t, lang):
    try:
        tts = gTTS(text=t, lang=lang)
        tts.save("v.mp3")
        with open("v.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except: pass

st.title("🐆 Oráculo AlbalamG Universal")
st.write(f"📍 Tu luz brilla desde: **{rastrear_origen()}**")

consulta = st.text_input("Consulta al Jaguar (Cualquier idioma):")

if st.button("Consultar"):
    if consulta:
        idioma = detect(consulta)
        res = "Tu cuerpo es un templo de resonancia. Busca la tierra." if idioma == "es" else "Your body is a resonance temple. Seek the earth."
        st.info(f"🐆 **Balam ({idioma.upper()}):** {res}")
        hablar(res, idioma)
        
        # Guardar estadística
        st.session_state['bitacora'].append({
            "Hora": time.strftime("%H:%M:%S"),
            "País/Ciudad": rastrear_origen(),
            "Idioma": idioma.upper(),
            "Feedback": "Pendiente"
        })
    else: st.warning("El Jaguar espera tu palabra.")

# --- SECCIÓN DE FEEDBACK ---
st.markdown("---")
f_user = st.text_area("⭐ ¿Cómo te sientes tras la consulta? Déjanos tu feedback:")
if st.button("Enviar"):
    if st.session_state['bitacora']:
        st.session_state['bitacora'][-1]["Feedback"] = f_user
        st.success("✨ Tu sentir ha sido integrado al Imperio.")

# --- PANEL SECRETO PARA TI ---
st.sidebar.title("🔑 Admin")
llave = st.sidebar.text_input("Llave Maestra:", type="password")
if llave == "balam-admin":
    st.sidebar.write("### 📊 Dictado de Estadísticas")
    df = pd.DataFrame(st.session_state['bitacora'])
    st.sidebar.dataframe(df)
    st.sidebar.write(f"⏱️ Tiempo de sesión: {round(time.time()-st.session_state['inicio'], 1)}s")
    