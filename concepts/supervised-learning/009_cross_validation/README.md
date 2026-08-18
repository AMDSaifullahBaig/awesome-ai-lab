# Cross Validation

A practical exploration of K-Fold Cross Validation using scikit-learn.

## Objective

Understand how Cross Validation evaluates a machine learning model using
multiple train-validation splits instead of relying on a single train-test
split.

---

## What is Cross Validation?

Cross Validation is a model evaluation technique used to estimate how well
a machine learning model performs on unseen data.

Instead of creating only one training and testing split, the dataset is
divided into multiple parts called **folds**.

In K-Fold Cross Validation, the dataset is divided into `K` folds.

For example, with 5-fold Cross Validation:

```text
Fold 1   Fold 2   Fold 3   Fold 4   Fold 5

 Test     Train    Train    Train    Train
 Train    Test     Train    Train    Train
 Train    Train    Test     Train    Train
 Train    Train    Train    Test     Train
 Train    Train    Train    Train    Test