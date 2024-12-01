from sklearn.preprocessing import MinMaxScaler, StandardScaler

def scale_data(df, scaler_type='minmax'):
    scaler = MinMaxScaler() if scaler_type == 'minmax' else StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled
