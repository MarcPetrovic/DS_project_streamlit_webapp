import pandas as pd

def summary(df):
    tab = pd.DataFrame(index=df.columns, columns=[
        'nb_unique_values',
        'nb_missing_values',
        'rate_missing_values',
        'type',
        'duplicates'
    ])
    tab['nb_unique_values'] = df.nunique().values
    tab['nb_missing_values'] = df.isna().sum().values
    tab['rate_missing_values'] = round(df.isna().sum() * 100 / len(df), 2)
    tab['type'] = df.dtypes.values
    tab['duplicates'] = df.duplicated().sum()
    return tab
