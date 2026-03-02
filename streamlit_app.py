import streamlit as st

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

st.title("🐆 Oráculo AlbalamG")
st.write("### 🐾 Sabiduría Biovibracional")

u = st.text_input("Consulta al Jaguar:")

if st.button("Consultar"):
    if u:
        st.info("🐆 Balam dice: Tu cuerpo es un templo de resonancia. Busca la tierra para sanar.")
    else:
     st.warning("Escribe tu consulta.")
st.balloons()

st.markdown("---")
st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
            