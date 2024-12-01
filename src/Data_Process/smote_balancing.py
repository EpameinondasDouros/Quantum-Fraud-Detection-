from imblearn.over_sampling import SMOTE
import pandas as pd

def balance_with_smote(df, target_col='Class', smote_ratio=0.15, random_state=42):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    smote = SMOTE(sampling_strategy=smote_ratio, random_state=random_state)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    balanced_df = pd.DataFrame(X_resampled, columns=X.columns)
    balanced_df[target_col] = y_resampled
    return balanced_df
