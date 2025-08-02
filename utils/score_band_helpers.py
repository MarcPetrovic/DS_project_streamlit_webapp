import pandas as pd
import numpy as np

def assign_score_bands(y_true, y_probs, threshold, model_name):
    df = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    df['model'] = model_name
    df['score_band'] = np.nan

    # Band 10: Score ≥ Threshold
    df.loc[df['y_prob'] >= threshold, 'score_band'] = 10

    # Übrige Scores (Score < Threshold)
    mask_rest = df['score_band'].isna()
    remaining_scores = df.loc[mask_rest, 'y_prob']

    # Falls zu wenig eindeutige Werte: adaptive Anzahl Bins
    num_unique = remaining_scores.nunique()
    num_bins = min(9, num_unique)

    if num_bins >= 2:
        bins = pd.qcut(remaining_scores, num_bins, labels=range(1, num_bins + 1), duplicates='drop')
        df.loc[mask_rest, 'score_band'] = bins
    else:
        # Fallback: alles restliche in Band 1
        df.loc[mask_rest, 'score_band'] = 1

    df['score_band'] = df['score_band'].astype(int)
    return df


def score_band_cost_analysis(df_band):
    """
    Gibt pro Modell und Score-Band:
    - total_samples, positives
    - operative Kosten (TP + FP × 550 €)
    - Opportunitätskosten (FN × 3350 €)
    """
    result = []

    for model in df_band['model'].unique():
        for band in sorted(df_band['score_band'].unique(), reverse=True):
            group = df_band[(df_band['model'] == model) & (df_band['score_band'] == band)]
            total = len(group)
            tp = ((group['y_true'] == 1)).sum()
            fp = ((group['y_true'] == 0)).sum()
            fn = 0  # da alle kontaktiert werden
            opp_cost = fn * 3350
            op_cost = (tp + fp) * 550

            result.append({
                "model": model,
                "score_band": band,
                "total_samples": total,
                "positives": tp,
                "cost_operational": op_cost,
                "cost_opportunity": opp_cost,
                "cost_total": op_cost + opp_cost
            })

    return pd.DataFrame(result)
