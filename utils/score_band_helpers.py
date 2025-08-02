import pandas as pd
import numpy as np

def assign_score_bands(y_true, y_probs, threshold, model_name):
    df = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    df['model'] = model_name

    df['score_band'] = np.nan
    df.loc[df['y_prob'] >= threshold, 'score_band'] = 10

    mask_rest = df['score_band'].isna()
    df.loc[mask_rest, 'score_band'] = pd.qcut(
        df.loc[mask_rest, 'y_prob'], 9, labels=range(1, 10), duplicates='drop'
    )

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
