import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import MeanSquaredError
from src.lstm_model.config import model_save_path, scaler_x_path, scaler_y_path, target_col

def evaluate_model(model_path, X_test, y_test, test_dates):
    """
    Evaluate trained LSTM model on test data.
    Computes RMSE, MAE and plots predicted vs actual.
    """
    # Load model
    model = load_model(model_path)

    # Load scalers
    scaler_X = joblib.load(scaler_x_path)
    scaler_y = joblib.load(scaler_y_path)

    # Predict
    y_pred_scaled = model.predict(X_test)
    y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).flatten()
    y_true = scaler_y.inverse_transform(y_test.reshape(-1, 1)).flatten()
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f"Test RMSE: {rmse:.4f}, Test MAE: {mae:.4f}")


    plt.figure(figsize=(12, 6))
    plt.plot(test_dates, y_true, label=f"Actual {target_col}")
    plt.plot(test_dates, y_pred, linestyle="--", label=f"Predicted {target_col}")
    plt.xlabel("Date")
    plt.ylabel(f"{target_col} Price")
    plt.title(f"Monthly {target_col} Forecast – Actual vs Predicted")
    plt.legend()
    plt.grid(True)
    plt.show()

    return rmse, mae, y_true, y_pred

def main():
    # Load test arrays saved by train.py
    X_test = np.load("data/processed/X_test.npy")
    y_test = np.load("data/processed/y_test.npy")
    test_dates = np.load("data/processed/test_dates.npy")

    evaluate_model(model_save_path, X_test, y_test, test_dates)


if __name__ == "__main__":
    main()