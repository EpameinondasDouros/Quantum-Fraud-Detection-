def select_top_features(df, target_col='isFraud', top_n=4):
    correlations = df.corr()[target_col].abs().sort_values(ascending=False)
    top_features = correlations.iloc[1:top_n+1].index
    return top_features.tolist()
