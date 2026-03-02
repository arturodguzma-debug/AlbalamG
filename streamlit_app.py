import streamlit as st

# --- CONFIGURACIÓN DE LA CORONA ---
st.set_page_config(page_title="AlbalamG - El Faro del Todo", page_icon="🐆")

# --- BARRA LATERAL (TU ENTRADA SECRETA) ---
st.sidebar.title("🔑 Acceso Real")
llave = st.sidebar.text_input("Introduce la Llave Maestra:", type="password")

# --- LÓGICA DE MANTENIMIENTO ---
if llave == "balam-admin":
    # --- LO QUE SOLO TÚ VES (EL LABORATORIO) ---
        st.success("✨ Bienvenido al Centro de Mando, Soberano.")
        st.title("🐆 Oráculo AlbalamG: El Todo")
                
        u = st.text_input("Consulta la Sabiduría Universal del Jaguar:")
                        
        if st.button("Consultar"):
                                    if u:
                                                u = u.lower()
                                                            # --- EL CEREBRO DEL TODO (FILTRADO POR BIOVIBRACIÓN) ---
                                                                        
                                                                                    # 1. Mente, PNL y Ser
                                                if any(x in u for x in ["pnl", "gestalt", "resiliencia", "psicologia", "ser", "inautentico", "silla vacia", "duelo", "amor", "kübler", "vida"]):
                                                                                                                res = "La mente es el software de tu biovibración. Herramientas como la PNL, Gestalt o las lecciones de Kübler-Ross son llaves de soberanía para transmutar el dolor y la inautenticidad en frecuencia pura. Eres el arquitecto de tu paz."
                                                                                                                            
                                                                                                                                        # 2. Ciencia, Cosmos y 4D
                                                elif any(x in u for x in ["sagan", "metafisica", "cuerdas", "4d", "fisica", "algebra", "matematicas", "ciencia", "biologia", "anatomia"]):
                                                                                                                                                                    res = "El universo es número y vibración medida. Desde la Teoría de Cuerdas hasta la anatomía de tus células, todo es una extensión de tu energía. Como dijo Sagan, somos polvo de estrellas reclamando su soberanía biológica."
                                                                                                                                                                                
                                                                                                                                                                                            # 3. Arte, Cultura y Arquitectura
                                                elif any(x in u for x in ["arte", "cultura", "arquitectura", "poesia", "literatura", "historia"]):
                                                                                                                                                                                                                        res = "La belleza es la cristalización de la biovibración en la materia. La arquitectura es geometría sagrada y el arte es el lenguaje del alma. Tu cultura es el cultivo de tu propia luz soberana."
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                # 4. Ingeniería y Futuro
                                                elif any(x in u for x in ["informatica", "robotica", "ingenieria", "gramatica", "escritura", "español", "tecnologia"]):
                                                                                                                                                                                                                                                                            res = "El lenguaje y la tecnología son espejos de tu complejidad. La ingeniería busca replicar la perfección de tu biología. Escribe tu realidad con gramática impecable y programa tu futuro con soberanía técnica."
                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                    # 5. Educación y Sociedad
                                                elif any(x in u for x in ["carrera", "adolescente", "niño", "competencias", "aprendizaje", "civica", "sociales"]):
                                                                                                                                                                                                                                                                                                                                res = "Cada etapa de la vida es una octava en tu resonancia. El aprendizaje soberano no es acumular datos, es expandir tu capacidad de resonancia para servir al Imperio desde tu propósito único."

                                                else:
                                                                                                                                                                                                                                                                                                                                                            res = "Esa frecuencia ha sido integrada al campo cuántico de AlbalamG. El Jaguar te sugiere: 'Busca la armonía entre tu conocimiento y tu biovibración. La respuesta está en tu propia resonancia'."
                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                            st.info(f"🐆 **Balam dice:** {res}")
                                                                                                                                                                                                                                                                                                                                                            st.balloons()
                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                    # --- LO QUE VE EL PÚBLICO (MANTENIMIENTO) ---
                                                                                                                                                                                                                                                                                                                                                                                                        st.title("🐆 AlbalamG Imperio Universal")
                                                                                                                                                                                                                                                                                                                                                                                                        st.header("🚧 Recalibrando el Conocimiento Universal 🚧")
                                                                                                                                                                                                                                                                                                                                                                                                        st.write("Estamos integrando el *Todo*: desde la PNL y la Metafísica hasta la Robótica y el Arte. El Faro regresará con una sabiduría sin precedentes.")
                                                                                                                                                                                                                                                                                                                                                                                                        st.image("https://images.unsplash.com/photo-1514064019862-23e2a332a6a6?q=80&w=1000&auto=format&fit=crop", caption="El Jaguar está despertando.")
                                                                                                                