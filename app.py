import streamlit as st

# Erstelle eine Sidebar mit einem Selectbox-Menü für die Navigation
navigation = st.sidebar.radio(
    "Navigation",
    ("Introduction", "Theoretical framework", "Methods & Data", "Technical Environment & Modeling", "Key Results", "Conclusion & Discussion")
)


# Basierend auf der Auswahl des Benutzers den Inhalt anpassen
if navigation == "Introduction":
    st.title("Introduction")
    st.markdown("""
    Over the last two decades, globalization and ever-increasing regulation by the banking supervisory 
    authorities have presented the financial sector with major challenges: On the one hand, open markets 
    have led to an intensification of competitive pressure, which has simultaneously led to a decline in 
    profit margins. On the other hand, financial service providers had to implement cross-border requirements 
    to protect their customers and secure their own liquidity, the implementation of which was associated 
    with additional financial costs. Banks could and can only withstand the economic pressure described 
    above if they see digitalization as an opportunity. Modern marketing management at financial service 
    providers therefore combines business and artificial intelligence concepts with machine learning methods 
    (e.g. decision trees, regression or dimension reduction) in order to generate cost-opti¬mized 
    communication campaigns.
    
    ## Ziel der Untersuchung
    Dein Ziel könnte sein, Lösungen zu finden, die helfen, dieses Problem zu adressieren.
    """)
    # Weitere Details zum Problem Statement hinzufügen 
# Basierend auf der Auswahl des Benutzers den Inhalt anpassen
elif navigation == "Theoretical framework":
    st.title("Problem Statement")
    st.markdown("""
    ## PORTER’S VALUE CHAIN APPROACH AND COST OPTIMIZATION
    The general institutionalization of Porter's value chain approach at the beginning of the 1980s 
    also led to a shift away from traditional sales models in companies. The special feature of Porter's 
    approach is that the division between primary and secondary activities within the value chain and 
    the comparison of these with the margin makes it possible to determine the costs of producing a 
    product or service. Through the practical application of Porter's value chain approach, it has been 
    empirically proven that conventional sales strategies, in which all customers are offered the same 
    sales promotion and at the same time the differences between customers are neglected, are associated 
    with high operating expenses and low monetary benefits
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

