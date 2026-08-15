# K-Nearest Neighbors

A practical exploration of K-Nearest Neighbors (KNN) for classification.

## Objective

Understand how KNN classifies observations based on the nearest training
examples and investigate how the choice of K affects model performance.

## How KNN Works

KNN finds the K training observations closest to a new observation and
assigns the majority class among those neighbors.

For two points, Euclidean distance can be calculated as:

$$
d(x,y) = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

## Key Concepts

### K

K represents the number of neighbors considered when making a prediction.

- Small K → more sensitive to individual observations
- Large K → considers a broader neighborhood

### Feature Scaling

KNN relies on distance calculations, so features with larger numerical
scales can dominate the distance.

Standardization:

$$
z = \frac{x-\mu}{\sigma}
$$

## Experiment

Tested different values of K and compared their accuracy.


| K | Accuracy |
|---:|---:|
| 1 | 95.56% |
| 3 | 95.56% |
| 5 | 94.44% |
| 7 | 91.11% |
| 9 | 90.00% |
| 11 | 88.89% |

## What I Practiced

- Loading a classification dataset
- Train/test splitting
- Feature scaling
- KNN classification
- Choosing K
- Model evaluation
- Visualizing K vs accuracy

## Tools

- Python
- NumPy
- Matplotlib
- scikit-learn

## Status

Completed