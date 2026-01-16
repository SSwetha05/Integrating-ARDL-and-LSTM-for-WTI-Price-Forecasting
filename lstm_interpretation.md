**LSTM Interpretation**



An LSTM model was applied to predict monthly crude oil prices. The model generated a RMSE of 8.5% and a MAE of 6.4% accuracy on the test dataset. RMSE determines the square root of the average squared differences between predicted and actual values and disproportionately penalizes larger errors while MAE simply measures the average absolute difference from an actual value. Both metrics suggest that the model is providing reasonably accurate forecasts, where errors are relatively small in comparison to the scale of crude oil prices. A lower RMSE and MAE indicates that the LSTM captures trends in crude oil prices well. The model was trained on historical data covering several years which enabled the model to learn more complex temporal dependencies including non-linear patterns, seasonality, and a chance of structural shifts in the temporal dependence in the training data.



The LSTM's efficiency comes from its inherent design to process and extract value from sequential data and capture  long-term dependencies in time series. The price of crude oil is influenced by many factors, including global demand, supply shocks, geopolitical events, and market speculations that may produce complex price patterns. Although traditional linear models like ARDL capture linear relationships well, they are not suited to explicit non-linearities in data or sudden and dramatic changes in trends.



LSTM networks, which have a gated architecture (input, output, and forget gates), are able to allow the network not to overwrite information from previous observations that are relevant, while providing the ability to forget irrelevant noise, as they are applicable to noisy environments, including highly volatile markets. The moderate RMSE and MAE suggest that the LSTM model is effective in learning attention to short term variation and longer term trends in price but some error is always implied, since shocks to the underlying factors are not foreseeable, and also, oil prices are inherently stochastic. 



Given the results, the LSTM model is a plausible framework for predicting crude oil prices. For policymakers, energy companies, and investors, the model has a potential use for price change estimation, in order to improve hedge strategy or to prepare better for procurement and production schedules. The RMSE of 8.5%, suggests again that prices will vary from the forecasted price only modestly on average. But prediction should proceed with caution, as extreme price shocks, related to geopolitical crises, for example, may mean further deviation, beyond provided estimates.



