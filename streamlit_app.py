import streamlit as st

st.set_page_config(page_title="AlbalamG", page_icon="🐆")

# 1. Oráculo
st.title("🐆 Oráculo AlbalamG")
st.write("### 🐾 Habla con el Jaguar")
pregunta = st.text_input("¿Qué busca tu alma?")

if st.button("Consultar"):
    if pregunta:
            st.info("✨ **Balam dice:** 'Tu vibración es recibida. Escucha tu sangre y equilibra tu energía.'")
            st.balloons()

            st.markdown("---")

                    # 2. Ofrenda
            with st.expander("🌱 Ofrenda de Honor ($2 USDT)"):
                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")

                        # 3. Contador
                        if 'v' not in st.session_state: st.session_state['v'] = 1
                        else: st.session_state['v'] += 1
                        st.caption(f"👣 Almas: {st.session_state['v']}")
