## Overview

**DBSCAN** stands for **Density-Based Spatial Clustering of Applications
with Noise**.

It is an unsupervised learning algorithm that forms clusters based on
the **density of data points**.

Unlike K-Means, DBSCAN does not require the number of clusters to be
specified beforehand.

Its main advantage is that it can also identify **noise/outlier points**.

---

# DBSCAN Parameters (Quick Reference)

DBSCAN has two key parameters: **`eps`** and **`min_samples`**. They define what constitutes a "dense region."

---

## 1. `eps` (Neighborhood Radius)

- **What it does:** Maximum distance between two samples to be considered neighbors.
- **Type:** Positive float (e.g., `0.1`, `0.5`, `1.0`).
- **Effect of increasing it:** Larger neighborhoods → more points become connected → clusters grow or merge.
- **Effect of decreasing it:** Smaller neighborhoods → fewer connections → more points become noise.
- **No universal best value** – depends on feature scale, density, and distance metric.

---

## 2. `min_samples` (Density Threshold)

- **What it does:** Minimum number of points required within `eps` for a point to be a **core point**.
- **Type:** Integer (e.g., `3`, `5`, `10`).
- **Effect of increasing it:** Requires denser regions → fewer core points → more noise.
- **Effect of decreasing it:** Easier to form dense regions → more clusters may form.
- **No universal best value** – depends on dataset size, noise level, and dimensionality.

---

## Relationship

`eps` and `min_samples` work together:

- `eps` = how far to look.
- `min_samples` = how many points are needed to call it "dense."

---

## Critical: Feature Scaling

Since `eps` is a distance, features on larger scales dominate.  
**Always scale your data** (e.g., with `StandardScaler`) before applying DBSCAN.

---

## Point Types

| Type | Description |
| :--- | :--- |
| **Core** | Has ≥ `min_samples` points within `eps`. |
| **Border** | Not a core point, but lies within `eps` of a core point. |
| **Noise** | Neither core nor border (labeled `-1`). |

---

## Summary Table

| Parameter | Meaning | Type | Increase Effect |
| :--- | :--- | :--- | :--- |
| `eps` | Neighbor radius | Float | More connections, larger clusters |
| `min_samples` | Min. density | Integer | More noise, fewer core points |

---

## Mental Model

- **`eps`** → How far do I look?
- **`min_samples`** → How many points do I need to call it dense?
- **DBSCAN** → Find dense regions, mark sparse points as noise.