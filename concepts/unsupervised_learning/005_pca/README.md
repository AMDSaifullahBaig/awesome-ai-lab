# PCA – Principal Component Analysis (Complete README)

## What is PCA?
**Principal Component Analysis (PCA)** is an unsupervised dimensionality reduction technique. It transforms a dataset with many features into fewer **principal components** that retain as much variance (information) as possible.

**Goal:** Reduce dimensions while preserving maximum variance.

---

## Dataset Used (Iris)
- **Samples:** 150
- **Original Features:** 4 (sepal length, sepal width, petal length, petal width)
- **Classes:** 3 (not used; PCA is unsupervised)

```python
from sklearn.datasets import load_iris
data = load_iris()
x = data.data      # PCA applied here
y = data.target    # Not used for PCA
```

# Core Mathematical Concepts

## Variance
Measures spread of a single feature:

$$ Var(X) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2 $$

## Covariance
Measures how two features change together:

$$ Cov(X,Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) $$

- **Positive:** X ↑, Y ↑
- **Negative:** X ↑, Y ↓
- **Zero:** No linear relationship

## Covariance Matrix
For 4 features, a 4×4 matrix where:

- Diagonal = variance of each feature
- Off-diagonal = covariance between feature pairs

---

# Key Takeaways

- **Variance** → spread of a feature
- **Covariance** → relationship between two features
- **Eigenvectors** → directions (PCs)
- **Eigenvalues** → variance captured
- **PC1** → maximum variance; **PC2** → next highest
- **Explained Variance Ratio** → helps choose `n_components`
- On Iris, 2 PCs retain ~97.77% variance
- PCA is **unsupervised** (no labels used)
- **Always scale features** before PCA if units differ