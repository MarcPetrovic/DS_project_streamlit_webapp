import streamlit as st
from PIL import Image

# Links for images
image_porter_url = "https://github.com/MarcPetrovic/DS_project_streamlit_webapp/raw/main/images/porter.PNG"

# Erstelle eine Sidebar mit einem Selectbox-Menü für die Navigation
navigation = st.sidebar.radio(
    "Navigation",
    ("Introduction", "Theoretical framework", "Methods & Data", "Technical Environment & Modeling", "Key Results", "Conclusion & Discussion")
)

# Basierend auf der Auswahl des Benutzers den Inhalt anpassen
if navigation == "Introduction":
    st.title("Introduction")
    # Bild von der URL laden und anzeigen
    st.image(image_porter_url, caption="Bild aus GitHub Repository", use_container_width=True)
    st.markdown("""
    Over the last two decades, globalization and ever-increasing regulation by the banking supervisory 
    authorities have presented the financial sector with major challenges: On the one hand, open markets 
    have led to an intensification of competitive pressure, which has simultaneously led to a decline in 
    profit margins. On the other hand, financial service providers had to implement cross-border requirements 
    to protect their customers and secure their own liquidity, the implementation of which was associated 
    with additional financial costs. Banks could and can only withstand the economic pressure described 
    above if they see digitalization as an opportunity. Modern marketing management at financial service 
    providers therefore combines business and artificial intelligence concepts with machine learning methods 
    (e.g. decision trees, regression or dimension reduction) in order to generate cost-optimized 
    communication campaigns.
    
    ## Ziel der Untersuchung
    Dein Ziel könnte sein, Lösungen zu finden, die helfen, dieses Problem zu adressieren.
    """)
    # Weitere Details zum Problem Statement hinzufügen 
    
# Basierend auf der Auswahl des Benutzers den Inhalt anpassen
elif navigation == "Theoretical framework":
    st.header("Theoretical Framework")

    # ----- Unternavigation auch in der Seitenleiste -----
    sub_section = st.sidebar.radio("Theoretical Subtopics", [
        "PORTER’S VALUE CHAIN APPROACH AND COST OPTIMIZATION",
        "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS",
        "SUPERVISED LEARNING AND THE RESPONSE-MODEL",
        "BRIEF INTRODUCTION TO CRISP-DM"
    ])

    # ----- Inhalte zu den Unterpunkten -----
    if sub_section == "PORTER’S VALUE CHAIN APPROACH AND COST OPTIMIZATION":
        st.subheader("Porter’s Value Chain Approach and Cost Optimization")
        st.write("Hier steht der Inhalt zu Porter's Value Chain ...")

    elif sub_section == "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS":
        st.subheader("The Relevance of Data Mining for Direct Marketing Campaigns")
        st.write("Hier steht der Inhalt über Data Mining ...")

    elif sub_section == "SUPERVISED LEARNING AND THE RESPONSE-MODEL":
        st.subheader("Supervised Learning and the Response-Model")
        st.write("Hier geht es um das Response-Modell ...")

    elif sub_section == "BRIEF INTRODUCTION TO CRISP-DM":
        st.subheader("Brief Introduction to CRISP-DM")
        st.write("CRISP-DM ist ein Data-Mining-Prozessmodell ...")

# ---- Andere Hauptpunkte ----
elif navigation == "Methods & Data":
    st.title("Methods & Data")
    st.write("Hier kannst du die Methoden und Daten, die du verwendet hast, erklären.")
    # Details zu den Methoden und Daten hinzufügen

elif navigation == "Technical Environment & Modeling":
    st.title("Technical Environment & Modeling")
    st.write("Hier kannst du die technische Umgebung und das Modellierungsverfahren beschreiben.")
    # Details zur technischen Umgebung und Modellierung hinzufügen

elif navigation == "Key Results":
    st.title("Key Results")
    st.write("Hier kannst du die wichtigsten Ergebnisse deiner Analyse präsentieren.")
    # Details zu den wichtigsten Ergebnissen hinzufügen

elif navigation == "Conclusion & Discussion":
    st.title("Conclusion & Discussion")
    st.write("Hier kannst du deine Schlussfolgerungen und Diskussionen darlegen.")
    # Details zur Schlussfolgerung und Diskussion hinzufügen

