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
        Given the previously mentioned business context, the classification task goes beyond statistical accuracy 
        and targets minimization of financial loss. This makes the project a clear example of a cost-sensitive 
        classification problem, where Type I and Type II errors have unequal cost implications:
         - Type I Error (False Positive): Predicting that a customer will subscribe, when in fact they do not.
           This leads to wasted marketing costs, including call center resources and campaign-related expenses.
         - Type II Error (False Negative): Predicting that a customer will not subscribe, when in fact they 
           would have. This results in missed revenue, specifically the lost interest margins the bank would 
           have gained from the customer’s fixed-term deposit. In addition to economic loss, the bank also 
           misses the opportu¬nity to build closer customer relationships or even increase customer loyalty.

        To systematically manage these outcomes, a cost matrix is employed. Using standard loss function 
        notation, the cost matrix L is defined as follows:
         """)
        st.latex(r"""
        L = \begin{pmatrix}
        0 & L_{12} \\
        L_{21} & 0 \\
        \end{pmatrix}
        = 
        \begin{pmatrix}
        0 & 3350 \\
        550 & 0 \\
        \end{pmatrix}
        """)
        st.markdown("""
        where: 
         - L₁₂ = €3,350: Cost of a **false negative** – missed interest revenue  
         - L₂₁ = €550: Cost of a **false positive** – unnecessary marketing expenditure  
         - L₁₁, L₂₂ = €0: Correct predictions (**true positives** and **true negatives**) are assumed 
           to have zero cost.
        """)
        st.markdown("""
        These cost values are derived as follows:
        - **False Positive Cost (Type I)**: Based on data from the Strategy & Retail Banking Monitor 2024 
          (reporting period 2022–2023), the average operational expense per unsuccessful customer contact 
          was estimated at €550.
        - **False Negative Cost (Type II)**: Represents the lost net interest revenue the bank could have 
          earned from a customer who would have signed the contract but was not contacted. This value was 
          derived using.
            - An average interest rate for installment loans of 9.45%, based on 2023 data from the German 
              Bundesbank (Konsumentenkredite an private Haushalte – Ratenkredite).
            - An average interest rate for 12-month fixed-term deposits of 2.75%, based on statistics from 
              tagesgeldvergleich.net (Zinsentwicklung bei Festgeldkonten, 2023).

        This results in a net interest margin (spread) of 6.70%. Assuming an average invested capital of 
        €50,000 per customer, the missed revenue equals:
        """)
        st.latex(r"""
        Revenue_{FN} = €50,000 * 0.067 = €3,350
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
        According to the CRISP-DM methodology, the Business Understanding phase establishes the foundational knowledge 
        necessary for the entire data mining project. This includes clarifying the precise business question, consolidating 
        domain expertise, identifying key stakeholders, understanding data availability and accessibility, and defining the 
        technical environment. Importantly, this phase also involves making early but critical decisions regarding the 
        analytical approach and modeling strategy.
        
        In this project, the modeling methodology is explicitly outlined and aligned with business goals within the Business 
        Understanding phase to ensure a coherent and goal-driven process. The choice of machine learning algorithms and 
        evaluation metrics is not deferred to later phases but carefully considered upfront to reflect the project’s specific 
        requirements and constraints.  
        The modeling approach is structured as a two-iteration process:
         - In the first iteration, a broad set of candidate algorithms – including logistic regression, XGBoost, naive bayes,
           random forest, gradient boosting, and deci¬sion trees – is  assessed. The evaluation metric driving the initial 
           comparison is the mean accuracy score, derived through repeated stratified k-fold cross-validation (5 splits, 
           2 repeats) applied exclusively on the training data. This robust validation framework is chosen to mitigate 
           overfitting risks and account for class imbalances.
        - Selection after this iteration narrows down to two models based on compleme¬ntary criteria
            - A transparent, interpretable model prioritized for ease of explanation to internal stakeholders (e.g., sales 
              teams) and external regulators (e.g., BaFin), thus fostering trust and accountability.
            - A complex, non-linear model retained for benchmarking optimal pre¬dictive performance and exploring potential 
              gains from more sophis¬ticated approaches.
        
        Both models must demonstrate consistent cross-validation performance with minimal discrepancies between 
        training and validation, ensuring generalizability and avoiding overfitting. Accuracy remains a key indicator 
        of discrimination power, but not in isolation.
        - **The second iteration anticipates incorporating feature engineering** informed by exploratory data analysis 
          and success profile insights, aiming to enhance predictive signal extraction. This phase also broadens model 
          assessment beyond accuracy, introducing a comprehensive set of metrics that capture different aspects of 
          classifier quality and business relevance, including:
            - Early Retrieval Area (ERA)
            - False Positive Rate (FPR)
            - False Negative Rate (FNR)
            - Precision
            - Recall (True Positive Rate)
            - F1-Score
            - Cohen’s Kappa
            - Matthews Correlation Coefficient (MCC)
            - Total Cost (€) as a direct translation of misclassification consequences into financial terms
        
        By predefining this methodological framework within the Business Understanding phase, the project aligns its 
        analytical trajectory with business realities and stakehol¬der expectations from the outset. This approach 
        embodies the CRISP-DM philosophy of iterative refinement grounded in domain knowledge, enabling more effective, 
        transparent, and profitable model deployment.
        """)
    elif phase == "Technical Framework & Environment":
        st.subheader("5. Technical implementation framework")
        st.markdown("""
        The implementation of the CRISP-DM process was carried out within a customized technical environment based on the 
        [Anaconda Cloud](https://www.anaconda.com/products/cloud-suite) distribution. Anaconda is specifically tailored for data-intensive computing and offers a robust 
        ecosystem for managing Python packages, with particular advantages in terms of **version control**, **reproducibility**, 
        and **package dependency resolution**.
        
        Due to the use of specific and partially non-standard Python libraries within the project, a **dedicated Conda 
        environment was configured**. This environment was built on **Python 3.9** to ensure compatibility with all required 
        packages. To allow seamless execution within **Jupyter Notebooks**, the environment was explicitly registered as a 
        **Jupyter kernel using the ipykernel package**. This setup facilitated smooth integration of environment-specific 
        packages within the interactive notebook interface.
        
        """)
                # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/technical_environment.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 9: Overview of the main applications and tools, used within the data project")
        )
        st.markdown("""
        For the development and documentation of the data analysis pipeline, the web-based Jupyter Notebook environment was 
        employed. Jupyter enables an interactive, linear execution of code, ideal for the structured realization of all 
        CRISP-DM phases—particularly for data understanding, data preparation, modeling, and evaluation.

        As part of the exploratory data analysis (EDA), the open-source Python package ydata-profiling was used. This tool 
        automates the generation of descriptive statistics, missing value diagnostics, and graphical summaries, thus 
        significantly accelerating the initial data exploration phase and enabling systematic insight into the dataset 
        structure with minimal manual coding effort.

        To facilitate an interactive, user-friendly presentation of the machine learning results, the open-source library 
        Streamlit was employed. Streamlit allows rapid development of lightweight data apps and supports real-time parameter 
        interaction and visualiza¬tion without the need for advanced front-end programming skills.

        Finally, the GitHub platform was used to version, manage, and publish the source code and Streamlit application. GitHub 
        served both as a collaborative development environment and as a medium for publicly sharing the implementation and 
        results in the spirit of open, reproducible science.

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

        - "Yes" → The customer subscribed to the deposit offer (positive class)
        - "No" → The customer declined the offer (negative class)  
        
        This clearly defines the task as a supervised classification problem, with a strong business need to optimize both customer 
        selection and campaign cost.

        **Determine the objectives of data mining and model selection strategy:** In alignment with the business objectives, the 
        following supervised learning algorithms were selected for the first modeling iteration:
        - Logistic Regression
        - K-Nearest Neighbors (KNN)
        - Gradient Boosting Classifier
        - Decision Tree
        - Random Forest
        - Naïve Bayes
        - XGBoost  
        
        The primary selection criterion during this phase was predictive accuracy, estimated through repeated stratified 
        k-fold cross-validation (5 folds, 2 repeats) on the training dataset. To ensure generalizability and mitigate 
        overfitting, models were assessed not only by their mean accuracy but also by consistency across folds.

        **Expanded Evaluation Framework in the Second Modeling Iteration:** In the second iteration, both models were evaluated 
        using classification metrics derived from the confusion matrix, including:
        - **False Positives (Type I Errors)** – Costly due to unnecessary marketing expenditures
        - **False Negatives (Type II Errors)** – Result in missed revenue opportunities
        - **Recall** – Sensitivity to identifying actual subscribers
        - **Precision** – Accuracy of positive predictions
        - **F1-Score** – Harmonic mean of precision and recall  
        
        This expansion beyond mere accuracy was motivated by the cost-sensitive nature of the problem. Each misclassification 
        carries a quantifiable business cost (outlined in Section 3.1.1). The inclusion of financial risk metrics ensures that 
        model deployment aligns not only with statistical performance but also with economic optimization.

        **Conclusion of the Business Understanding Phase:** The decisions made during this phase establish a strong foundation 
        for the subsequent modeling steps. By:
        - Clearly defining the business objective
        - Understanding the financial mechanisms behind fixed-term deposits
        - Identifying the right modeling framework
        - Predefining cost-aware evaluation criteria  
        
        The project ensures that all subsequent phases remain anchored in business relevance and stakeholder value.
        """)
