from utils.model_pipeline import compute_metrics
from utils.compute_metrics import compute_metrics
from utils.find_best_threshold import find_best_threshold

def compare_models_by_threshold_strategy(y_true, logreg_proba, xgb_proba, strategy='f1'):
    best_threshold_logreg = find_best_threshold(y_true, logreg_proba, strategy)
    best_threshold_xgb = find_best_threshold(y_true, xgb_proba, strategy)

    metrics_logreg = compute_metrics(y_true, logreg_proba, best_threshold_logreg)
    metrics_xgb = compute_metrics(y_true, xgb_proba, best_threshold_xgb)

    return metrics_logreg, metrics_xgb
