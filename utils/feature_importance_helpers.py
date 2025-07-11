import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from xgboost import XGBClassifier
import seaborn as sns
import numpy as np

from utils.model_pipeline import load_data


def get_preprocessed_training_data():
    """
    Gibt die transformierten Trainingsdaten zurück.

    Returns:
        X_train (pd.DataFrame): Trainingsfeatures
        y_train (pd.Series): Zielvariable
    """
    X_train, _, y_train, _ = load_data()
    return X_train, y_train


def get_fitted_xgboost_model():
    """
    Trainiert ein XGBoost-Modell auf den Trainingsdaten.

    Returns:
        model (XGBClassifier): Trainiertes Modell
    """
    X_train, _, y_train, _ = load_data()
    model = XGBClassifier(
        n_estimators=50,
        objective='binary:logistic',
        use_label_encoder=False,
        eval_metric='logloss'
    )
    model.fit(X_train, y_train)
    return model


def plot_logistic_feature_importance(X_train, y_train, top_n=15):
    """
    Visualisiert die signifikantesten Features (Odds Ratios) einer logistischen Regression.

    Args:
        X_train (pd.DataFrame): Trainingsdaten
        y_train (pd.Series): Zielvariable
        top_n (int): Anzahl der anzuzeigenden Top-Features

    Returns:
        fig (matplotlib.figure.Figure)
    """
    X_const = sm.add_constant(X_train)
    model = sm.Logit(y_train, X_const).fit(disp=False)

    summary = model.summary2().tables[1]
    summary["odds_ratio"] = summary["Coef."].apply(lambda x: round(np.exp(x), 2))
    summary["p_value"] = summary["P>|z|"]

    filtered = summary[(summary["p_value"] < 0.05) & (summary.index != 'const')]
    filtered_sorted = filtered.sort_values("odds_ratio", ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x="odds_ratio",
        y=filtered_sorted.index,
        data=filtered_sorted,
        ax=ax,
        palette="Blues_d"
    )
    ax.set_title("Logistic Regression – Top Feature Odds Ratios (p < 0.05)")
    ax.set_xlabel("Odds Ratio")
    ax.set_ylabel("Feature")
    plt.tight_layout()
    return fig


def plot_xgboost_feature_importance(model, X_train, top_n=15):
    """
    Visualisiert die Feature Importances aus XGBoost (basierend auf .feature_importances_).

    Args:
        model (XGBClassifier): Trainiertes Modell
        X_train (pd.DataFrame): Trainingsdaten
        top_n (int): Anzahl der anzuzeigenden Top-Features

    Returns:
        fig (matplotlib.figure.Figure)
    """
    importances = model.feature_importances_
    importance_df = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(importance_df['Feature'], importance_df['Importance'], color='#191919')
    ax.set_xlabel('Feature Importance')
    ax.set_title('Top Features by Importance (XGBoost)')
    ax.invert_yaxis()
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')
    plt.tight_layout()
    return fig
