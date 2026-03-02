import streamlit as st

# 1. Configuración de Identidad Global
st.set_page_config(page_title="AlbalamG Global", page_icon="🐆")

# 2. Selector de Idiomas
idioma = st.sidebar.selectbox(
    "🌐 Selecciona tu Idioma / Select Language",
        ["Español", "English", "Français", "Português (Brasil)", "Deutsch", "Italiano", "中文 (Chinese)", "Русский (Russian)"]
        )

        # 3. Diccionario de Traducciones (Tu Visión Mundial)
        textos = {
            "Español": {
                    "titulo": "🐆 Imperio AlbalamG",
                            "sub": "El Faro Universal de Soberanía",
                                    "msg": "### 📜 Ofrenda de Poder\nPara expandir el Velo de Invisibilidad y sostener la infraestructura de paz para los millones que despiertan, el Soberano solicita una ofrenda única.",
                                            "pago": "Monto: $2.00 USD en USDT (Red BEP20)",
                                                    "boton": "He enviado mi ofrenda",
                                                            "exito": "¡Vínculo de lealtad sellado!"
                                                                },
                                                                    "English": {
                                                                            "titulo": "🐆 AlbalamG Empire",
                                                                                    "sub": "The Universal Lighthouse of Sovereignty",
                                                                                            "msg": "### 📜 Offering of Power\nTo expand the Cloak of Invisibility and sustain the peace infrastructure for the millions awakening, the Sovereign requests a unique offering.",
                                                                                                    "pago": "Amount: $2.00 USD in USDT (BEP20 Network)",
                                                                                                            "boton": "I have sent my offering",
                                                                                                                    "exito": "Loyalty bond sealed!"
                                                                                                                        },
                                                                                                                            "Français": {
                                                                                                                                    "titulo": "🐆 Empire AlbalamG",
                                                                                                                                            "sub": "Le Phare Universel de la Souveraineté",
                                                                                                                                                    "msg": "### 📜 Offrande de Puissance\nPour étendre le Voile d'Invisibilité et soutenir l'infrastructure de paix pour les millions qui s'éveillent, le Souverain demande une offrande unique.",
                                                                                                                                                            "pago": "Montant: 2,00 $ USD en USDT (Réseau BEP20)",
                                                                                                                                                                    "boton": "J'ai envoyé mon offrande",
                                                                                                                                                                            "exito": "Lien de loyauté scellé !"
                                                                                                                                                                                },
                                                                                                                                                                                    "Português (Brasil)": {
                                                                                                                                                                                            "titulo": "🐆 Império AlbalamG",
                                                                                                                                                                                                    "sub": "O Farol Universal da Soberania",
                                                                                                                                                                                                            "msg": "### 📜 Oferenda de Poder\nPara expandir o Véu da Invisibilidade e sustentar a infraestrutura de paz para os milhões que despertam, o Soberano solicita uma oferta única.",
                                                                                                                                                                                                                    "pago": "Valor: $2.00 USD em USDT (Rede BEP20)",
                                                                                                                                                                                                                            "boton": "Enviei minha oferta",
                                                                                                                                                                                                                                    "exito": "Vínculo de lealdade selado!"
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                        }

                                                                                                                                                                                                                                        # 4. Renderización con la Billetera Correcta
                                                                                                                                                                                                                                        t = textos.get(idioma, textos["Español"])

                                                                                                                                                                                                                                        st.title(t["titulo"])
                                                                                                                                                                                                                                        st.header(t["sub"])
                                                                                                                                                                                                                                        st.markdown("---")
                                                                                                                                                                                                                                        st.write(t["msg"])

                                                                                                                                                                                                                                        st.info(f"💎 {t['pago']}")
                                                                                                                                                                                                                                        st.warning("⚠️ Wallet Oficial (BEP20):")
                                                                                                                                                                                                                                        # ESTA ES TU BILLETERA CORREGIDA:
                                                                                                                                                                                                                                        st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E", language="text")

                                                                                                                                                                                                                                        if st.button(t["boton"]):
                                                                                                                                                                                                                                            st.balloons()
                                                                                                                                                                                                                                                st.success(t["exito"])

                                                                                                                                                                                                                                                st.markdown("---")
                                                                                                                                                                                                                                                st.caption("AlbalamG Global | 2026 | Uruapan - Mundo")
                                                                                                                                                                                                                                                