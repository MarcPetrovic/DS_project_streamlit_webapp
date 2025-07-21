import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve
import streamlit as st

def plot_ks_curve(y_true, y_probs, model_name="Model", color="blue"):
    """
    Zeichnet die KS-Kurve (TPR, FPR und KS-Distanz)
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_probs)
    ks_statistic = np.max(np.abs(tpr - fpr))
    ks_threshold = thresholds[np.argmax(np.abs(tpr - fpr))]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(thresholds, tpr, label='TPR', color='green')
    ax.plot(thresholds, fpr, label='FPR', color='darkblue')
    ax.plot(thresholds, tpr - fpr, label='TPR - FPR (KS Distance)', color=color)
    ax.axvline(ks_threshold, color='#191919', linestyle='--', label=f'KS Threshold = {ks_threshold:.4f}')
    ax.axhline(ks_statistic, color=color, linestyle='--', label=f'KS Statistic = {ks_statistic:.4f}')

    ax.set_xlabel('Threshold')
    ax.set_ylabel('Rate')
    ax.set_title(f'KS Curve – {model_name}')
    ax.grid(True, linestyle='--', alpha=0.6, color='grey')
    ax.set_facecolor('lightgrey')
    ax.legend()
    plt.tight_layout()

    st.pyplot(fig)
