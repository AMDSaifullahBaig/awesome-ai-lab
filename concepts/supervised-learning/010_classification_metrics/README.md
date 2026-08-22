# Classification Metrics

A practical exploration of common classification evaluation metrics using
scikit-learn.

## Objective

Understand how to evaluate a classification model using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The experiment uses Logistic Regression on the Iris dataset.

---

## Why Do We Need Multiple Metrics?

A model can make many correct predictions while still performing poorly
for a particular class.

Accuracy alone does not always tell us where the model is making mistakes.

Different metrics answer different questions:

| Metric | Main Question |
|---|---|
| Accuracy | How many predictions were correct overall? |
| Precision | When the model predicts positive, how often is it correct? |
| Recall | How many actual positive cases did the model find? |
| F1 Score | How well are precision and recall balanced? |
| Confusion Matrix | Which classes were predicted correctly or incorrectly? |

---

# 1. Confusion Matrix

For a binary classification problem, predictions can be divided into four
categories:

```text
                    Actual
                 Positive  Negative

Predicted Positive    TP       FP
Predicted Negative    FN       TN