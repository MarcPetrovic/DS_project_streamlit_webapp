from sklearn.metrics import f1_score, precision_recall_curve, roc_curve
import numpy as np

def find_best_threshold(y_true, y_proba, strategy='f1', cost_function=None):
    """
    Findet den optimalen Threshold basierend auf der gewählten Strategie.

    Args:
        y_true (array-like): Wahre Labels.
        y_proba (array-like): Vorhersagewahrscheinlichkeiten (z. B. predict_proba[:, 1]).
        strategy (str): 'f1', 'cost', 'youden', 'pr_gap', 'default'.
        cost_function (callable, optional): Muss übergeben werden, wenn strategy='cost'.

    Returns:
        float: Der optimale Threshold.
    """
    if strategy == 'f1':
        precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
        thresholds = np.append(thresholds, 1.0)  # Längenangleichung
        f1_scores = 2 * (precision * recall) / (precision + recall + 1e-6)
        best_idx = np.argmax(f1_scores)
        return thresholds[best_idx]
    
    elif strategy == 'cost':
        if cost_function is None:
            raise ValueError("Für strategy='cost' muss cost_function übergeben werden.")
        thresholds = np.linspace(0, 1, 200)
        costs = [cost_function(y_true, (y_proba >= t).astype(int)) for t in thresholds]
        return thresholds[np.argmin(costs)]
    
    elif strategy == 'youden':
        fpr, tpr, thresholds = roc_curve(y_true, y_proba)
        youden_index = tpr - fpr
        best_idx = np.argmax(youden_index)
        return thresholds[best_idx]

    elif strategy == 'pr_gap':
        precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
        thresholds = np.append(thresholds, 1.0)
        diff = np.abs(precision - recall)
        best_idx = np.argmin(diff)
        return thresholds[best_idx]

    elif strategy == 'default':
        return 0.5

    else:
        raise ValueError(f"Unbekannte Strategie: {strategy}")
