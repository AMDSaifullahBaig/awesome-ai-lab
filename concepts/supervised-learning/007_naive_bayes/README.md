# Naive Bayes

A practical exploration of Naive Bayes classification using scikit-learn.

## Objective

Understand how Naive Bayes uses probability and Bayes' theorem to classify
observations, and investigate the effect of `var_smoothing` on a Gaussian
Naive Bayes classifier.

---

## What is Naive Bayes?

Naive Bayes is a supervised learning algorithm based on **Bayes' theorem**.

It calculates the probability of a class given a set of observed features.

For classification:

P(C | X) = P(X | C) P(C) / P(X)

where:

- `P(C | X)` = probability of class C given the features X
- `P(X | C)` = probability of observing X given class C
- `P(C)` = prior probability of class C
- `P(X)` = probability of observing X

The classifier predicts the class with the highest posterior probability:

C* = argmax P(C | X)

---

## The "Naive" Assumption

Naive Bayes assumes that the features are conditionally independent
given the class.

For multiple features:

P(X | C) = P(x₁ | C) P(x₂ | C) ... P(xₙ | C)

Therefore:

P(C | X) ∝ P(C) ∏ P(xᵢ | C)

The independence assumption simplifies the calculation significantly.

Although the features may not actually be independent, Naive Bayes can
still perform well in many practical situations.

---

## Gaussian Naive Bayes

`GaussianNB` is designed for continuous numerical features.

It assumes that the values of each feature within each class follow a
Gaussian (normal) distribution.

The Gaussian probability density function is:

P(x | C) =
1 / sqrt(2πσ²) × exp(-(x - μ)² / (2σ²))

where:

- `x` = observed feature value
- `μ` = mean of the feature for the class
- `σ²` = variance of the feature for the class
- `σ` = standard deviation

The mean and variance are estimated from the training data.

---

## var_smoothing

`var_smoothing` is a parameter of `GaussianNB` that adds a small amount
of variance to improve numerical stability.

The parameter can be specified as:

```python
GaussianNB(var_smoothing=value)