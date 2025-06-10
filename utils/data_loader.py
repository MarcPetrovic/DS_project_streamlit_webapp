import pandas as pd
import os

def load_csv_data(
    filename: str,
    sep: str = ",",
    header: bool = True,
    add_row_id: bool = False,
    encoding: str = "utf-8"
) -> pd.DataFrame:
    """
    Lädt eine CSV-Datei und gibt ein pandas DataFrame zurück.

    Args:
        filename (str): Pfad zur CSV-Datei (relativ oder absolut).
        sep (str): Trennzeichen (Standard: ',').
        header (bool): True, wenn erste Zeile Spaltennamen enthält (Standard: True).
        add_row_id (bool): True, wenn eine ROW_ID-Spalte hinzugefügt werden soll (Standard: False).
        encoding (str): Zeichencodierung der Datei (Standard: 'utf-8').

    Returns:
        pd.DataFrame: Eingelesene Daten als DataFrame.
    """
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Datei nicht gefunden: {filename}")
        
        df = pd.read_csv(filename, sep=sep, header=0 if header else None, encoding=encoding)
        
        if add_row_id:
            df["ROW_ID"] = df.index + 1
        
        return df

    except Exception as e:
        raise RuntimeError(f"Fehler beim Einlesen der Datei '{filename}': {e}")
