# DS_project_streamlit_webapp

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Streamlit-brightgreen)](https://your-streamlit-app-url.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python) 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

---

## Project Overview
This project demonstrates the application of the CRISP-DM methodology to a real-world business case. The main focus lies in evaluating classification models under cost-sensitive conditions and optimizing thresholds to balance operational costs and predictive performance. The results highlight how data-driven strategies can support decision-making and resource allocation in a practical context.

---

## Deployment
The application is hosted on Streamlit Cloud and can be accessed directly via the following link:
👉 [**Launch the Streamlit Web App**](https://dsproject-crispdm-bank-campaign-cost-optimizer.streamlit.app)

---

## Data Source
The analyses are based on publicly available datasets entitled “Bank Marketing (with social/economic context)”, it is freely available to secondary researchers in the machine learning repository of the University of California, Irvine (UCI), at the following link: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing

---

## Acknowledgements
Special thanks go to Lucas Varela for his guidance and to datascientest.com as the training provider of this project.

---

## Repository Structure
```plaintext
├── data/                          # csv files of primary researcher
│   ├── bank-additional-full.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── ...
├── images/                        # pngs for design uplift of the web application
│   ├── 1st_iteration_modeling.PNG
│   ├── 2nd_iteration_modeling.PNG
│   ├── alternative_thresholding_strategies.PNG
│   └── ...
├── My_pages/                      # py files for navigation and content of web application
│   ├── practical_application/
|   │   ├── business_understanding.py
|   │   ├── data_preparation.py
|   │   ├── data_understanding.py
|   │   ├── evaluation.py
|   │   └── modeling.py
│   ├── theoretical_framework/
|   │   ├── introduction_crisp_dm.py
|   │   ├── porters_value_chain.py
|   │   ├── relevance_data_mining.py
|   │   └── supervised_learning.py
│   ├── about_project.py
│   ├── bibliography.py
│   ├── conclusion_duiscussion.py
│   ├── introduction.py
│   ├── methods_data.py
│   ├── practical_application_crisp_dm.py
│   └── theoretical_framework_overview.py
├── utils/                         # Helper modules for plots, metrics, confusion matrices, etc.
│   ├── compare_models.py
│   ├── compute_metrics.py
│   ├── cost_cal.py
│   └── ...
├── README.md                      # Project documentation (this file)
├── LICENSE                        # License information (MIT)
├── requirements.txt               # Dependencies for Streamlit app
├── app.py                         # Navigation for Streamlit app
└── spa_config.py                  # Configuration py for drop down menue within success profile analysis
