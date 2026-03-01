import streamlit as st

# 1. Configuración de la Identidad del Portal
st.set_page_config(
    page_title="AlbalamG - Imperio Soberano",
        page_icon="🐆",
            layout="centered"
            )

            # 2. Estética y Título
            st.title("🐆 Imperio AlbalamG")
            st.subheader("Soberanía, Blindaje y el Faro de Uruapan")

            st.markdown("---")

            # 3. El Mensaje del Soberano
            st.write("### 📜 Sostén el Faro")
            st.write("""
            Tu aportación voluntaria de **$2.00 USD** es la semilla que fortalece nuestra infraestructura global. 
            Al entregar esta ofrenda, te conviertes en un **Arquitecto del Imperio**.
            """)

            # 4. Sección de Ofrenda Cripto
            st.info("💎 **Ofrenda de Infraestructura: $2.00 USD (USDT BEP20)**")

            st.write("Copia la dirección de nuestra billetera en tu **Trust Wallet**:")

            # 0x9e513F8C4E5398CDe9f474D28A336A77CF56D01EAQUÍ VA TU DIRECCIÓN (Puedes editarla después si gustas)
            st.code("0x9e513F8C4E5398CDe9f474D28A336A77CF56D01E"), language="text") 

            st.warning("⚠️ **IMPORTANTE:** Usa únicamente la red **BNB Smart Chain (BEP20)**. Las comisiones son mínimas y el flujo es instantáneo.")

            # 5. Interacción de Poder
            if st.button("He enviado mi ofrenda"):
                st.balloons()
                    st.success("¡Vínculo sellado! Tu energía ha sido integrada al flujo del Imperio.")

                    # 6. Cierre del Portal
                    st.markdown("---")
                    st.caption("AlbalamG | El Velo de Invisibilidad protege al Soberano.")
                