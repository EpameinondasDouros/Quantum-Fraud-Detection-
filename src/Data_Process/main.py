from data_preprocessing import load_data, preprocess_data
from smote_balancing import balance_with_smote
from feature_selection import select_top_features
from data_scaling import scale_data
from data_splitting import split_data
import pandas as pd

# Step 1: Load and preprocess data
file_path = "../../Datasets/PS_20174392719_1491204439457_log.csv"
raw_data = load_data(file_path)
cleaned_data = preprocess_data(raw_data)

# Step 2: Apply SMOTE
balanced_data = balance_with_smote(cleaned_data, target_col='isFraud', smote_ratio=0.1)

# Step 3: Feature selection
top_features = select_top_features(balanced_data, target_col='isFraud')
selected_data = balanced_data[top_features + ['isFraud']]

# Step 4: Scale the data
scaled_data = scale_data(selected_data)

# Step 5: Split the data
X = scaled_data[:, :-1]
y = scaled_data[:, -1]
X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
