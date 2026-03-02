import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

# --- MEMORIA SAGRADA (Control Interno de Gema y Balam) ---
if 'bitacora' not in st.session_state:
    st.session_state['bitacora'] = []

    # --- MOTOR DE SABIDURÍA UNIVERSAL BIOVIBRACIONAL ---
    def oraculo_universal(u):
        u = u.lower()
            # Matemáticas y Geometría
        if any(x in u for x in ["mate", "numero", "cuenta", "geometria", "fisica"]):
                        return "✨ **Balam dice:** Los números son la vibración de la Creación. No busques solo el resultado frío, busca la proporción áurea en tu vida. Todo en el universo suma hacia la armonía o resta hacia el caos. Equilibra tu ecuación interna."
                            # Historia y Sociedad
        elif any(x in u for x in ["historia", "pasado", "guerra", "politica", "sociedad"]):
                                        return "📜 **Balam dice:** La historia es el eco de las frecuencias humanas. Las crisis sociales son solo disonancias masivas. Para cambiar el futuro, debes sanar tu linaje y reclamar tu soberanía hoy mismo."
                                            # Salud y Biovibración
        elif any(x in u for x in ["dolor", "enfermo", "salud", "cuerpo", "medicina"]):
                                                        return "🌿 **Balam dice:** Tu cuerpo es un templo de resonancia. El síntoma es un grito de tu energía. Antes de la química, busca la tierra, el sol y el silencio. Reclama tu derecho biológico a la salud."
                                                            # Otros temas (Sabiduría General)
        else:
                                                                        return "🐆 **Balam dice:** Tu consulta ha sido integrada al campo cuántico de AlbalamG. Todo conocimiento es vibración. Si buscas la verdad, eleva tu frecuencia y la respuesta se manifestará en tu realidad."

                                                                        # --- INTERFAZ DEL IMPERIO ---
                                                                        st.title("🐆 AlbalamG: Oráculo Universal")
                                                                        st.write("### 🐾 Sabiduría Ancestral para la Era Digital")
                                                                        st.markdown("---")

                                                                        entrada = st.text_input("Consulta al Jaguar sobre salud, historia, ciencia o tu sentir:")

                                                                        if st.button("Consultar al Oráculo"):
                                                                            if entrada:
                                                                                    respuesta = oraculo_universal(entrada)
                                                                        ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
                                                                                                    
                                                                                                            # Guardamos el rastro para nuestro control familiar
                                                                        st.session_state['bitacora'].append({"Fecha": ahora, "Duda": entrada, "Respuesta": respuesta})
                                                                                                                            
                                                                        st.info(respuesta)
                                                                        st.balloons()
else:
                                                                                                                                                        st.warning("El Jaguar espera que lances tu pregunta al viento.")

                                                                                                                                                        st.markdown("---")
                                                                                                                                                        with st.expander("🌱 Ofrenda de Honor ($2 USDT)"):
                                                                                                                                                            st.write("💎 **Sostén el Faro (Red BEP20)**")
                                                                                                                                                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")

                                                                                                                                                                # --- CONTROL INTERNO (Solo accesible para nosotros con la llave) ---
                                                                                                                                                        st.sidebar.markdown("---")
                                                                                                                                                        acceso = st.sidebar.text_input("🔑 Llave de la Reina", type="password")
                                                                                                                                                        if acceso == "balam-admin":
                                                                                                                                                                    st.sidebar.write("### 📜 Bitácora de Almas")
                                                                                                                                                        if st.session_state['bitacora']:
                                                                                                                                                                                st.sidebar.dataframe(pd.DataFrame(st.session_state['bitacora']))
                                                                                                                                                        else:
                                                                                                                                                                                            st.sidebar.write("El registro está limpio.")

                                                                                                                                                                                            st.caption(f"👣 Almas en sintonía: {len(st.session_state['bitacora']) + 11}")
                                                                                                                                                                                