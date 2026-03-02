import streamlit as st
     
st.set_page_config(page_title="AlbalamG Oráculo", page_icon="🐆")
     
     # 1. Configuración de Sesión
if 'visitas' not in st.session_state:
         st.session_state['visitas'] = 1
else:
     st.session_state['visitas'] += 1
             
             # 2. Textos Biovibracionales
st.title("🐆 Oráculo AlbalamG")
st.subheader("Guía Biovibracional y Soberanía")
st.markdown("---")
             
st.write("### 🐾 Habla con el Jaguar")
st.write("Siente tu frecuencia y entrega tu duda. Balam te guiará.")
             
             # 3. El Salón de Consulta
pregunta = st.text_area("¿Qué busca saber tu alma?", height=100)
             
if st.button("Consultar al Oráculo"):
                 if pregunta:
                         with st.spinner("Balam conectando..."):
                                     st.info("✨ **Respuesta:** Tu vibración es recibida. Balam dice: 'Escucha el rugido de tu sangre y equilibra tu energía'.")
                                     st.balloons()
else:
                                                 st.warning("El Jaguar espera tus palabras.")
                                                             
                                                 st.markdown("---")
                                                             
                                                             # 4. El Jardinero (Ofrenda)
                                                 with st.expander("🌱 Ofrenda Voluntaria ($2 USDT)"):
                                                                 st.write("💎 **Red BEP20**")
                                                 st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
                                                                     
                                                 st.markdown("---")
                                                 st.caption(f"👣 Almas en el Faro: {st.session_state['visitas']}")
                                                 st.info(f"✨ **Respuesta del Oráculo:**\n\nTu vibración ha sido recibida. Recuerda que la salud 
                                                                                                                                                                                       