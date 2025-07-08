#from utils.model_pipeline import train_and_predict
from utils.compute_metrics import compute_metrics
from utils.find_best_threshold import find_best_threshold
from utils.cost_calc import calculate_cost

def compare_models_by_threshold_strategy(y_true, logreg_proba, xgb_proba, strategy='f1'):
    """
    Comparison of two models based on selected threshold strategy
    and returns relevant metrics.

    Args:
        y_true: empirical labels
        logreg_proba: probability for LogReg
        xgb_proba: probability for XGBoost
        strategy: Threshold strategy (e.g. 'f1', 'cost', 'youden', ...)

    Returns:
        Tuple of two metric-dictionaries (logreg, xgb)
    """
    kwargs = {"calculate_cost": calculate_cost} if strategy == "cost" else {}

    best_threshold_logreg = find_best_threshold(y_true, logreg_proba, strategy, **kwargs)
    best_threshold_xgb = find_best_threshold(y_true, xgb_proba, strategy, **kwargs)

    metrics_logreg = compute_metrics(y_true, logreg_proba, best_threshold_logreg)
    metrics_xgb = compute_metrics(y_true, xgb_proba, best_threshold_xgb)

    return metrics_logreg, metrics_xgb
