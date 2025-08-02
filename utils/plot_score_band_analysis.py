import matplotlib.pyplot as plt
import pandas as pd

def plot_score_band_distribution_and_cost(df_costs: pd.DataFrame) -> plt.Figure:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharex=True)

    width = 0.35
    offsets = {"Logistic Regression": -width/2, "XGBoost": width/2}
    colors = {"cost_operational": "#4DAF4A", "cost_opportunity": "#E41A1C"}

    # Links: Verteilung Fallzahlen
    for model, color in zip(["Logistic Regression", "XGBoost"], ["#097a80", "#C00000"]):
        data = df_costs[df_costs["model"] == model].sort_values("score_band", ascending=False)
        x = [i + offsets[model] for i in data["score_band"]]
        ax1.bar(x, data["total_samples"], width=width, label=model, color=color)

    ax1.set_title("Sample Distribution by Score Band")
    ax1.set_xlabel("Score Band (10 = Top Priority)")
    ax1.set_ylabel("Number of Samples")
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.4)

    # Rechts: gestapelte Kosten
    for model in ["Logistic Regression", "XGBoost"]:
        data = df_costs[df_costs["model"] == model].sort_values("score_band", ascending=False)
        x = [i + offsets[model] for i in data["score_band"]]
        op = data["cost_operational"] / 1000
        opp = data["cost_opportunity"] / 1000

        ax2.bar(x, op, width=width, label=f"{model} – Operative", color=colors["cost_operational"])
        ax2.bar(x, opp, width=width, bottom=op, label=f"{model} – Opportunity", color=colors["cost_opportunity"])

    ax2.set_title("Stacked Cost per Score Band")
    ax2.set_xlabel("Score Band (10 = Top Priority)")
    ax2.set_ylabel("Cost per Band (k €)")
    ax2.legend()
    ax2.grid(True, linestyle="--", alpha=0.4)

    fig.tight_layout()
    return fig
