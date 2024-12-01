import pandas as pd

def load_data(file_path, delimiter=','):
    return pd.read_csv(file_path, delimiter=delimiter)

def preprocess_data(df):
    df_filtered = df.loc[(df['type'].isin(['CASH_OUT', 'TRANSFER'])), :]
    df_filtered.drop(columns=['nameOrig', 'nameDest', 'isFlaggedFraud'], inplace=True)
    df_filtered['type'] = df['type'].map({'CASH_OUT': 0, 'TRANSFER': 1})
    return df_filtered
