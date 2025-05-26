import streamlit as st
from utils.image_loader import show_github_image

def show():
  # Dropdown für die Phasen
    phase = st.selectbox("Select a subchapter of CRISP-DM-phase Data Understanding:", [
        "General Procedere & EDA",
        "Instructions Primary Researcher",
        "Data Audit - Client Socio-Economic Attributes",
        "Data Audit - Economic Environment",
        "Data Audit - Current Marketing Activities",
        "Data Audit - Previous Marketing Activities",
        "Key Results of the 2nd Phase"
    ])
    # Inhalte je nach Auswahl
    if phase == "General Procedere & EDA":
        st.subheader("1. General Procedere & Exploratory Data Analysis")
        st.markdown("""
        As already mentioned in the first section of the third chapter of this research project paper, data was not 
        collected independently, but secondary data was used in the empirical part of the study. The dataset used, 
        entitled *“Bank Marketing (with social/economic context)”*, is freely available to secondary researchers in 
        the machine learning repository of the University of California, Irvine (UCI), at the following link: <a href="http://archive.ics.uci.edu/ml/datasets/Bank+Marketing" target="_blank">http://archive.ics.uci.edu/ml/datasets/Bank+Marketing</a>.
        The data basis of the project was collected from a Portuguese bank that used its own contact-center to do 
        directed marketing campaigns. The telephone, with a human agent as the interlocutor, was the dominant marketing 
        channel.
        """, unsafe_allow_html=True)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/target_group_marketing.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 6: Target groups in marketing: Who is the fixed-term deposit suitable for?")
        )
        st.markdown("""
        A fixed-term deposit is an investment with a fixed term in which money is paid into an account at a financial 
        institution. Fixed-term deposits generally have short-term terms of one month to several years and have 
        different minimum deposits. When concluding a fixed-term deposit contract, investors must be aware that they 
        will not be able to access their money again until the contractually agreed term has expired. In some cases, 
        the account holder may allow the investor to terminate - or withdraw - the deposit early if they give several 
        days' notice. There is also a penalty for early cancellation. Fixed-term deposits offer consumers a high degree 
        of planning security, as the interest rates are fixed and guaranteed. It is therefore suitable for customers 
        who prefer a conservative, secure investment to preserve their assets. Fixed-term deposits are suitable for 
        short-term investments, for example if you want to ‘park’ money that you will only need for an investment at 
        a later date. However, you can also use fixed-term deposits to build up assets or as part of your retirement 
        provision. As fixed-term deposits are not affected by price fluctuations, they are a particularly safe form 
        of investment.
       """)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/business_logic.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 7: Presentation of the business logic in the financial services sector with special \n"
                 "emphasis on the three players involved in financial transactions")
        )
        st.markdown("""
        When an account holder deposits money with a bank, the bank can use this money to lend it to other consumers. 
        In return for the right to use these funds to lend, it pays the depositor (or investor) a fee in the form of 
        interest on the account balance. With most deposit accounts of this type, the holder can withdraw their money 
        at any time. This makes it difficult for the bank to know in advance how much it can lend at any given time. 
        To solve this problem, banks offer fixed-term deposit accounts. The interest rate on a fixed-term deposit 
        account is slightly higher than that on a normal savings or interest-bearing current account. When a customer 
        invests money in a fixed-term deposit account, the bank can invest the money in other financial products that 
        yield a higher return than what the bank pays the customer for using their money. The bank can also lend the 
        money to other customers and thus receive a higher interest rate from the borrowers than what the bank pays 
        for the fixed-term deposit.

        For example, a financial institution may offer an interest rate of 2,75 % for fixed-term deposits with a term 
        of one years. The deposited funds can then be made available by the financial institution as loans to borrowers 
        or lenders at an interest rate of 9,45 %. The difference between the interest rate the bank pays its customers 
        for deposits and the interest rate it charges its lenders is known as the net interest margin and is 6,70 % in 
        the example. This interest spread is a very important profitability indicator for banks. In practice, banks face 
        the challenge of finding a balance in the interest spread. If, on the one hand, the interest rate on fixed-term 
        deposits is too low, they will not be able to persuade new investors to sign a contract. On the other hand, banks 
        cannot set their lending rates too high, as otherwise no new borrowers will take out a loan with the bank.
        """)
    elif phase == "Instructions Primary Researcher":
        st.subheader("2. Instructions from the Primary Researcher")
        st.markdown("""
        In the data understanding phase, which should be interpreted as complementary to the business understanding
        phase, the focus is on identifying, collecting and analysing the data sets that can help you achieve the
        project objectives. In this context, the quality of the data must be checked and ensured. This phase also 
        includes the task of describing the data using statistical analyses and determining attributes and their 
        characteristics. This phase also consists of a total of four tasks:
        1.	Collect initial data: Acquire the necessary data and (if necessary) load it into your analysis tool.
        2.	Describe data: Examine the data and document its surface properties like data format, number of records, 
        or field identities.
        3.	Explore data: Dig deeper into the data. Query it, visualize it, and identify relationships among the 
        data.
        4.	Verify data quality: How clean/dirty is the data? Document any quality issues.
        """)
    elif phase == "Data Audit - Client Socio-Economic Attributes":
        st.subheader("3. Data Audit - Client Socio-Economic Attributes")
        st.markdown("""
        In the data understanding phase, which should be interpreted as complementary to the business understanding
        phase, the focus is on identifying, collecting and analysing the data sets that can help you achieve the
        project objectives. In this context, the quality of the data must be checked and ensured. This phase also 
        includes the task of describing the data using statistical analyses and determining attributes and their 
        characteristics. This phase also consists of a total of four tasks:
        1.	Collect initial data: Acquire the necessary data and (if necessary) load it into your analysis tool.
        2.	Describe data: Examine the data and document its surface properties like data format, number of records, 
        or field identities.
        3.	Explore data: Dig deeper into the data. Query it, visualize it, and identify relationships among the 
        data.
        4.	Verify data quality: How clean/dirty is the data? Document any quality issues.
        """)
    elif phase == "Data Audit - Economic Environment":
        st.subheader("4. Data Audit - Economic Environment")
        st.markdown("""
        In the data understanding phase, which should be interpreted as complementary to the business understanding
        phase, the focus is on identifying, collecting and analysing the data sets that can help you achieve the
        project objectives. In this context, the quality of the data must be checked and ensured. This phase also 
        includes the task of describing the data using statistical analyses and determining attributes and their 
        characteristics. This phase also consists of a total of four tasks:
        1.	Collect initial data: Acquire the necessary data and (if necessary) load it into your analysis tool.
        2.	Describe data: Examine the data and document its surface properties like data format, number of records, 
        or field identities.
        3.	Explore data: Dig deeper into the data. Query it, visualize it, and identify relationships among the 
        data.
        4.	Verify data quality: How clean/dirty is the data? Document any quality issues.
        """)
    elif phase == "Data Audit - Current Marketing Activities":
        st.subheader("5. Data Audit - Current Marketing Activities")
        st.markdown("""
        In the data understanding phase, which should be interpreted as complementary to the business understanding
        phase, the focus is on identifying, collecting and analysing the data sets that can help you achieve the
        project objectives. In this context, the quality of the data must be checked and ensured. This phase also 
        includes the task of describing the data using statistical analyses and determining attributes and their 
        characteristics. This phase also consists of a total of four tasks:
        1.	Collect initial data: Acquire the necessary data and (if necessary) load it into your analysis tool.
        2.	Describe data: Examine the data and document its surface properties like data format, number of records, 
        or field identities.
        3.	Explore data: Dig deeper into the data. Query it, visualize it, and identify relationships among the 
        data.
        4.	Verify data quality: How clean/dirty is the data? Document any quality issues.
        """)
