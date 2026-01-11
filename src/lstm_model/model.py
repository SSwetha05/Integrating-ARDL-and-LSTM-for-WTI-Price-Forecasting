from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from src.lstm_model.config import Dense_units, lookback, LSTM_units, Droupout_units

def build_lstm(input_shape):
    """
    Builds and compiles the LSTM model.

    """
    model = Sequential([
    LSTM(LSTM_units, input_shape=input_shape),
    Dropout(Droupout_units),
    Dense(Dense_units, activation="relu"),
    Dense(1)
])

    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.summary()

    return model