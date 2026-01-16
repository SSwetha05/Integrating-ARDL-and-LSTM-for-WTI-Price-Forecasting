Research Question
1. Do macroeconomic and commodity market variables exhibit a stable long-run cointegrated relationship with WTI crude oil prices, and what are their short-run dynamics?
2. Can a data-driven LSTM model, incorporating broader financial and macroeconomic indicators, effectively forecast short-term movements in WTI crude oil prices?

Why ARDL + LSTM
This study employs a hybrid modelling framework combining an Autoregressive Distributed Lag (ARDL) model and a Long Short-Term Memory (LSTM) neural network to forecast crude oil prices. 
The ARDL model is used to capture the short-run and long-run equilibrium relationships between crude oil prices and key macroeconomic and commodity variables, while the LSTM model is applied to capture complex, non-linear, and temporal dependencies that traditional econometric models may not fully account for.

Repository Structure

├── ardl_analysis/
│   ├── ardl_model_dataset.csv
│   ├── ardl_summary_statistics.csv
│   ├── ardl_adf_test/
│   │   ├── at_level_unit_root_test/
│   │   │   └── *.pdf
│   │   ├── at_diff_unit_root_test/
│   │   │   └── *.pdf
│   │   └── adf_test_summary.csv
│   ├── f_bounds_test.pdf
│   ├── error_correction_regression.pdf
│   ├── cusum_test.pdf
│   ├── cusum_of_square_test.pdf
│   └── interpretation.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── lstm_wti_monthly.keras
│   ├── scaler_x.save
│   └── scaler_y.save
│
├── src/
│   └── lstm_model/
│       ├── __init__.py
│       ├── config.py
│       ├── data_loader.py
│       ├── preprocessing.py
│       ├── features.py
│       ├── sequences.py
│       ├── model.py
│       ├── train.py
│       ├── evaluate.py
│       └── forecast.py
│
├── lstm_interpretation.md
├── requirements.txt
└── .gitignore

Folder Descriptions

ardl_analysis 
  Contains all econometric analysis conducted in EViews, including unit root tests,
  ARDL bounds testing, error correction model estimation, and model stability diagnostics.
  The folder also includes a written interpretation of the results.
data 
  Raw and processed datasets used for both ARDL and LSTM analysis.
models 
  Trained LSTM model and associated scalers used for normalization and inverse transformation.
src/lstm_model  
  Modular Python implementation of the LSTM forecasting pipeline, including data preprocessing,
  feature engineering, model training, evaluation, and multi-step forecasting.
lstm_interpretation.md 
  Interpretation of LSTM model performance, forecasting results, and limitations.

Conclusion
The ARDL model offered a theoretical basis for exploring the short-term and long-term relationships between crude oil pricing and macroeconomic variables, but it is not primarily designed for multi-step forecasting. 
Therefore, once cointegration from  the ARDL model was confirmed, the LSTM model was created by including additional variables such as Copper, S&P 500 Index, US CPI, and US 10-Year Treasury Yield. 
This was done to implement an effective method to forecast crude oil prices. 
The objective to utilize LSTM to provide predictive ability from a practical perspective to build upon the theoretical explanation provided by ARDL was fulfilled.
