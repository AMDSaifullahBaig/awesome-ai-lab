### Linear Regression

Linear regression models the relationship between input features and a
continuous target using a linear equation:

$$
\hat{y} = wx + b
$$

where:

- $w$ = coefficient/weight
- $b$ = intercept/bias
- $\hat{y}$ = predicted value

### Mean Squared Error (MSE)

MSE measures the average squared difference between the actual and
predicted values.

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

where:

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $n$ = number of observations

Lower MSE generally indicates smaller prediction errors.

### R² Score

R² (coefficient of determination) measures how much of the variation
in the target variable is explained by the model.

$$
R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
{\sum_{i=1}^{n}(y_i-\bar{y})^2}
$$

where:

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $\bar{y}$ = mean of the actual target values

A score of:

- **1.0** → perfect predictions
- **0.0** → no better than predicting the mean
- **< 0** → worse than simply predicting the mean