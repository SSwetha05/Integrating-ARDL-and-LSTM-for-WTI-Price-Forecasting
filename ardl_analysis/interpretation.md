**ARDL model specification**



WTIt = f (BRENTt, EPUt, USDINRt, GOLDt, KOLt)            — (Eqn. 1)





&nbsp;WTIt = α0 + ∑\_{i=1}^{p−1}φi\*WTIt - 1 + j + ∑\_{j=0}^{q1−1}01jΔBRENTt - j + ∑\_{j=0}^{q2−1}02jΔEPUt - j + ∑\_{j=0}^{q3−1}03jΔUSDINRt - j + ∑\_{j=0}^{q4−1}04jΔGOLDt - j + ∑\_{j=0}^{q5−1}05jΔKOLt - j + γECTt-1 + εt   — (Eqn. 2)





**ADF-Test Interpretation**

The Augmented Dickey–Fuller (ADF) test was used to assess the stationarity of WTI, Brent, Gold, EPU, KOL, and USDINR under the assumption of a trend. At level form, WTI (p = 0.4073), Brent (p = 0.5304), Gold (p = 0.6413), and USDINR (p = 0.5204) have p-values above 0.05, indicating non-stationarity. In contrast, EPU (p = 0.0003) and KOL (p = 0.0158) are significant at 5%, suggesting stationarity at level. After first differencing, all variables become significant (p = 0.0000), confirming stationarity at first difference. Thus, the variables exhibit a mixed order of integration, I(0) and I(1), supporting the use of the ARDL bounds testing approach to examine long-run relationships.



**F-Bounds test Interpretation**

The ARDL bounds test for cointegration was applied to determine whether a long-run equilibrium relationship exists among the variables. The computed F-statistic is 4.075494, which exceeded the upper bound critical value of 3.38 at the 5% significance level.

Since the F-statistic lies above the I(1) bound, we reject the null hypothesis of “no cointegration” This indicates the presence of a long-run cointegrating relationship among the variables in the model. Thus, it can be concluded that the dependent and independent variables move together in the long run, justifying further estimation of both short-run and long-run coefficients within the ARDL framework.



**Recursive stability test (ECM Regression, CUSUM, CUSUM of Square)**

The coefficient of the error correction term, CointEq(−1), is −0.424372 and is highly significant at the 1% level (p = 0.0000). This negative and statistically significant coefficient confirms the existence of a long-run equilibrium relationship among the variables included in the model. The magnitude of −0.424 indicates that approximately 42.4% of the short-run disequilibrium from the previous period is corrected within the current period. In other words, when crude oil prices deviate from their long-run equilibrium path due to short-term shocks, about 42% of that imbalance is adjusted back toward equilibrium each period. This relatively moderate adjustment speed suggests that the system converges to its long-run equilibrium at a steady pace rather than instantaneously. The statistical significance and correct negative sign of the error correction term provide strong evidence of stable long-run dynamics in the ARDL model, validating the cointegrating relationship among crude oil prices (Brent) and the selected macroeconomic and financial variables. Since the coefficient is more than -1, the model is stable and the model will correct itself monotonically in the long run.

The recursive residual stability tests were conducted using the CUSUM - stability of parameters and CUSUM of Squares (CUSUMSQ), stability of variance procedures to evaluate the structural stability of the ARDL model over the sample period. The results, as shown in Figures, indicate that the plotted blue lines remain within the 5% significance boundaries, represented by the dashed red lines, throughout the sample period.



**Coefficient Diagnostics (Long-run and short-run dynamics)**

The long-run coefficients reveal that Brent exerts a strong and positive influence on WTI prices, with a coefficient of 0.424 that is highly significant. This implies that Brent and WTI crude oil prices move closely together over time, indicating long-run market integration. In contrast, gold, EPU, and USDINR are statistically insignificant in the long run, suggesting that these variables do not have stable equilibrium relationships with WTI. The coefficient of KOL is negative and significant, showing that higher coal prices tend to reduce WTI prices in the long run, possibly reflecting substitution effects between energy sources.

In the short-run dynamics, changes in Brent prices have the most significant effect on WTI, with a coefficient of 0.946 that is highly significant and positive. Lagged changes in gold and EPU have negative and significant effects, indicating that increases in gold prices and policy uncertainty tend to lower WTI prices in the subsequent period. 

A delayed positive effect is observed from KOL after three lags, suggesting that changes in coal prices influence crude oil markets with a lag, possibly due to gradual substitution and adjustment processes within the energy sector. In contrast, exchange rate fluctuations, represented by USDINR, do not exhibit a statistically significant short-run impact on WTI prices.

Overall, the results suggest a stable long-run equilibrium among WTI, Brent, and KOL, with Brent emerging as the dominant variable influencing oil price dynamics. In the short run, oil prices respond primarily to Brent fluctuations and are moderately affected by uncertainty and gold price movements. The significant and negative coefficient of the lagged WTI term supports the presence of a well-functioning adjustment mechanism, meaning that short-run deviations from equilibrium tend to self-correct over time. These findings confirm that WTI prices are both influenced by global oil market interactions and sensitive to broader economic conditions, though the primary driver remains the co-movement with Brent prices.





