import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from src.lstm_model.config import processed_path, feature_cols, target_col, train_ratio, val_ratio, scaler_x_path, scaler_y_path, date_col

def preprocess_data():
    """
    Loads cleaned CSV, scales features and target, and returns:
    X_scaled, y_scaled, dates, scaler_X, scaler_y
    """

    df = pd.read_csv(processed_path)

    # Split raw dataframe 
    n_total = len(df)
    n_train = int(n_total * train_ratio)
    n_val = int(n_total * val_ratio)

    train_df = df.iloc[:n_train]
    val_df   = df.iloc[n_train:n_train+n_val]
    test_df  = df.iloc[n_train+n_val:]

    scaler_X = MinMaxScaler()
    scaler_y = MinMaxScaler()

    scaler_X.fit(train_df[feature_cols])
    scaler_y.fit(train_df[[target_col]])

    X_scaled = scaler_X.transform(df[feature_cols])
    y_scaled = scaler_y.transform(df[[target_col]])

    dates = df[date_col].values

    joblib.dump(scaler_X, scaler_x_path)
    joblib.dump(scaler_y, scaler_y_path)

    return X_scaled, y_scaled, dates
