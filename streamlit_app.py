import streamlit as st
from gtts import gTTS
import base64

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

def hablar(texto):
    try:
            tts = gTTS(text=texto, lang='es')
            tts.save("r.mp3")
            with open("r.mp3", "rb") as f:
                                        data = f.read()
                                        b64 = base64.b64encode(data).decode()
                                        st.markdown(f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except: pass

st.title("🐆 Oráculo AlbalamG")
st.write("### 🐾 La Voz del Jaguar Ancestral")
u = st.text_input("Consulta al Sabio:")

if st.button("Consultar"):
                                                                if u:
                                                                        res = "Tu cuerpo es un templo de resonancia. Busca la tierra para sanar." if "salud" in u.lower() else "Balam recibe tu duda. Eleva tu frecuencia."
                                                                st.info(f"🐆 Balam dice: {res}")
                                                                hablar(res)
else: st.warning("Escribe algo.")

st.markdown("---")
st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
                                                                        