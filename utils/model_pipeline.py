import pandas as pd
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from utils.data_loader import load_csv_data  # Pfad ggf. anpassen

def load_data():
    """
    Lädt Trainings- und Testdaten aus CSV-Dateien im data-Ordner.
    
    Returns:
        X_train, X_test, y_train, y_test: Als Pandas DataFrames/Series
    """
    X_train = load_csv_data("data/X_train_transformed2nd.csv", ignore_index_column=False).squeeze()
    X_test = load_csv_data("data/X_test_transformed2nd.csv", ignore_index_column=False).squeeze()
    y_train = load_csv_data("data/y_train.csv", ignore_index_column=True).squeeze()
    y_test = load_csv_data("data/y_test.csv", ignore_index_column=True).squeeze()

    return X_train, X_test, y_train, y_test


def train_and_predict(model_type='logistic'):
    """
    Lädt Daten, trainiert ein Klassifikationsmodell und gibt die Wahrscheinlichkeiten für X_test zurück.

    Args:
        model_type (str): 'logistic' oder 'xgboost'

    Returns:
        model: Das trainierte Modell
        y_proba: Die Vorhersagewahrscheinlichkeiten auf dem Testset (nur Klasse 1)
        y_test: Die echten Labels
    """
    # 1. Daten laden
    X_train, X_test, y_train, y_test = load_data()

    # 2. Modell wählen
    if model_type == 'logistic':
        model = LogisticRegression(max_iter=1000, solver='sag', random_state=42)
    elif model_type == 'xgboost':
        model = XGBClassifier(n_estimators=50, objective='binary:logistic',use_label_encoder=False, eval_metric='logloss', random_state=42)
    else:
        raise ValueError("Ungültiger Modelltyp. Wähle 'logistic' oder 'xgboost'.")

    # 3. Modell trainieren
    model.fit(X_train, y_train)

    # 4. Vorhersagewahrscheinlichkeiten berechnen (nur Klasse 1)
    y_proba = model.predict_proba(X_test)[:, 1]

    return model, y_proba, y_test
