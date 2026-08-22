# 011 - Regression Metrics

A practical exploration of common regression evaluation metrics using
scikit-learn.

## Objective

Understand how to evaluate a regression model using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The experiment uses Linear Regression on the Diabetes dataset.

---

## Why Regression Metrics?

In classification, predictions are usually evaluated as correct or
incorrect.

In regression, the prediction is a continuous value, so we need to
measure **how far the prediction is from the actual value**.

Different metrics measure this error in different ways.

---

## 1. Mean Absolute Error (MAE)

MAE calculates the average absolute difference between the actual and
predicted values.

### Formula

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

Where:

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $n$ = number of samples

### Intuition

MAE answers:

> How far away are my predictions from the actual values on average?

It treats all errors proportionally.

---

## 2. Mean Squared Error (MSE)

MSE calculates the average of the squared differences between actual and
predicted values.

### Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Squaring the errors makes larger errors much more significant.

For example:

$$
2^2 = 4
$$

while:

$$
10^2 = 100
$$

Therefore, MSE is more sensitive to large errors than MAE.

---

## 3. Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

### Formula

$$
RMSE = \sqrt{MSE}
$$

RMSE brings the error back to the same units as the target variable.

For example, if:

$$
MSE = 2500
$$

then:

$$
RMSE = \sqrt{2500} = 50
$$

RMSE is also more sensitive to large errors because it is based on
squared errors.

---

## 4. R² Score

R², or the coefficient of determination, measures how much of the
variation in the target variable is explained by the model.

### Formula

$$
R^2 = 1 -
\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
{\sum_{i=1}^{n}(y_i-\bar{y})^2}
$$

Where:

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $\bar{y}$ = mean of the actual target values

### Interpretation

Generally:

```text
R² = 1
→ Perfect predictions

R² = 0
→ No better than predicting the mean

R² < 0
→ Worse than predicting the mean