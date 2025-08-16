# DS_project_streamlit_webapp

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Streamlit-brightgreen)](https://your-streamlit-app-url.streamlit.app)

---

## Project Overview
This project demonstrates the application of the CRISP-DM methodology to a real-world business case. The main focus lies in evaluating classification models under cost-sensitive conditions and optimizing thresholds to balance operational costs and predictive performance. The results highlight how data-driven strategies can support decision-making and resource allocation in a practical context.

---

## Deployment
The application is hosted on Streamlit Cloud and can be accessed directly via the following link:
👉 [**Launch the Streamlit Web App**](https://your-streamlit-app-url.streamlit.app)

---

## Data Source
The analyses are based on publicly available datasets provided as part of the training resources from datascientest.com.

---

## Acknowledgements
Special thanks go to Lucas Varela for his guidance and to datascientest.com as the training provider.

---

## 📂 Repository Structure
```plaintext
├── evaluation.py              # Main evaluation logic with threshold tuning strategies
├── utils/                      # Helper modules for plots, metrics, confusion matrices, etc.
│   ├── plot_helpers.py
│   ├── table_helpers.py
│   ├── image_loader.py
│   └── ...
├── README.md                  # Project documentation (this file)
├── LICENSE                    # License information (MIT)
└── requirements.txt           # Dependencies for Streamlit app
