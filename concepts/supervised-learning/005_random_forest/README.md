# Random Forest

A practical exploration of Random Forest classification using
scikit-learn.

## Objective

Understand how Random Forest extends Decision Trees by combining
multiple decision trees and investigate the effect of the number of
trees on model performance.

## Random Forest

Random Forest is an ensemble learning algorithm that combines the
predictions of multiple Decision Trees.

For classification, the individual trees contribute predictions and
the forest combines them to produce the final class prediction.

## Key Concept

### n_estimators

`n_estimators` specifies the number of Decision Trees in the Random
Forest.

For example:

```python
RandomForestClassifier(n_estimators=100)