import streamlit as st

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

# 1. Selector de Idiomas
idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Español", "English"])

# 2. Diccionario con tono de "Jardinero" (Voluntario)
textos = {
"Español": {
    "titulo": "🐆 Bienvenid@ a AlbalamG",
        "sub": "Espacio de Paz y Soberanía",
            "msg": "### 🌱 Sembrando Conciencia\nEste es un espacio abierto. Si nuestra guía te ha servido, puedes apoyar voluntariamente el mantenimiento de este jardín digital.",
                "boton_pago": "Realizar Ofrenda Voluntaria ($2 USDT)",
                    "boton_consulta": "💬 Ir a Consultas (Gratuito)",
                        "exito": "¡Gracias por nutrir este jardín!"
                        },
                        "English": {
                            "titulo": "🐆 Welcome to AlbalamG",
                                "sub": "Space of Peace and Sovereignty",
                                    "msg": "### 🌱 Sowing Awareness\nThis is an open space. If our guidance has helped you, you can voluntarily support the maintenance of this digital garden.",
                                        "boton_pago": "Make Voluntary Offering ($2 USDT)",
                                            "boton_consulta": "💬 Go to Consultations (Free)",
                                                "exito": "Thank you for nurturing this garden!"
                                                }
                                                }

t = textos.get(idioma, textos["Español"])

                                                # 3. Interfaz del Portal
st.title(t["titulo"])
st.subheader(t["sub"])
st.markdown("---")

                                                # Botón de Consulta (El primero para no ahuyentar)
                                                # if st.button(t["boton_consulta"]):
st.info("🚀 Redirigiendo al Oráculo de Consultas... (Aquí pondremos el link de tu otra plataforma)")

st.write(t["msg"])

                                                    # Sección de Ofrenda (Elegante y no invasiva)
with st.expander(t["boton_pago"]):
                                                        st.write("💎 **Red BEP20 (BNB Smart Chain)**")
                                                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
                                                        if st.button("✅ Hecho"):
                                                                        st.balloons()
                                                                        st.success(t["exito"])

                                                                        st.markdown("---")
                                                                        st.caption("AlbalamG | Uruapan - 2026")
                                                        