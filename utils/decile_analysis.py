import pandas as pd

def decile_analysis(y_true, y_probs):
    """
    Berechnet für jede Decile die Anzahl positiver Fälle, Gesamtanzahl und Lift.
    """
    df = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    df['decile'] = pd.qcut(df['y_prob'], 10, labels=False, duplicates='drop')
    global_pos_rate = df['y_true'].mean()
    
    analysis = df.groupby('decile').agg(
        total_samples=('y_true', 'count'),
        positives=('y_true', 'sum'),
        lift=('y_true', lambda x: x.sum() / (len(x) * global_pos_rate))
    ).sort_index(ascending=False)
    
    return analysis
