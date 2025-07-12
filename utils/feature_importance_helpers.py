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

def plot_logistic_feature_importance(model, X_train, y_train, top_n=10):
    """
    Visualisiert die signifikanten Features einer logistischen Regression
    basierend auf transformierten Odds Ratios in Prozent.

    Args:
        model: Platzhalter für Konsistenz (nicht verwendet)
        X_train (pd.DataFrame): Trainingsdaten
        y_train (pd.Series): Zielvariable (0/1)
        top_n (int): Anzahl der Top-Features

    Returns:
        fig (matplotlib.figure.Figure): Feature Importance Plot
    """
    import statsmodels.api as sm
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Sicherstellen, dass X_train numerisch ist
    X_train = X_train.astype("float64")
    X_const = sm.add_constant(X_train)

    # Modell fitten mit y_train (nicht mit model.predict!)
    model_sm = sm.Logit(endog=y_train, exog=X_const)
    result = model_sm.fit(disp=False)

    # Odds Ratios
    odds_ratios = np.exp(result.params)
    summary = result.summary2().tables[1]
    odds_ratio_df = pd.DataFrame({'Odds Ratio': odds_ratios})
    combined_summary = summary.join(odds_ratio_df)

    # Signifikante Features
    significant_features = combined_summary[
        (combined_summary['P>|z|'] < 0.05) & (combined_summary.index != 'const')
    ]

    # Normalisieren
    significant_features['Normalized Odds Ratio (%)'] = np.abs((significant_features['Odds Ratio'] - 1) * 100)

    # Top-N Auswahl
    top_features = significant_features.sort_values('Normalized Odds Ratio (%)', ascending=False).head(top_n)
    colors = ['#097a80' if coef > 0 else '#C00000' for coef in top_features['Coef.']]

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_features.index, top_features['Normalized Odds Ratio (%)'], color=colors)
    ax.set_xlabel('Effect Size (%)')
    ax.set_title('Top Significant Features (Logistic Regression)')
    ax.invert_yaxis()
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')
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
