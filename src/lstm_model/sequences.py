import numpy as np

def create_sequences(X, y, dates, lookback):
    """
    Create rolling window sequences for LSTM.

    """
    X_seq, y_seq, date_seq = [], [], []

    for i in range(lookback, len(X)):
        X_seq.append(X[i - lookback:i])
        y_seq.append(y[i])
        date_seq.append(dates[i])

    return np.array(X_seq), np.array(y_seq), np.array(date_seq)