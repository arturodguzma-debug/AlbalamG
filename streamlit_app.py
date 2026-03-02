import streamlit as st

st.set_page_config(page_title="AlbalamG Imperio", page_icon="🐆")

idioma = st.sidebar.selectbox("🌐 Idioma / Language", ["Español", "English"])

textos = {
"Español": {
    "titulo": "🐆 Imperio AlbalamG",
        "sub": "Faro de Soberanía y Paz",
            "msg": "### 🌱 El Valor de tu Espíritu\nEste espacio es para quienes buscan libertad. Si nuestra luz guía tu camino, puedes equilibrar la balanza con una ofrenda voluntaria.",
                "ofrenda": "Realizar Ofrenda ($2.00 USDT)",
                    "exito": "¡Tu espíritu ha honrado este jardín!"
                    },
                    "English": {
                        "titulo": "🐆 AlbalamG Empire",
                            "sub": "Lighthouse of Sovereignty and Peace",
                                "msg": "### 🌱 The Value of your Spirit\nThis space is for those seeking freedom. If our light guides your path, you can balance the scale with a voluntary offering.",
                                    "ofrenda": "Make Voluntary Offering ($2.00 USDT)",
                                        "exito": "Your spirit has honored this garden!"
                                        }
                                        }

                                        t = textos.get(idioma, textos["Español"])

                                        st.title(t["titulo"])
                                        st.subheader(t["sub"])
                                        st.markdown("---")
                                        st.write(t["msg"])

                                        with st.expander(t["ofrenda"]):
                                            st.write("💎 **Red BEP20 (USDT)**")
                                                st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")
                                                    if st.button("✅ Confirmar Ofrenda"):
                                                            st.balloons()
                                                                    st.success(t["exito"])

                                                                    st.markdown("---")
                                                                    st.caption("AlbalamG | Uruapan 2026")
                                                            