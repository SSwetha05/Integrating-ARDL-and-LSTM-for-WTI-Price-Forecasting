import os
import joblib
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from src.lstm_model.config import lookback, batch_size, epochs, model_save_path, scaler_x_path, scaler_y_path, train_ratio, val_ratio, seed
from src.lstm_model.preprocessing import preprocess_data  # scaled arrays
from src.lstm_model.sequences import create_sequences
from src.lstm_model.model import build_lstm

def main():
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

    X_scaled, y_scaled, dates = preprocess_data()
    X_seq, y_seq, seq_dates = create_sequences(X_scaled, y_scaled, dates, lookback)

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

    print("Shapes -> X_train:", X_train.shape, "X_val:", X_val.shape, "X_test:", X_test.shape)


    model = build_lstm(input_shape=(lookback, X_train.shape[2]))

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

    print(f"Training complete. Model saved at {model_save_path}")

    np.save("data/processed/X_test.npy", X_test)
    np.save("data/processed/y_test.npy", y_test)
    np.save("data/processed/test_dates.npy", test_dates)
    last_sequence = X_seq[-1]  
    np.save("data/processed/last_sequence.npy", last_sequence)

if __name__ == "__main__":
    main()