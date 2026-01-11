import pandas as pd
from src.lstm_model.config import data_path, processed_path, date_col

def build_clean_monthly_dataset():
    """
    Builds the final monthly macro–oil dataset used for all models.
    Applies Brent differencing, monthly resampling, and missing-value handling.
    """
df = pd.read_csv(data_path)

df["BRENT_diff"] = df["BRENT"].diff()


df[date_col] = pd.to_datetime(df[date_col], format="%d-%m-%Y", errors="coerce")
df = df.sort_values(date_col)

df = df.set_index(date_col)
df = df.resample("MS").mean()      # complete monthly calendar

# Interpolate internal missing values
df = df.interpolate(method="time")

# Fill NaNs at the beginning or end (forward/backward fill)
df = df.ffill().bfill()

df = df.reset_index()
# Drop original Brent (we only use the spread)
df = df.drop(columns=["BRENT"])

# Save engineered dataset
df.to_csv(processed_path, index=False)

print("Clean monthly dataset saved to:", processed_path)
print("Final dataframe shape:", df.shape)
print(df.head())

if __name__ == "__main__":
    build_clean_monthly_dataset()
