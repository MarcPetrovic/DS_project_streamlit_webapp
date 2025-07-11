import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

def plot_logistic_feature_importance(X_train, y_train):
    # Statsmodels-Logit-Modell
    X_train_sm = sm.add_constant(X_train)
    model = sm.Logit(y_train, X_train_sm).fit(disp=0)

    # Odds Ratios und Signifikanz
    odds_ratios = np.exp(model.params)
    summary = model.summary2().tables[1]
    summary['Odds Ratio'] = odds_ratios
    significant = summary[(summary['P>|z|'] < 0.05) & (summary.index != 'const')]

    # Transformation & Auswahl Top 10
    significant['Normalized Odds Ratio (%)'] = np.abs((significant['Odds Ratio'] - 1) * 100)
    top_10 = significant.sort_values('Normalized Odds Ratio (%)', ascending=False).head(10)
    colors = ['#097a80' if coef > 0 else '#C00000' for coef in top_10['Coef.']]

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    top_10['Normalized Odds Ratio (%)'].plot(kind='barh', color=colors, ax=ax)
    ax.set_xlabel('Feature Importance (%)')
    ax.set_title('Top Significant Features (Logistic Regression)')
    ax.invert_yaxis()
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')
    return fig

def plot_xgboost_feature_importance(xgb_model, X_train):
    importances = xgb_model.feature_importances_
    importance_df = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False).head(10)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(importance_df['Feature'], importance_df['Importance'], color='#191919')
    ax.set_xlabel('Feature Importance')
    ax.set_title('Top Features by Importance (XGBoost)')
    ax.invert_yaxis()
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')
    return fig
