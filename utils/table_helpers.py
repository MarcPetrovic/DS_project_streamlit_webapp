import pandas as pd

def render_html_table_metrics(df: pd.DataFrame) -> str:
    html = """
    <style>
        .scrollable-table-container {
            height: 400px;
            overflow-y: auto;
            border: 1px solid #ccc;
            padding: 10px;
        }
        table {
            width: 100% !important;
            border-collapse: collapse !important;
            table-layout: auto !important;
            border: 2px solid black !important;
        }
        th {
            position: sticky;
            top: 0;
            background-color: #097a80 !important;
            color: white !important;
            border: 1px solid lightgray !important;
            text-align: left !important;
            padding: 8px !important;
            word-break: normal !important;
            max-width: 400px !important;
            min-width: 120px !important;
            font-size: 14px !important;
        }
        td {
            background-color: white !important;
            color: black !important;
            border: 1px solid black !important;
            text-align: left !important;
            padding: 8px !important;
            word-break: normal !important;
            max-width: 400px !important;
            min-width: 120px !important;
            font-size: 14px !important;
        }
    </style>
    <div class="scrollable-table-container">
    <table>
        <thead>
            <tr>
    """

    for col in df.columns:
        html += f"<th>{col}</th>"
    html += "</tr></thead><tbody>"

    for _, row in df.iterrows():
        html += "<tr>"
        for col in df.columns:
            cell = row[col]
            html += f"<td>{str(cell)}</td>"
        html += "</tr>"

    html += "</tbody></table></div>"
    return html


def mark_best(df: pd.DataFrame) -> pd.DataFrame:
    df_marked = df.copy()
    for idx in df.index:
        idx_str = str(idx) 
        val1 = df.loc[idx, "Logistic Regression"]
        val2 = df.loc[idx, "XGBoost"]

        is_cost = "Cost" in idx_str or "€" in idx_str

        if is_cost:
            val1 = val1 / 1000
            val2 = val2 / 1000
            if not idx_str.endswith("(k €)"):
                df_marked.rename(index={idx: f"{idx_str} (k €)"}, inplace=True)
                idx = f"{idx_str} (k €)"

        if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
            if "Rate" in idx_str or is_cost:
                if val1 < val2:
                    df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f} ✅"
                    df_marked.loc[idx, "XGBoost"] = f"{val2:.3f}"
                else:
                    df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f}"
                    df_marked.loc[idx, "XGBoost"] = f"{val2:.3f} ✅"
            else:
                if val1 > val2:
                    df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f} ✅"
                    df_marked.loc[idx, "XGBoost"] = f"{val2:.3f}"
                else:
                    df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f}"
                    df_marked.loc[idx, "XGBoost"] = f"{val2:.3f} ✅"
        else:
            df_marked.loc[idx, "Logistic Regression"] = str(val1)
            df_marked.loc[idx, "XGBoost"] = str(val2)
    return df_marked

def mark_best_overall(df: pd.DataFrame, metric_cols: list, minimize_cols: list = []) -> pd.DataFrame:
    """
    Marked within a comparison modell table (over all strategies) the best value with ✅.
    
    Args:
        df (pd.DataFrame): DataFrame with strategie, models and metrics.
        metric_cols (list): list of metric columns, which should be compared.
        minimize_cols (list): metrics, where best performing value is the lowest (e. g. costs).
        
    Returns:
        pd.DataFrame: Marked with ✅ .
    """
    df_marked = df.copy()

    for col in metric_cols:
        try:
            # selecting numeric column for comparison
            vals = pd.to_numeric(df[col], errors='coerce')
            if col in minimize_cols:
                best_val = vals.min()
            else:
                best_val = vals.max()
            
            # Marked up value
            df_marked[col] = [
                f"{val:.3f} ✅" if val == best_val else f"{val:.3f}"
                for val in vals
            ]
        except:
            continue

    return df_marked

def mark_best_and_second_best_overall(df: pd.DataFrame, metric_cols: list, minimize_cols: list = []) -> pd.DataFrame:
    """
    Markiert die besten Werte mit ✅ und die zweitbesten mit 🔷 pro Metrik über alle Modelle & Strategien.

    Args:
        df (pd.DataFrame): DataFrame mit Modell–Strategie–Metriken.
        metric_cols (list): Liste zu vergleichender Metriken.
        minimize_cols (list): Metriken, bei denen kleinere Werte besser sind.

    Returns:
        pd.DataFrame: Mit Symbolen markierter DataFrame.
    """
    df_marked = df.copy()

    for col in metric_cols:
        try:
            # Konvertiere zur Sicherheit
            numeric_vals = pd.to_numeric(df[col], errors='coerce')
            sort_asc = col in minimize_cols
            sorted_vals = numeric_vals.sort_values(ascending=sort_asc)

            best_val = sorted_vals.iloc[0]
            second_best_val = sorted_vals.iloc[1]

            # Markiere Spalte
            def format_val(val):
                if pd.isna(val):
                    return ""
                elif val == best_val:
                    return f"{val:.3f} ✅"
                elif val == second_best_val:
                    return f"{val:.3f} 🔷"
                else:
                    return f"{val:.3f}"

            df_marked[col] = numeric_vals.apply(format_val)

        except Exception as e:
            print(f"Skipping column {col} due to error: {e}")
            continue

    # Threshold-Spalte: Nur numerisch und auf 3 Nachkommastellen
    if "Threshold" in df_marked.columns:
        try:
            df_marked["Threshold"] = pd.to_numeric(df_marked["Threshold"], errors='coerce').map(lambda x: f"{x:.3f}")
        except:
            pass
    return df_marked
