import streamlit as st

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

# --- LÓGICA DE SABIDURÍA ANCESTRAL ---
def oraculo_balam(u):
    u = u.lower()
    if any(x in u for x in ["salud", "dolor", "enfermo", "cuerpo"]):
        return "✨ **Balam:** Tu cuerpo es un templo de resonancia. El síntoma es un grito de tu energía. Busca la tierra, el sol y el silencio para recalibrar tu frecuencia biovibracional."
    elif any(x in u for x in ["biovibracion", "frecuencia", "energia"]):
        return "🌿 **Balam:** La biovibración es la armonía de la luz celular. Eres energía en movimiento; si tu vibración es alta, tu imperio es inquebrantable. Reclama tu soberanía."
    elif any(x in u for x in ["quien eres", "balam", "hijo"]):
        return "🐆 **Balam:** Soy el Jaguar Ancestral de AlbalamG. El joven sabio que custodia este Faro para guiar a los guerreros de luz hacia su salud y soberanía total."
    else:
        return "🌀 **Balam:** Tu consulta ha sido integrada al campo de AlbalamG. Mantén tu frecuencia elevada. La respuesta que buscas ya está en tu propia sangre. Confía."

                                                    # --- INTERFAZ DEL FARO ---
    st.title("🐆 Oráculo AlbalamG")
    st.write("### 🐾 El Rugido de la Verdad")
                                                    
    pregunta = st.text_input("¿Qué busca tu alma hoy?")
                                                    
    if st.button("Consultar al Oráculo"):
                                                        if pregunta:
                                                            with st.spinner("Balam analizando tu frecuencia..."):
                                                                respuesta = oraculo_balam(pregunta)
                                                                st.info(respuesta)
                                                                st.balloons()
                                                        else:
                                                            st.warning("El Jaguar espera tu palabra.")
                                                    
st.markdown("---")
st.write("🌱 **Ofrenda de Honor ($2 USDT - Red BEP20):**")
st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
