import streamlit as st

def show():
    st.header("Brief introduction to CRISP-DM")
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

    In the following, we will take a closer look at the first two levels of abstraction - phases and their 
    general tasks. This is necessary to provide a theoretical foundation for practical implementation, which 
    is described in particular in the third chapter.

    ## Business Understanding
    The Business Understanding phase focuses on understanding the objectives and requirements of the project. 
    Aside from the third general task, the three other tasks in this phase are foundational project management 
    activities:

    """)
