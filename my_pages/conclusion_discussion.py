import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_csv_data
from utils.my_colormaps import my_cmap_r, cmap_4, my_cmap

from utils.model_pipeline import *
from utils.find_best_threshold import find_best_threshold
from utils.cost_calc import calculate_cost
from utils.decile_roi import decile_roi_analysis
from utils.plot_roi_lift_combined import plot_decile_lift_roi

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    st.header("Conclusion & Prospect")
    #st.write("Hier formulierst du deine Schlussfolgerungen und Diskussion.")
    st.markdown("""
    The present study has demonstrated convincingly that the application of a well-founded scientific, methodological, and technical 
    framework—combined with a realistic use case from the banking sector—provides an effective foundation for developing data-driven 
    decision models in marketing. In particular, the strict orientation toward business-relevant performance indicators, the structured 
    implementation along the CRISP-DM process model, and the technical execution within a modern development environment have made it 
    possible to derive efficient and operationally applicable classification models from complex datasets.

    At the same time, the study also reveals limitations of both conceptual and infrastructural nature, which should be seen as a 
    starting point for future research and enhancement.

    First and foremost, methodological limitations within the CRISP-DM framework must be acknowledged. Although the project was 
    systematically conducted along the CRISP-DM structure, the final phase—deployment—could not be fully operationalized. Since no 
    production-ready target system was available for the practical use of the model, a technical platform to integrate the predictive 
    model into existing business processes was lacking. As a result, no implementation roadmap could be outlined, nor was a systematic 
    feature and model monitoring established (e.g., using information value, stability or population shift indices). Important aspects 
    such as retraining strategies and automation processes were likewise excluded from the scope of this project.

    """)
        # Daten & Modelle laden (einmal, mit Caching)
    @st.cache_resource
    def get_predictions():
        _, logreg_probs, y_test = train_and_predict(model_type="logistic")
        _, xgb_probs, _ = train_and_predict(model_type="xgboost")
        return logreg_probs, xgb_probs, y_test

    @st.cache_resource
    def get_model_fit():
        logreg_model, X_train, X_test, y_train, y_test = train_model(model_type="logistic")
        xgb_model, _, _, _, _ = train_model(model_type="xgboost")
        return logreg_model, xgb_model, X_train, y_train
    # === Funktion zur Berechnung der IV-Werte pro Decile ===
    def calculate_iv_by_decile(y_true, y_prob, bins=10):
        df = pd.DataFrame({'y_true': y_true, 'y_prob': y_prob})
        df['decile'] = pd.qcut(df['y_prob'], bins, labels=False, duplicates='drop')
    
        # Sortiere Deciles von 10 (höchste Score) bis 1 (niedrigste)
        df['decile'] = bins - df['decile']
    
        total_goods = (df['y_true'] == 1).sum()
        total_bads = (df['y_true'] == 0).sum()
    
        summary = df.groupby('decile').agg(
            good=('y_true', lambda x: (x == 1).sum()),
            bad=('y_true', lambda x: (x == 0).sum())
        ).sort_index(ascending=False)
    
        summary['%Goods'] = summary['good'] / total_goods
        summary['%Bads'] = summary['bad'] / total_bads
        summary['IV'] = (summary['%Goods'] - summary['%Bads']) * np.log((summary['%Goods'] + 1e-6) / (summary['%Bads'] + 1e-6))
    
        return summary.reset_index()

    # === Funktion zur Visualisierung ===
    def plot_dual_iv_chart(train_df, test_df, model_name):
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
    
       # Farben festlegen basierend auf Modellname
        if model_name.lower() == "logistic regression":
            color = '#097a80'  # Türkis
        elif model_name.lower() == "xgboost":
            color = '#191919'  # Dunkelgrau
        else:
            color = '#888888'  # Fallback
    
        # Plot Train
        axes[0].bar(train_df['decile'], train_df['IV'], color=color)
        axes[0].set_title(f'{model_name} – Train Set', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Decile')
        axes[0].set_ylabel('IV Contribution')
        axes[0].grid(True, linestyle='--', alpha=0.5)
        axes[0].set_facecolor('lightgrey')
        axes[0].tick_params(axis='x', labelrotation=0)
        axes[0].set_xticks(range(1, 11))
    
        # Plot Test
        axes[1].bar(test_df['decile'], test_df['IV'], color=color)
        axes[1].set_title(f'{model_name} – Test Set', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Decile')
        axes[1].grid(True, linestyle='--', alpha=0.5)
        axes[1].set_facecolor('lightgrey')
        axes[1].tick_params(axis='x', labelrotation=0)
        axes[1].set_xticks(range(1, 11))
  
        # Hintergrund
        fig.patch.set_facecolor('white')
        st.pyplot(fig)
    
    # === Main Streamlit Logik ===
    st.subheader("Information Value (IV) per Decile – Train vs. Test")
    
    logreg_model, xgb_model, X_train, y_train = get_model_fit()
    _, logreg_probs, y_test = train_and_predict(model_type="logistic")
    _, xgb_probs, _ = train_and_predict(model_type="xgboost")
    
    # Wahrscheinlichkeiten für Training berechnen
    logreg_probs_train = logreg_model.predict_proba(X_train)[:, 1]
    xgb_probs_train = xgb_model.predict_proba(X_train)[:, 1]
    
    # IV berechnen
    logreg_train_iv = calculate_iv_by_decile(y_train, logreg_probs_train)
    logreg_test_iv = calculate_iv_by_decile(y_test, logreg_probs)
    
    xgb_train_iv = calculate_iv_by_decile(y_train, xgb_probs_train)
    xgb_test_iv = calculate_iv_by_decile(y_test, xgb_probs)
    
    # Charts anzeigen
    plot_dual_iv_chart(logreg_train_iv, logreg_test_iv, model_name="Logistic Regression")
    plot_dual_iv_chart(xgb_train_iv, xgb_test_iv, model_name="XGBoost")

    def get_iv_table(y_true, y_prob, model_name, dataset_label, bins=10):
        df = pd.DataFrame({'y_true': y_true, 'y_prob': y_prob})
        df['decile'] = pd.qcut(df['y_prob'], bins, labels=False, duplicates='drop')
        df['decile'] = bins - df['decile']  # Deciles absteigend sortieren
    
        total_goods = (df['y_true'] == 1).sum()
        total_bads = (df['y_true'] == 0).sum()
    
        grouped = df.groupby('decile').agg(
            Count=('y_true', 'count'),
            Goods=('y_true', lambda x: (x == 1).sum()),
            Bads=('y_true', lambda x: (x == 0).sum())
        ).reset_index()

        grouped['%Goods'] = grouped['Goods'] / total_goods
        grouped['%Bads'] = grouped['Bads'] / total_bads
        grouped['IV'] = (grouped['%Goods'] - grouped['%Bads']) * np.log((grouped['%Goods'] + 1e-6) / (grouped['%Bads'] + 1e-6))
        grouped['Cumulative IV'] = grouped['IV'].cumsum()
    
        grouped.insert(0, "Dataset", dataset_label)
        grouped.insert(0, "Model", model_name)
    
        return grouped.round(4)
        
    # 📊 IV-Tabellen für alle 4 Kombinationen
    logreg_train_table = get_iv_table(y_train, logreg_probs_train, model_name="Logistic Regression", dataset_label="Train")
    logreg_test_table  = get_iv_table(y_test, logreg_probs, model_name="Logistic Regression", dataset_label="Test")
    xgb_train_table    = get_iv_table(y_train, xgb_probs_train, model_name="XGBoost", dataset_label="Train")
    xgb_test_table     = get_iv_table(y_test, xgb_probs, model_name="XGBoost", dataset_label="Test")
    
    # 👉 Zusammenführen
    iv_summary_table = pd.concat([logreg_train_table, logreg_test_table, xgb_train_table, xgb_test_table], ignore_index=True)

    if st.checkbox("📊 Show IV-Table", value=False):
        # 🎨 Anzeige in Streamlit
        st.subheader("📋 IV Contribution Table by Decile")
        st.dataframe(iv_summary_table.style.format({
            "%Goods": "{:.2%}",
            "%Bads": "{:.2%}",
            "IV": "{:.3f}",
            "Cumulative IV": "{:.3f}"
        }))

    st.markdown("""
    A key insight of this study was the monetization of model errors (false positives and false negatives) through the integration of 
    business-relevant cost parameters. However, the evaluation focused solely on the cost dimension (operational and opportunity costs), 
    thereby introducing economic limitations to the overall model analysis. A more comprehensive profitability assessment—e.g., through 
    the inclusion of actual revenue, contribution margins, or profit figures—was not performed. Similarly, financial ratios such as Return 
    on Investment (ROI) or Cost-to-Revenue Ratio (CRR) were not incorporated into a weighted cost function that considers true positives, 
    limiting the full realization of the campaign’s economic potential. Future analyses should therefore aim for a multidimensional 
    evaluation framework that includes all four components of the confusion matrix (TP, FP, TN, FN).

    """)
    strategy = st.selectbox(
        "Select threshold tuning strategy",
        options=["f1", "cost", "youden", "pr_gap", "default", "manual"],
        index=0
    )
    
    # Manuelle Schwelle
    if strategy == "manual":
        threshold = st.slider("Select threshold", 0.0, 1.0, 0.5, step=0.01)
        threshold_logreg = threshold
        threshold_xgb = threshold
    else:
        kwargs = {"cost_function": calculate_cost} if strategy == "cost" else {}
        threshold_logreg = find_best_threshold(y_test, logreg_probs, strategy=strategy, **kwargs)
        threshold_xgb = find_best_threshold(y_test, xgb_probs, strategy=strategy, **kwargs)
    
    df_logreg = decile_roi_analysis(
        y_true=y_test,
        y_probs=logreg_probs,
        threshold=threshold_logreg,
        model_name="Logistic Regression"
    )
    
    df_xgb = decile_roi_analysis(
        y_true=y_test,
        y_probs=xgb_probs,
        threshold=threshold_xgb,
        model_name="XGBoost"
    )
    fig_roi_lift = plot_decile_lift_roi(df_logreg, df_xgb)
    st.subheader("Lift and ROI per Decile")
    st.pyplot(fig_roi_lift)
    
    st.markdown("""
    Finally, several statistical and methodological extensions were deliberately omitted to first ensure a robust analytical baseline model. 
    Nevertheless, many advanced techniques that are common in industrial applications were not considered. These include methods for class 
    rebalancing (e.g., SMOTE or reweighting), feature engineering based on Weight of Evidence, or statistical bootstrapping to iteratively 
    select relevant variables. Likewise, dimensionality reduction techniques (e.g., clustering or principal component analysis) were not 
    applied. Although decile analysis was conducted to support campaign prioritization, explicit rating classes were not defined, which would 
    have enabled targeted selection under resource constraints. Additionally, more advanced techniques for handling missing values (e.g., multiple 
    imputation) and an out-of-time validation to ensure model stability over time would have been desirable.

    """)
    
    df = load_csv_data(
        filename="data/bank-additional-full.csv",
        sep=";",
        header=True,
        add_row_id=True,
        ignore_index_column=False
    )
    
    # Jahr zuordnen anhand von ROW_ID
    df_view = (
        df.groupby(["month", "cons.price.idx"], as_index=False)
        .agg(COUNT_TOTAL_PER_MONTH=("month", "count"), MAX_RN_month=("ROW_ID", "max"))
    )
    df_view["year"] = df_view["MAX_RN_month"].apply(
        lambda x: 2008 if x <= 27690 else (2009 if x <= 39130 else 2010)
    )
    df = df.merge(
        df_view[["month", "cons.price.idx", "year"]],
        on=["month", "cons.price.idx"],
        how="left"
    )

    df["date_period"] = pd.to_datetime(
        df["year"].astype(str) + "-" +
        pd.to_datetime(df["month"], format="%b").dt.month.astype(str),
        format="%Y-%m"
    ).dt.to_period("M")
    df["date_int"] = df["date_period"].dt.strftime('%Y%m').astype(int)
    df["date_period"] = df["date_period"].astype(str)

    # 👉 AGGREGATION FÜR ZEITREIHENPLOT
    df["target"] = df["y"].apply(lambda x: 0 if x == "no" else 1)
    df["BASIS"] = 1

    df_plot_view = (
        df.groupby("date_period")
          .agg(Target=("target", "sum"), Basis=("BASIS", "sum"))
          .reset_index()
    )
    df_plot_view["Success_Ratio"] = df_plot_view["Target"] / df_plot_view["Basis"]
    df_plot_view.sort_values("date_period", inplace=True)

    # Titel und Beschreibung
    st.subheader("Subscription Success Rate Over Time")
    st.markdown("""
    This time series shows the monthly success rate of term deposit subscriptions based on the bank’s marketing campaigns. The red line illustrates the 
    success rate of term deposit subscriptions, while the blue bars represent total campaign contacts.
    """)
    
 # Deine Farbvorgaben
    line_color = "#C00000"      # für Success Ratio
    bar_color = "#097a80"       # für Kontaktanzahl
    bg_color = "white"
    area_color = "lightgrey"
    label_color = "black"
    
    # 🎯 Sicherstellen, dass Success Ratio in Prozent ist
    df_plot_view["Success_Ratio"] = df_plot_view["Success_Ratio"] * 100
    
   # 📊 Plot erzeugen
    fig, ax1 = plt.subplots(figsize=(14, 5))
    ax1.set_facecolor(area_color)
    fig.patch.set_facecolor(bg_color)

    # 🟦 Säulen auf linker Y-Achse
    bars = ax1.bar(
        df_plot_view["date_period"],
        df_plot_view["Basis"],
        color=bar_color,
        label="Total Contacts",
        alpha=0.85,
        zorder=1
    )
    ax1.set_ylabel("Total Contacts", color=label_color)
    ax1.tick_params(axis='y', labelcolor=label_color)
    ax1.set_xlabel("Date (Month)", color=label_color)
    ax1.tick_params(axis='x', rotation=45, labelcolor=label_color)

    # 🔴 Linie auf rechter Y-Achse
    ax2 = ax1.twinx()
    line = ax2.plot(
        df_plot_view["date_period"],
        df_plot_view["Success_Ratio"],
        color=line_color,
        marker='o',
        linestyle='--',
        linewidth=2.2,
        label="Success Ratio (%)",
        zorder=2  # Linie vor die Säulen
    )
    ax2.set_ylabel("Success Ratio (%)", color=label_color)
    ax2.tick_params(axis='y', labelcolor=label_color)
    ax2.set_ylim([0, 100])

    # 🗂️ Legende manuell zusammenführen
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    # 🧾 Titel & Layout
    plt.title("Success Ratio and Contact Volume Over Time", fontsize=14, fontweight='bold', color=label_color)
    ax1.grid(True, linestyle='--', color='grey', alpha=0.6)
    plt.tight_layout()    
    # 📌 Streamlit-Ausgabe
    st.pyplot(fig)
    
    st.subheader("Prospect")
    st.markdown("""
    Despite these limitations, the present study provides a sound and practical basis for the structured development of response models in 
    banking-related marketing and clearly highlights the value of data-driven decision-making for strategic marketing processes. Future projects 
    should particularly focus on the complete operationalization of all CRISP-DM phases, the integration of financial performance measures such 
    as ROI and profit, and the application of more sophisticated statistical methodologies to further improve the transferability of such models 
    into real-world business operations. The combination of data-centric thinking, economic grounding, and scalable technical design remains the 
    key success factor.

    """)
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
