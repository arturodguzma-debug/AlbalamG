import streamlit as st

st.set_page_config(page_title="AlbalamG Global", page_icon="🐆")

idioma = st.sidebar.selectbox("🌐 Idioma", ["Español", "English", "Français", "Português"])

textos = {
"Español": {"titulo": "🐆 Imperio AlbalamG", "sub": "Faro Universal", "msg": "Ofrenda de Poder", "pago": "$2.00 USD USDT (BEP20)", "boton": "Enviar", "exito": "¡Sello de Lealtad!"},
"English": {"titulo": "🐆 AlbalamG Empire", "sub": "Universal Lighthouse", "msg": "Power Offering", "pago": "$2.00 USD USDT (BEP20)", "boton": "Send", "exito": "Loyalty Sealed!"}
}

t = textos.get(idioma, textos["Español"])

st.title(t["titulo"])
st.header(t["sub"])
st.write(t["msg"])
st.info(t["pago"])
st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")

st .button(t["boton"]):
st.balloons(    )
st.success(t["exito"])
    