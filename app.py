import streamlit as st

# Erstelle eine Sidebar mit einem Selectbox-Menü für die Navigation
navigation = st.sidebar.radio(
    "Navigation",
    ("Problem Statement", "Methods & Data", "Technical Environment & Modeling", "Key Results", "Conclusion & Discussion")
)

# Basierend auf der Auswahl des Benutzers den Inhalt anpassen
if navigation == "Problem Statement":
    st.title("Problem Statement")
    st.markdown("""
    ## Hintergrund
    Hier kannst du das Problem in mehreren Abschnitten erläutern. Zum Beispiel:
    
    - Was ist das Problem?
    - Warum ist es wichtig?
    - Wer ist betroffen?
    
    ## Ziel der Untersuchung
    Dein Ziel könnte sein, Lösungen zu finden, die helfen, dieses Problem zu adressieren.
    """)
    # Weitere Details zum Problem Statement hinzufügen

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

