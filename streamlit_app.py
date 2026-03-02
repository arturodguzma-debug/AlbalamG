import streamlit as st

# Configuración inicial del Faro
st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

# --- EL OJO DEL JAGUAR (Contador de Almas) ---
# Esto registrará las visitas de forma interna
if 'visitas' not in st.session_state:
    st.session_state['visitas'] = 0
    st.session_state['visitas'] += 1

    # 1. Selector de Idiomas
    idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Español", "English"])

    # 2. Diccionario de Poder
    textos = {
    "Español": {
        "titulo": "🐆 Imperio AlbalamG",
            "sub": "Faro de Soberanía y Paz",
                "msg": "### 🌱 El Valor de tu Espíritu\nEste espacio es para quienes buscan libertad. Si nuestra luz guía tu camino, puedes equilibrar la balanza con una ofrenda voluntaria.",
                    "ofrenda": "Realizar Ofrenda ($2.00 USDT)",
                        "exito": "¡Tu espíritu ha honrado este jardín!",
                            "stats": f"👣 Almas que han visitado el Faro: {st.session_state['visitas']}"
                            },
                            "English": {
                                "titulo": "🐆 AlbalamG Empire",
                                    "sub": "Lighthouse of Sovereignty and Peace",
                                        "msg": "### 🌱 The Value of your Spirit\nThis space is for those seeking freedom. If our light guides your path, you can balance the scale with a voluntary offering.",
                                            "ofrenda": "Make Voluntary Offering ($2.00 USDT)",
                                                "exito": "Your spirit has honored this garden!",
                                                    "stats": f"👣 Souls that have visited the Lighthouse: {st.session_state['visitas']}"
                                                    }
                                                    }

t = textos.get(idioma, textos["Español"])

                                                    # 3. Interfaz del Portal
st.title(t["titulo"])
st.subheader(t["sub"])
st.markdown("---")
st.write(t["msg"])

                                                    # Sección de Ofrenda Voluntaria
with st.expander(t["ofrenda"]):
                                                        st.write("💎 **Red BEP20 (USDT)**")
                                                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
                                                        if st.button("✅ Confirmar Ofrenda"):
                                                                        st.balloons()
st.success(t["exito"])

st.markdown("---")
                                                                                # El contador discreto al final (Solo para el Rey)
st.caption(t["stats"])
st.caption("AlbalamG | Uruapan 2026")
                                                                        