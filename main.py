import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import joblib

seed = 42
os.environ['PYTHONHASHSEED'] = str(seed)
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

data_path = "LSTM_model_dataset.csv"
model_save_path = "lstm_wti_monthly.h5"
scaler_x_path = "scaler_X.save"
scaler_y_path = "scaler_y.save"

date_col = "Year"

lookback = 12          # past 12 months
batch_size = 32
epochs = 100

train_ratio = 0.72
val_ratio = 0.08
test_ratio = 0.20


df = pd.read_csv(data_path)
df["BRENT_diff"] = df["BRENT"].diff()

target_col = "WTI"
feature_cols = [
    "BRENT_diff",
    "GLD",
    "CPI",
    "SP500",
    "EPU",
    "CPER",
    "KOL",
    "UST10Y",
    "USDINR"
]

df[date_col] = pd.to_datetime(df[date_col], format="%d-%m-%Y", errors="coerce")
df = df.sort_values(date_col)

df = df.set_index(date_col)
df = df.resample("MS").mean()      # complete monthly calendar

# Interpolate internal missing values
df = df.interpolate(method="time")

# Fill NaNs at the beginning or end (forward/backward fill)
df = df.ffill().bfill()

df = df.reset_index()
print("Final dataframe shape:", df.shape)
print(df.head())

assert len(df) > lookback, "Not enough data after cleaning!"
assert not df.isna().any().any(), "NaNs still present!"

# Split raw dataframe first
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

joblib.dump(scaler_X, scaler_x_path)
joblib.dump(scaler_y, scaler_y_path)


def create_sequences(X, y, dates, lookback):
    X_seq, y_seq, date_seq = [], [], []

    for i in range(lookback, len(X)):
        X_seq.append(X[i - lookback:i])
        y_seq.append(y[i])
        date_seq.append(dates[i])

    return np.array(X_seq), np.array(y_seq), np.array(date_seq)

dates = df[date_col].values
X_seq, y_seq, seq_dates = create_sequences(
    X_scaled, y_scaled, dates, lookback
)


n_total = len(X_seq)
n_train = int(n_total * train_ratio)
n_val = int(n_total * val_ratio)

X_train = X_seq[:n_train]
y_train = y_seq[:n_train]

X_val = X_seq[n_train:n_train + n_val]
y_val = y_seq[n_train:n_train + n_val]

X_test = X_seq[n_train + n_val:]
y_test = y_seq[n_train + n_val:]
test_dates = seq_dates[n_train + n_val:]


model = Sequential([
    LSTM(64, input_shape=(lookback, X_train.shape[2])),
    Dropout(0.5),
    Dense(16, activation="relu"),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.summary()


callbacks = [
    EarlyStopping(monitor="val_loss", patience=15, restore_best_weights=True),
    ModelCheckpoint(model_save_path, monitor="val_loss", save_best_only=True)
]

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=epochs,
    batch_size=batch_size,
    callbacks=callbacks,
    verbose=2,
    shuffle=False
)


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

n_futute_months = 12
last_sequence = X_seq[-1]
future_preds_scaled = []

for _ in range(n_futute_months):
    next_pred = model.predict(
        last_sequence.reshape(1, lookback, -1)
    )
    future_preds_scaled.append(next_pred[0, 0])

    # roll window (exogenous vars held constant)
    next_features = last_sequence[-1].copy()
    last_sequence = np.vstack([last_sequence[1:], next_features])



