import streamlit as st

def show():
    st.header("Brief introduction to CRISP-DM")
    # Checkbox: Text soll standardmäßig angezeigt werden
    if st.checkbox("🧠 Show/hide introduction text", value=True):
        st.markdown("""
        The CRISP-DM data mining methodology is an industry-independent hierarchical process model consisting 
        of task sets described at four levels of abstraction (from general to specific): Phase, General Tasks, 
        Specialized Activities and Process Instance. Every of the six iterative phases stands for a general 
        and generic task, following its own specialized tasks and actions in order to generate a special output 
        on a procedural instance. At the top level, the data mining process is organized into a series of six 
        phases; each phase consists of several generic tasks at the second level. This second level is called 
        generic because it should be general enough to cover all possible data mining situations. The third 
        level, the level of specialized activities, describes in detail how actions in the generic tasks should 
        be carried out in certain specific situations. For example, a generic tasks called “Clean data” could 
        be placed on the second level. The third level describes how these specific tasks differ in different 
        situations, e.g. cleaning numerical values versus cleaning categorical values or whether the problem 
        type is clustering or predictive modelling. The fourth level, the process instance, is a record of the 
        actions, decisions and results of an actual data mining operation and is structured according to the 
        tasks defined at the higher levels. The description of phases and tasks as discrete steps that are 
        performed in a specific order represents an idealized sequence of events. In practice, many of the 
        tasks can be performed in a slightly varying and incremental sequence. 
        """)
    st.markdown("""
    In the following, we will take a closer look at the first two levels of abstraction - phases and their 
    general tasks. This is necessary to provide a theoretical foundation for practical implementation, which 
    is described in particular in the third chapter.
    """)
    
    # Dropdown für die Phasen
    phase = st.selectbox("Select a CRISP-DM-phase:", [
        "Business Understanding",
        "Data Understanding",
        "Data Preparation",
        "Modeling",
        "Evaluation",
        "Deployment"
    ])
    # Inhalte je nach Auswahl
    if phase == "Business Understanding":
        st.subheader("1. Business Understanding")
        st.markdown("""
        The Business Understanding phase focuses on understanding the objectives and requirements of the project.
        Aside from the third general task, the three other tasks in this phase are foundational project management
        activities:
        1.	Define the business objectives: Based on a deep understanding of the business customer perspective, 
        the business success criteria can then be determined.
        2.	Assessment of the situation in the business environment: What (technical and financial) resources are 
        available, what requirements are placed on the project, what costs are associated with what returns 
        and what risks can be calculated.
        3.	Determine the objectives of data mining: In addition to defining the business objectives, the type of 
        data mining should be explained (e.g. classification) and, based on this, the success criteria of data 
        mining (e.g. accuracy) must be derived.
        4.	Produce project plan: Select technologies and tools and define detailed plans for each project phase.
       """)
    elif phase == "Data Understanding":
        st.subheader("2. Data Understanding")
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

    elif phase == "Data Preparation":
        st.subheader("3. Data Preparation")
        st.markdown("""
        Data should be selected by defining inclusion and exclusion criteria. Poor data quality can be remedied by 
        cleansing the data. Depending on the model used (which was defined in the first phase), derived attributes 
        must be constructed. Different methods are possible for all these steps, depending on the model. A general 
        rule of thumb is that 80% of the data project is spent on data preparation. This phase, often referred to 
        as ‘data preparation’, prepares the final dataset(s) for modelling. It consists of five tasks:
        1.	Select data: Determine which data sets will be used and document reasons for inclusion/exclusion.
        2.	Clean data: Often this is the lengthiest task. Without it, you’ll likely fall victim to garbage-in, 
        garbage-out. A common practice during this task is to correct, impute, or remove erroneous values.
        3.	Construct data: Derive new attributes that will be helpful. For example, derive someone’s body mass index 
        from height and weight fields.
        4.	Integrate data: Create new data sets by combining data from multiple sources.
        5.	Format data: Re-format data as necessary. For example, you might convert string values that store numbers 
        to numeric values so that you can perform mathematical operations.
        """)

    elif phase == "Modeling":
        st.subheader("4. Modeling")
        st.markdown("""
        The data modelling phase consists of selecting the modelling technique, building the test case and the model. 
        In general, the choice of data mining technique depends on the business problem and the data. More important, 
        however, is how to justify the choice. Certain parameters must be defined for the creation of the model. For 
        the evaluation of the model, it is appropriate to assess the model based on evaluation criteria and select 
        the best ones. This phase consists of three tasks:
        1.	Select modeling techniques: Determine which algorithms to try (e.g. regression, classification).
        2.	Generate test design: Pending your modeling approach, you might need to split the data into training, test, 
        and validation sets.
        3.	Build and assess model: Generally, multiple models are competing against each other, and the data scientist 
        needs to interpret the model results based on domain knowledge, the pre-defined success criteria, and the 
        test design.
        """)

    elif phase == "Evaluation":
        st.subheader("5. Evaluation")
        st.markdown("""
        In the evaluation phase, the results are compared with the defined business objectives. The results must 
        therefore be interpreted and further measures defined. While the ‘Build and Assess Model’ task in the modelling 
        phase focuses on the technical assessment of the model, the evaluation phase deals with the question of which 
        model is best suited for the company and what to do next. This phase consists of three tasks:
        1.	Evaluate results: Do the models meet the business success criteria? Which one(s) should we approve for the 
        business?
        2.	Review process: Review the work accomplished and for example ask yourself: “Was anything overlooked?”, 
        “Were all steps properly executed?” Last but not least: Summarize findings and correct anything if needed.
        3.	Determine next steps: Based on the previous tasks, determine whether to proceed to deployment, iterate further, 
        or initiate new projects.
        """)

    elif phase == "Deployment":
        st.subheader("6. Deployment")
        st.markdown("""
        Depending on the requirements, the deployment phase could be a final report or a software component. This final 
        phase has four general tasks:
        1.	Plan deployment: Develop and document a plan for deploying the model
        2.	Plan monitoring and maintenance: Develop a thorough monitoring and maintenance plan to avoid issues during 
        the operational phase (or post-project phase) of a model
        3.	Produce final report: The project team documents a summary of the project which might include a final 
        presentation of data mining results.
        4.	Review project: Conduct a project retrospective about what went well, what could have been better, and 
        how to improve in the future.
        """)
