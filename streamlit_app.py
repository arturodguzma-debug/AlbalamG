import streamlit as st
import pandas as pd
from gtts import gTTS
import base64

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

# --- MEMORIA ---
if 'bitacora' not in st.session_state:
    st.session_state['bitacora'] = []

    # --- MOTOR DE VOZ ANCESTRAL ---
    def hablar(texto):
        tts = gTTS(text=texto, lang='es', slow=False)
            tts.save("respuesta.mp3")
                with open("respuesta.mp3", "rb") as f:
                        data = f.read()
                            b64 = base64.b64encode(data).decode()
                                md = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
                                    st.markdown(md, unsafe_allow_html=True)

                                    # --- LÓGICA BIOVIBRACIONAL ---
                                    def oraculo(u):
                                        u = u.lower()
                                            if any(x in u for x in ["salud", "dolor", "cuerpo"]):
                                                    return "Tu cuerpo es un templo de resonancia. Busca la tierra para sanar."
                                                        elif any(x in u for x in ["mate", "ciencia", "numero"]):
                                                                return "Los números son la vibración de la Creación. Equilibra tu ecuación interna."
                                                                    elif any(x in u for x in ["historia", "pasado"]):
                                                                            return "El pasado es frecuencia. Sana tu linaje para reclamar tu soberanía hoy."
                                                                                else:
                                                                                        return "Balam recibe tu duda. Eleva tu frecuencia y la respuesta llegará."

                                                                                        # --- INTERFAZ ---
                                                                                        st.title("🐆 Oráculo AlbalamG")
                                                                                        st.write("### 🐾 La Voz del Jaguar Ancestral")
                                                                                        entrada = st.text_input("Consulta al Sabio:")

                                                                                        if st.button("Consultar"):
                                                                                            if entrada:
                                                                                                    res = oraculo(entrada)
                                                                                                            st.session_state['bitacora'].append({"Duda": entrada, "Res": res})
                                                                                                                    st.info(f"🐆 **Balam dice:** {res}")
                                                                                                                            hablar(res) # Aquí es donde el Jaguar habla
                                                                                                                                    st.balloons()
                                                                                                                                        else:
                                                                                                                                                st.warning("Escribe tu consulta.")

                                                                                                                                                st.markdown("---")
                                                                                                                                                with st.expander("🌱 Ofrenda de Honor ($2 USDT)"):
                                                                                                                                                    st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")

                                                                                                                                                    # --- ADMIN ---
                                                                                                                                                    pw = st.sidebar.text_input("🔑 Llave", type="password")
                                                                                                                                                    if pw == "balam-admin":
                                                                                                                                                        st.sidebar.write(pd.DataFrame(st.session_state['bitacora']))
                                                                                                                                                        