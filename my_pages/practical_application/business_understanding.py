import streamlit as st
from utils.image_loader import show_github_image

def show():
  # Dropdown für die Phasen
    phase = st.selectbox("Select a subchapter of CRISP-DM-phase Business Understanding:", [
        "General Business Knowledge",
        "Cost-optimized Assesment Metrics",
        "Alternative Thresholding Strategies",
        "Methodical Decisions for Modeling",
        "Technical Framework & Environment",
        "Key Results & Strategic Modeling Decisions"
    ])
    # Inhalte je nach Auswahl
    if phase == "General Business Knowledge":
        st.subheader("1. General business knowledge")
        st.markdown("""
        In the following, a well-founded understanding of the business process of investing term deposits at banks 
        will be conveyed. Without this expertise, it is not possible to use data and technology effectively and 
        efficiently to achieve the project goal. At its core, the current data project is about helping banks to 
        improve their marketing efforts by reducing costs and saving resources such as call center agents. It is 
        a classification problem involving the prediction of contract signings of term deposits. In general, a 
        marketing campaign represents the stimulus, and in the context of this project, the stimulus is represented 
        by a specific call from an internal bank call center agent. The stimulus is concrete in the context of the 
        call: This is an offer of a specific fixed-term deposit contract with interest rates above the market average. 
        The response side is represented by a bank customer and his reaction to the agent's call respectively to the 
        offer. The recorded reaction of the bank customer is binary and distinguishes between “Yes”, conclusion of 
        a fixed-term deposit contract, or “No”, no conclusion of a fixed-term deposit contract.
       """)
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
    elif phase == "Cost-optimized Assesment Metrics":
        st.subheader("2. Cost-optimized assesment metrics for a cost-sensitive classification problem")
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
    elif phase == "Alternative Thresholding Strategies":
        st.subheader("3. Alternative Thresholding Strategies")
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
    elif phase == "Methodical Decisions for Modeling":
        st.subheader("4. Methodical decisions for modeling within the business undestanding phases")
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
    elif phase == "Technical Framework & Environment":
        st.subheader("5. Technical implementation framework")
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
    elif phase == "Key Results & Strategic Modeling Decisions":
        st.subheader("6. Key results and strategic modeling decisions")
        st.markdown("""
        This section summarizes the essential business goals, contextual conditions, and methodical decisions made 
        during the Business Understanding phase of the CRISP-DM process.
        
        **Definition of the business objective:** The overarching goal of the project is to develop a binary classification 
        model to predict customer responsiveness to outbound telemarketing campaigns for fixed-term deposit products. 
        By targeting only customers with a high predicted likelihood of accepting an investment offer, the bank can 
        improve its marketing efficiency, reduce unnecessary expenditures, and maximize the return on campaign investments.

        **Assessment of the situation in the business environment:** The data originates from a Portuguese financial institution 
        that conducts regular marketing campaigns via its internal call center. These campaigns are specifically designed to 
        promote interest-bearing fixed-term deposit contracts to existing customers. The stimulus in this case is a telephone-based 
        product offer, and the response is represented by a binary outcome:
        
        •	"Yes" → The customer subscribed to the deposit offer (positive class)
                •	"No" → The customer declined the offer (negative class)
        
        This clearly defines the task as a supervised classification problem, with a strong business need to optimize both customer 
        selection and campaign cost.

        **Determine the objectives of data mining and model selection strategy:** In alignment with the business objectives, the 
        following supervised learning algorithms were selected for the first modeling iteration:
        
        •	Logistic Regression
        •	K-Nearest Neighbors (KNN)
        •	Gradient Boosting Classifier
        •	Decision Tree
        •	Random Forest
        •	Naïve Bayes
        •	XGBoostThe 
        
        The primary selection criterion during this phase was predictive accuracy, estimated through repeated stratified 
        k-fold cross-validation (5 folds, 2 repeats) on the training dataset. To ensure generalizability and mitigate 
        overfitting, models were assessed not only by their mean accuracy but also by consistency across folds.

        **Expanded Evaluation Framework in the Second Modeling Iteration:** In the second iteration, both models were evaluated 
        using classification metrics derived from the confusion matrix, including:
        
        •	False Positives (Type I Errors) – Costly due to unnecessary marketing expenditures
        •	False Negatives (Type II Errors) – Result in missed revenue opportunities
        •	Recall – Sensitivity to identifying actual subscribers
        •	Precision – Accuracy of positive predictions
        •	F1-Score – Harmonic mean of precision and recall
        
        This expansion beyond mere accuracy was motivated by the cost-sensitive nature of the problem. Each misclassification 
        carries a quantifiable business cost (outlined in Section 3.1.1). The inclusion of financial risk metrics ensures that 
        model deployment aligns not only with statistical performance but also with economic optimization.

        **Conclusion of the Business Understanding Phase:** The decisions made during this phase establish a strong foundation 
        for the subsequent modeling steps. By:
        
        •	clearly defining the business objective,
        •	understanding the financial mechanisms behind fixed-term deposits,
        •	identifying the right modeling framework,
        •	and predefining cost-aware evaluation criteria
        
        The project ensures that all subsequent phases remain anchored in business relevance and stakeholder value.
        """)
