import streamlit as st
import pandas as pd
import time
import requests
from gtts import gTTS
import base64
from langdetect import detect

# --- CONFIGURACIÓN DEL IMPERIO ---
st.set_page_config(page_title="AlbalamG Universal", page_icon="🐆", layout="wide")

if 'bitacora' not in st.session_state:
    st.session_state['bitacora'] = []
    if 'inicio' not in st.session_state:
        st.session_state['inicio'] = time.time()

        # --- RASTREO GEOGRÁFICO ---
        def rastrear_origen():
            try:
                    d = requests.get('https://ipapi.co/json/').json()
                            return f"{d.get('country_name')} ({d.get('city')})"
                                except: return "Frontera Desconocida"

                                # --- VOZ Y RUGIDO ---
                                def rugido_balam(t, lang):
                                    try:
                                            tts = gTTS(text=t, lang=lang)
                                                    tts.save("v.mp3")
                                                            with open("v.mp3", "rb") as f:
                                                                        data = f.read()
                                                                                b64 = base64.b64encode(data).decode()
                                                                                        st.markdown(f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
                                                                                            except: pass

                                                                                            # --- INTERFAZ DEL FARO ---
                                                                                            st.title("🐆 Oráculo AlbalamG Universal")
                                                                                            st.write(f"📍 Tu luz se emite desde: **{rastrear_origen()}**")

                                                                                            consulta = st.text_input("Consulta al Jaguar (Cualquier idioma):")

                                                                                            if st.button("Consultar al Oráculo"):
                                                                                                if consulta:
                                                                                                        idioma = detect(consulta)
                                                                                                                # Respuesta base (se puede expandir más adelante)
                                                                                                                        res = "Tu cuerpo es un templo de resonancia. Busca la tierra." if idioma == "es" else "Your body is a resonance temple. Seek the earth."
                                                                                                                                
                                                                                                                                        st.info(f"🐆 **Balam ({idioma.upper()}):** {res}")
                                                                                                                                                rugido_balam(res, idioma)
                                                                                                                                                        
                                                                                                                                                                # Guardar en la Bitácora de Inteligencia
                                                                                                                                                                        st.session_state['bitacora'].append({
                                                                                                                                                                                    "Hora": time.strftime("%H:%M:%S"),
                                                                                                                                                                                                "País/Ciudad": rastrear_origen(),
                                                                                                                                                                                                            "Idioma": idioma.upper(),
                                                                                                                                                                                                                        "Consulta": consulta,
                                                                                                                                                                                                                                    "Feedback": "N/A"
                                                                                                                                                                                                                                            })
                                                                                                                                                                                                                                                    st.balloons()
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                st.warning("El Jaguar espera tu palabra.")

                                                                                                                                                                                                                                                                # --- SECCIÓN DE FEEDBACK ---
                                                                                                                                                                                                                                                                st.markdown("---")
                                                                                                                                                                                                                                                                st.write("### ⭐ Tu Sentir (Retroalimentación)")
                                                                                                                                                                                                                                                                f_user = st.text_area("¿Cómo te sientes tras esta consulta?")
                                                                                                                                                                                                                                                                if st.button("Enviar al Imperio"):
                                                                                                                                                                                                                                                                    if st.session_state['bitacora']:
                                                                                                                                                                                                                                                                            st.session_state['bitacora'][-1]["Feedback"] = f_user
                                                                                                                                                                                                                                                                                    st.success("✨ Tu vibración ha sido integrada al corazón de AlbalamG.")

                                                                                                                                                                                                                                                                                    # --- PANEL ADMIN (ESTADÍSTICAS) ---
                                                                                                                                                                                                                                                                                    st.sidebar.title("🔑 Admin")
                                                                                                                                                                                                                                                                                    llave = st.sidebar.text_input("Llave Maestra:", type="password")
                                                                                                                                                                                                                                                                                    if llave == "balam-admin":
                                                                                                                                                                                                                                                                                        st.sidebar.write("### 📊 Dictado de Estadísticas")
                                                                                                                                                                                                                                                                                            df = pd.DataFrame(st.session_state['bitacora'])
                                                                                                                                                                                                                                                                                                st.sidebar.dataframe(df)
                                                                                                                                                                                                                                                                                                    st.sidebar.write(f"⏱️ Tiempo de conexión: {round(time.time()-st.session_state['inicio'], 1)}s")

                                                                                                                                                                                                                                                                                                    with st.expander("🌱 Ofrenda de Honor ($2 USDT)"):
                                                                                                                                                                                                                                                                                                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
