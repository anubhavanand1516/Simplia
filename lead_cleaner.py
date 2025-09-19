# lead_cleaner.py
import pandas as pd

def clean_and_dedupe(records):
    """Takes a list of dicts, returns cleaned DataFrame."""
    df = pd.DataFrame(records)

    # Intentionally duplicate first row to show dedupe (optional)
    if not df.empty:
        df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

    # Cleaning
    df['email'] = df['email'].str.strip().str.lower()
    df['phone'] = df['phone'].str.strip()

    before = len(df)
    df = df.drop_duplicates(subset=['email','phone'], keep='first').reset_index(drop=True)
    after = len(df)

    return df, before, after
