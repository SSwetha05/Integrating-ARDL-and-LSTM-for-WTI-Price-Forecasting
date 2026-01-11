"""
Feature specification for the WTI forecasting model.

Defines the exogenous macro-financial variables used to predict WTI prices.
"""

# Exogenous predictors used by the LSTM
FEATURES = [
    "BRENT_diff",   # Global crude price shock
    "GLD",          # Safe-haven & inflation hedge
    "CPI",          # US inflation
    "SP500",        # Global risk appetite
    "EPU",          # Policy uncertainty
    "CPER",         # Industrial metals demand
    "KOL",          # Thermal coal (energy substitute)
    "UST10Y",       # Long-term interest rates
    "USDINR"        # Dollar strength vs emerging markets
]

TARGET = "WTI"