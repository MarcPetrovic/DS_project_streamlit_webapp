import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_gains_chart(y_true, y_probs, model_name, color):
    """
    Zeichnet die Gains Chart-Kurve (kumulativer Anteil positiver Fälle).
    """
    data = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    data = data.sort_values(by='y_prob', ascending=False).reset_index(drop=True)
    data['cumulative_positives'] = data['y_true'].cumsum()
    total_positives = data['y_true'].sum()
    sample_size = len(data)
    
    proportions = np.arange(1, len(data) + 1) / sample_size
    gains = data['cumulative_positives'] / total_positives

    plt.plot(proportions, gains, label=model_name, color=color)
