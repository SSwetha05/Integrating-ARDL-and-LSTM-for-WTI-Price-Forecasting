#Reproducibility
seed = 42

#Paths
data_path = "data/raw/LSTM_model_dataset.csv"
processed_path = "data/processed/cleaned_monthly.csv"
model_save_path = "models/lstm_wti_monthly.keras"
scaler_x_path = "scaler_X.save"
scaler_y_path = "scaler_y.save"

#Data
date_col = "Year"
target_col = "WTI"
feature_cols = ["BRENT_diff", "GLD", "CPI", "SP500", "EPU", "CPER", "KOL", "UST10Y", "USDINR"]

#Time-series stuff
lookback = 12          # past 12 months
n_future_months = 12   #Forecast time-period
train_ratio = 0.72
val_ratio = 0.08
test_ratio = 0.20

#Model Hyperparameters
batch_size = 32
epochs = 100
LSTM_units = 64
Droupout_units = 0.5
Dense_units = 16