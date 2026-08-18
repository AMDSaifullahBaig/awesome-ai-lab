# Gradient Boosting

A practical exploration of Gradient Boosting classification using
scikit-learn.

## Objective

Understand how Gradient Boosting builds an ensemble of decision trees
sequentially, with each new tree attempting to improve the existing model.

The experiments focus on `n_estimators` and `learning_rate`.

---

## What is Gradient Boosting?

Gradient Boosting is an ensemble learning method that combines multiple
weak learners, usually Decision Trees, to build a stronger predictive
model.

Unlike Random Forest, where trees are built independently, Gradient
Boosting builds trees sequentially.

The general process is:

Tree 1
  ↓
Calculate errors
  ↓
Tree 2 learns from the errors
  ↓
Update the model
  ↓
Tree 3 learns from remaining errors
  ↓
...
  ↓
Final model

Each new tree attempts to reduce the loss of the current model.

---

## Additive Model

Gradient Boosting builds the final model by adding weak learners
sequentially:

F_m(x) = F_(m-1)(x) + η h_m(x)

where:

- `F_m(x)` = model after adding the m-th tree
- `F_(m-1)(x)` = previous model
- `h_m(x)` = newly trained decision tree
- `η` = learning rate
- `m` = current boosting stage

The learning rate controls how strongly each new tree contributes to
the existing model.

---

## Loss Function

Gradient Boosting attempts to minimize a loss function.

In general:

L(y, F(x))

where:

- `y` = actual target
- `F(x)` = current model prediction
- `L` = loss function

The next weak learner is trained to move the model in a direction that
reduces this loss.

This is where the term **gradient boosting** comes from.

---

## n_estimators

`n_estimators` specifies the number of boosting stages, or trees, used
by the model.

For example:

```python
GradientBoostingClassifier(n_estimators=100)