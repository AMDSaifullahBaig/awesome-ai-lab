# Support Vector Machine (SVM)

A practical exploration of Support Vector Machine classification using
scikit-learn.

## Objective

Understand how Support Vector Machines separate classes using a decision
boundary and how the `C` parameter affects the model.

The experiment also uses feature scaling because SVM is sensitive to the
scale of input features.

---

## What is SVM?

Support Vector Machine (SVM) is a supervised learning algorithm used
primarily for classification.

The basic idea is to find a decision boundary (hyperplane) that separates
different classes while maximizing the margin between the classes.

For a linear SVM, the decision boundary can be represented as:

w · x + b = 0

where:

- `w` = weight vector
- `x` = input feature vector
- `b` = bias

---

## Margin

The margin is the distance between the decision boundary and the closest
data points from each class.

The points closest to the decision boundary are called **support vectors**.

For a linear SVM, the margin width is:

Margin = 2 / ||w||

Therefore, maximizing the margin is equivalent to minimizing:

1/2 ||w||²

subject to the training points being correctly separated.

---

## Soft-Margin SVM

Real-world datasets are not always perfectly separable.

SVM therefore allows some observations to violate the margin by introducing
slack variables.

The optimization problem can be written as:

Minimize:

1/2 ||w||² + C Σ ξᵢ

subject to:

yᵢ(w · xᵢ + b) ≥ 1 - ξᵢ

and:

ξᵢ ≥ 0

where:

- `ξᵢ` = slack variable for observation `i`
- `C` = penalty parameter
- `w` = weight vector
- `b` = bias
- `yᵢ` = class label

---

## The C Parameter

`C` controls how strongly the model penalizes classification errors and
margin violations.

### Small C

A smaller `C` allows more violations of the margin.

This gives the model more tolerance for incorrectly classified or
margin-violating observations.

### Large C

A larger `C` places a stronger penalty on errors.

The model therefore tries harder to classify the training observations
correctly.

Conceptually:

Small C → wider margin, more tolerance for errors

Large C → stronger penalty for errors

---

## Feature Scaling

SVM can be sensitive to the scale of the features.

For example, suppose one feature ranges from:

0 to 1

while another ranges from:

0 to 10,000

The larger-scale feature can have a much greater influence on the
optimization process.

Therefore, features are commonly standardized before training.

### Standardization

The standardization formula is:

z = (x - μ) / σ

where:

- `x` = original feature value
- `μ` = mean of the feature
- `σ` = standard deviation of the feature
- `z` = standardized value

After standardization, each feature has approximately:

Mean = 0

Standard deviation = 1

In the experiment, `StandardScaler` was used.

```python
scaler = StandardScaler()

train_x_scaled = scaler.fit_transform(train_x)
test_x_scaled = scaler.transform(test_x)