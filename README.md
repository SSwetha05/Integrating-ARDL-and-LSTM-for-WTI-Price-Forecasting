**Why ARDL + LSTM**
This study employs a hybrid modelling framework combining an Autoregressive Distributed Lag (ARDL) model and a Long Short-Term Memory (LSTM) neural network to forecast crude oil prices. 
The ARDL model is used to capture the short-run and long-run equilibrium relationships between crude oil prices and key macroeconomic and commodity variables, while the LSTM model is applied to capture complex, non-linear, and temporal dependencies that traditional econometric models may not fully account for.

**Repository Structure**
*ardl_analysis* 
  Contains all econometric analysis conducted in EViews, including unit root tests,
  ARDL bounds testing, error correction model estimation, and model stability diagnostics.
  The folder also includes a written interpretation of the results.
  
*data* 
  Raw and processed datasets used for both ARDL and LSTM analysis.
  
*models* 
  Trained LSTM model and associated scalers used for normalization and inverse transformation.
  
*src/lstm_model*  
  Modular Python implementation of the LSTM forecasting pipeline, including data preprocessing,
  feature engineering, model training, evaluation, and multi-step forecasting.
  
*lstm_interpretation.md* 
  Interpretation of LSTM model performance, forecasting results, and limitations.

**Conclusion**
The ARDL model offered a theoretical basis for exploring the short-term and long-term relationships between crude oil pricing and macroeconomic variables, but it is not primarily designed for multi-step forecasting. 
The LSTM model complemented the econometric insights of the ARDL analysis by capturing non-linear and temporal patterns, enabling effective short-term and multi-step forecasting of crude oil prices. 
Overall, the hybrid ARDL–LSTM framework successfully integrates economic theory with data-driven prediction, fulfilling the study’s objective of combining interpretability with practical forecasting performance.
