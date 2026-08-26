# 002 — Hierarchical Clustering

## Overview

**Hierarchical Clustering** is an unsupervised learning technique that
builds a hierarchy of clusters.

Unlike K-Means, where we start by choosing the number of clusters and
then find their centroids, hierarchical clustering starts with individual
data points and progressively combines them into larger clusters.

This experiment uses **Agglomerative Hierarchical Clustering**, which
follows a bottom-up approach.

---

# Dataset

This experiment uses the **Iris dataset** from scikit-learn.

The Iris dataset contains measurements of 150 Iris flowers belonging to
three known species.

| Property | Value |
|---|---:|
| Samples | 150 |
| Features | 4 |
| Known classes | 3 |
| Learning type | Unsupervised |
| Dataset | Iris |

### Features

The four features are:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The feature matrix is:

$$
X \in \mathbb{R}^{150 \times 4}
$$
# Linkage Methods in Hierarchical Clustering

Linkage determines **how the distance between two clusters is calculated**.

When Agglomerative Clustering has to decide which two clusters to merge,
different linkage methods use different definitions of "distance".

---

## 1. Single Linkage

### Idea

Single linkage uses the **minimum distance** between any two points
belonging to the two clusters.

In simple words:

> Find the closest pair of points between the two clusters.

### Formula

For clusters $A$ and $B$:

$$
D(A,B)=
\min_{x\in A,\;y\in B} d(x,y)
$$

Where:

- $A$ = first cluster
- $B$ = second cluster
- $d(x,y)$ = distance between two points

### Example

```text
Cluster A          Cluster B

● ● ●                ● ● ●
      \              /
       \____________/
        closest pair
```

### 2. Complete Linkage
## Idea

Complete linkage uses the maximum distance between any two points
belonging to the two clusters.

#### In simple words:

Find the farthest pair of points between the two clusters.

## Formula
D(A,B)=
x∈A,y∈B
max
	​

d(x,y)

Example
Cluster A          Cluster B


● ● ●              ● ● ●
|                    |
|____________________|
       
farthest pair

The distance is determined by the most distant pair.

## Advantage

Tends to produce more compact and evenly sized clusters.

## Disadvantage

A single distant point can strongly affect the distance between clusters.

sklearn
AgglomerativeClustering(
    n_clusters=3,
    linkage="complete"
)
# 3. Average Linkage
## Idea

Average linkage calculates the average distance between every point
in one cluster and every point in the other cluster.

#### In simple words:

Don't look only at the closest or farthest points. Consider all
pairwise distances and take their average.

### Formula
D(A,B)=∣A∣∣B∣1x∈A∑	​y∈B∑	​d(x,y)

Where:

$|A|$ = number of points in cluster A
$|B|$ = number of points in cluster B
$d(x,y)$ = distance between points
Example
```
Cluster A          Cluster B


● ● ●              ● ● ●


 \  |  /            \ | /
  \ | /              \|/
   distances
      ↓
    average
```
Instead of using only one pair of points, it considers all pairs.
## Advantage

Usually provides a balance between single and complete linkage.

## Disadvantage

More computationally expensive than simply considering one pair.
```
sklearn
AgglomerativeClustering(
    n_clusters=3,
    linkage="average"
)
```
## 4. Ward Linkage

Ward is slightly different from the other three.

Instead of directly defining cluster distance using a minimum,
maximum, or average pairwise distance, Ward linkage chooses the merge
that causes the smallest increase in within-cluster variance.

### Idea

Merge the two clusters that cause the smallest increase in overall
cluster variance.

Conceptually, it tries to keep clusters compact.

#### Objective

The idea is related to minimizing:

k=1∑K	​xi	​∈Ck	​∑	​∣∣xi	​−μk​∣∣2
Where:

$C_k$ = cluster
$x_i$ = data point
$\mu_k$ = centroid of the cluster
## Intuition

```
Good merge:


● ●       ● ●
 \         /
  \_______/
    compact




Bad merge:


● ●                 ●
 \                   |
  \__________________|
      large spread
```
Ward prefers the merge that produces the smaller increase in
within-cluster variation.

### Advantage

Often produces compact, well-separated clusters.

### Disadvantage

It is more restrictive than the other linkage methods and is designed
to work with Euclidean distance.
```
sklearn
AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)
```
## Quick Comparison
|Method|How cluster distance is calculated|

| Single | Minimum distance |
|--|--: |
| Complete |Maximum distance|
| Average |Average of all pairwise distances|
| Ward |Minimum increase in within-cluster variance|