from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.4, val_test_ratio=0.5, random_state=42):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=test_size, random_state=random_state)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=val_test_ratio, random_state=random_state)
    return X_train, X_val, X_test, y_train, y_val, y_test
