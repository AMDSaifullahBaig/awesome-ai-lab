# 01 — Elbow Method

## Overview

The **Elbow Method** is a technique used with **K-Means clustering** to estimate a suitable number of clusters.

K-Means requires the number of clusters to be specified beforehand:

```python
KMeans(n_clusters=k)

Dataset Information
Property	Value
Number of samples	150
Number of features	4
Number of classes	3
Task	Unsupervised clustering
Dataset source	sklearn.datasets
```

Inertia

Inertia is the sum of squared distances between each sample and the centroid of the cluster to which it belongs.

The formula is:

J=i=1∑n	​∣∣xi	​−ck(i)	​∣∣2

Where:

$J$ = inertia
$n$ = number of samples
$x_i$ = data point $i$
$c_{k(i)}$ = centroid assigned to point $i$

For multiple features:

J=i=1∑n	​j=1∑m	​(xij	​−ck(i)j​)2

Where:

$m$ = number of features
$x_{ij}$ = feature j of sample i
$c_{k(i)j}$ = feature j of the centroid assigned to sample i
Interpretation of Inertia

A smaller inertia means that the points are closer to their assigned centroids.

Therefore:

Low inertia
    ↓
Points are closer to their centroids
    ↓
More compact clusters

However, there is an important problem.

Increasing K generally decreases inertia.

Therefore, we cannot simply choose the value of K with the lowest inertia.

# Silhouette Score

The **Silhouette Score** evaluates how well each data point fits within
its assigned cluster compared with the nearest neighboring cluster.

For each point:

- `a(i)` = average distance from the point to points in its own cluster.
- `b(i)` = average distance from the point to points in the nearest other cluster.

The silhouette value is:

$$
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}
$$

The score ranges from:

$$
-1 \leq s(i) \leq 1
$$

### Interpretation

- Close to `+1` → point is well separated from other clusters.
- Around `0` → point lies near a cluster boundary.
- Negative → point may be assigned to the wrong cluster.

The overall `silhouette_score()` is the average silhouette value across
all samples.

In this experiment:

- `K = 2` → approximately **0.67**
- `K = 3` → approximately **0.55**

Therefore, according to the Silhouette Score, **K = 2 produces better
separated clusters than K = 3** for this dataset.

This differs from the Elbow Method, which suggested approximately
`K = 3`.

This demonstrates that different clustering evaluation methods can
recommend different values of `K`.