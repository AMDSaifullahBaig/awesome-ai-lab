# Gaussian Mixture Models (GMM) — Quick README

## Overview
GMM is an **unsupervised soft clustering** algorithm. It models data as a mixture of multiple Gaussian (bell-shaped) probability distributions. Instead of assigning a point to a single cluster (like K-Means), GMM outputs the **probability** of belonging to each cluster.

---

## Dataset (Iris)
- **Samples:** 150
- **Features:** 4 (Sepal Length, Width, Petal Length, Width)
- **Known Classes:** 3 (not used during training)

---

## Core Concept

A Gaussian is defined by its mean ($\mu$) and variance ($\sigma^2$).  
GMM assumes the data comes from a weighted sum of $K$ Gaussians:

$$p(x) = \sum_{k=1}^{K} \pi_k \cdot \mathcal{N}(x \mid \mu_k, \Sigma_k)$$

- $\pi_k$ = weight of component $k$
- $\mu_k$ = mean (center)
- $\Sigma_k$ = covariance (spread & orientation)

---

## Hard vs Soft Clustering

| K-Means (Hard) | GMM (Soft) |
| :--- | :--- |
| Assigns 1 cluster | Assigns probabilities to *all* clusters |
| Uses centroids | Uses Gaussian distributions |
| `predict()` only | `predict()` + `predict_proba()` |

**Example (Soft):**  
Point X → Cluster 0: 80%, Cluster 1: 15%, Cluster 2: 5%.

---

## Code Example

```python
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

# Scale features (important!)
x_scaled = StandardScaler().fit_transform(x)

# Create model with 3 components
model = GaussianMixture(n_components=3, random_state=50)
model.fit(x_scaled)

# Get hard labels (highest probability)
labels = model.predict(x_scaled)

# Get soft probabilities
probs = model.predict_proba(x_scaled)

# Inspect learned parameters
print(model.means_)        # Centers
print(model.covariances_)  # Shapes/orientations
print(model.weights_)      # Component contributions
