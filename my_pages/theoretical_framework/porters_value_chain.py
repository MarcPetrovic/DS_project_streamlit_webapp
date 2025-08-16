import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    st.header("Porter's Value Chain Approach and Cost Optimization")
    st.markdown("""
    The general institutionalization of Porter's value chain approach at the beginning of the 1980s also led 
    to a shift away from traditional sales models in companies. The special feature of Porter's approach is 
    that the division between primary and secondary activities within the value chain and the comparison of 
    these with the margin makes it possible to determine the costs of producing a product or service. Through 
    the practical application of Porter's value chain approach, it has been empirically proven that conventional 
    sales strategies, in which all customers are offered the same sales promotion and at the same time the 
    differences between customers are neglected, are associated with high operating expenses and low monetary 
    benefits.
    """)

    show_github_image(
    image_filename="images/relevance_cvc.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 2: Schematic representation of the costs of the value chain approach with particular \n"
             "emphasis on operating expenses for marketing activities")
    )

    st.markdown("""
    In addition to the process optimization described above, which focused on resource-optimized use, other 
    macroeconomic aspects, such as the creation of new retail relationships and the associated emergence of 
    so-called global markets, increased the pressure between competitors within specific sectors. Ultimately, 
    however, it was digitalization and the option of omnichannel marketing in particular that caused a fundamental 
    break within the corporate culture. Within this new culture, the econo¬mics of customer relationships changed 
    fundamentally and companies implemented new concepts of customer relations. The primary marketing objective 
    changed in the way that the focus was no longer on the cost-intensive expansion of the customer base, but 
    rather on intensifying new business with existing customers (cross-selling and up-selling).
    """)

    show_github_image(
    image_filename="images/marketing_expenses.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 3: Time series analysis of banks' operating expenditure on marketing activities \n"
             "and the correlation between operating expenses and income per bank customer")
    )

    st.markdown("""
    Over the last two decades, the focus of marketing has shifted from the breadth of the customer base to the 
    depth of the needs of individual customers. Today, successful companies are practising the new economics of 
    the customer relationship by being interested in long-term customer relationships when the customer value is 
    in favour. Every interaction with profitable customers is aimed at providing them with a service experience 
    and building and maintaining a direct relationship. The latter primarily serves to gather information about 
    the customer in order to create needs-based product offerings (user-centred product development) and to find 
    the right time to contact the customer (best time to contact).
    
    """)

    show_github_image(
    image_filename="images/corr_ops_income_expenses.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 4: Development of retail banks operating cost per customer (€) \n"
             "between 2022 and 2023")
    )
    st.markdown("""
        <!-- Font Awesome einbinden -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <style>
        #scroll-top-link {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
    
            width: 60px;
            height: 60px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
    
            display: flex;
            align-items: center;
            justify-content: center;
    
            background-color: black;
            color: white;
            text-decoration: none;
            font-size: 24px;
            transition: background-color 0.3s ease, opacity 0.2s ease;
        }
    
        @media (prefers-color-scheme: dark) {
            #scroll-top-link {
                background-color: #222;
                color: white;
            }
        }
    
        @media (prefers-color-scheme: light) {
            #scroll-top-link {
                background-color: #e0e0e0;
                color: black;
            }
        }
    
        /* Optional: Hover-Effekt */
        #scroll-top-link:hover {
            opacity: 0.85;
        }
        </style>
    
        <!-- Button mit Icon -->
        <a href="#top" id="scroll-top-link" title="Top">
            <i class="fas fa-arrow-up"></i>
        </a>
    """, unsafe_allow_html=True)
