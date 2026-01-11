from src.lstm_model.data_loader import build_clean_monthly_dataset
from src.lstm_model.preprocessing import preprocess_data
from src.lstm_model.train import main as train_model
from src.lstm_model.evaluate import main as evaluate_model
from src.lstm_model.forecast import main as run_forecast

if __name__ == "__main__":
    print("Running full WTI pipeline...")

    build_clean_monthly_dataset()
    preprocess_data()
    train_model()
    evaluate_model()
    run_forecast()
