import numpy as np
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from src.lstm_model.config import lookback, model_save_path, scaler_x_path, scaler_y_path, n_future_months
from src.lstm_model.sequences import create_sequences

def forecast_future(model_path, last_sequence, n_future_months, scaler_y):
    """
    Generate future WTI forecasts using the trained LSTM model.
    
    Parameters:
    - model_path : path to saved LSTM model (.h5)
    - last_sequence : 3D array (1 × lookback × features)
    - n_future_months : int, number of months to predict
    - scaler_y : fitted scaler for inverse-transforming predictions
    
    Returns:
    - future_preds : array of predicted WTI prices
    """
    model = load_model(model_save_path)
    scaler_y = joblib.load(scaler_y_path)

    current_seq = last_sequence.copy()
    future_preds_scaled = []

    for _ in range(n_future_months):
        next_pred = model.predict(current_seq.reshape(1, lookback, -1), verbose=0)
        future_preds_scaled.append(next_pred[0, 0])

        # roll window, hold exogenous variables constant
        next_features = current_seq[-1].copy()
        current_seq = np.vstack([current_seq[1:], next_features])

    future_prices = scaler_y.inverse_transform(
        np.array(future_preds_scaled).reshape(-1, 1)
    ).flatten()

    return future_prices

def main():
    # Load last sequence and scalers saved from training
    last_sequence = np.load("data/processed/last_sequence.npy")
    scaler_y = joblib.load(scaler_y_path)

    future_preds = forecast_future(model_save_path, last_sequence, n_future_months, scaler_y)

    print("\nFuture WTI forecasts:")
    for i, val in enumerate(future_preds, 1):
        print(f"Month +{i}: {val:.2f}")


if __name__ == "__main__":
    main()
