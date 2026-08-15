# Logistic Regression

A practical exploration of Logistic Regression for binary classification using scikit-learn.

## Objective

Understand and practice the basic workflow of a classification model:

`Data → Train/Test Split → Model → Prediction → Evaluation`

## Logistic Regression

Logistic Regression estimates the probability of an observation belonging to a class.

The sigmoid function is:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

where:

$$
z = wx + b
$$

The output of the sigmoid lies between 0 and 1 and can be interpreted as a probability.

## Confusion Matrix

A confusion matrix summarizes classification results using:

- **TP (True Positive)** — correctly predicted positive cases
- **TN (True Negative)** — correctly predicted negative cases
- **FP (False Positive)** — negative cases incorrectly classified as positive
- **FN (False Negative)** — positive cases incorrectly classified as negative

## Accuracy

Accuracy measures the proportion of correct predictions:

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

## Feature Scaling

Feature scaling was tested to observe its effect on Logistic Regression.

`StandardScaler` was used to standardize the features:

$$
z = \frac{x-\mu}{\sigma}
$$

where:

- $x$ = original feature value
- $\mu$ = mean of the feature
- $\sigma$ = standard deviation

## Scaling Experiment

The model was trained and evaluated both with and without feature scaling.

| Approach | Classification Errors |
|----------|------------------------|
| Without scaling | 22 |
| With scaling | 12 |

### Observation

Feature scaling reduced the number of classification errors from **22 to 12** on the test set.

This demonstrated the practical effect of feature scaling on Logistic Regression when the input features have different scales.

## What I Practiced

- Binary classification
- Train/test splitting
- Logistic Regression with scikit-learn
- Feature scaling with `StandardScaler`
- Predictions
- Accuracy
- Confusion matrix
- Comparing scaled and unscaled models

## Tools

- Python
- NumPy
- Pandas
- Matplotlib
- scikit-learn

## Status

Completed