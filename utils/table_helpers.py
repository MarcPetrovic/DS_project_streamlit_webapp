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
            table-layout: fixed !important;
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
            word-break: break-word !important;
            max-width: 250px !important;
            font-size: 14px !important;
        }
        td {
            background-color: white !important;
            color: black !important;
            border: 1px solid black !important;
            text-align: left !important;
            padding: 8px !important;
            word-break: break-word !important;
            max-width: 250px !important;
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
