# Decision Tree

A practical exploration of Decision Tree classification using scikit-learn.

## Objective

Understand how a Decision Tree makes predictions using a sequence of
decision rules and investigate how the maximum tree depth affects model
performance.

## Decision Tree

A Decision Tree is a supervised learning algorithm that makes predictions
by repeatedly splitting the data based on feature values.

The tree consists of:

- **Root Node** — the starting point of the tree
- **Decision Nodes** — conditions used to split the data
- **Branches** — outcomes of the decisions
- **Leaf Nodes** — final predicted classes

## Key Concept

### Maximum Depth

`max_depth` controls the maximum number of levels allowed in the tree.

A small depth produces a simpler model, while a larger depth allows the
tree to learn more complex patterns.

Increasing the depth too much can cause the model to learn the training
data too closely, resulting in overfitting.

## Feature Scaling

Feature scaling is not required for Decision Trees because the model
makes decisions using feature thresholds rather than distance calculations.

This differs from algorithms such as KNN, where feature scaling can have
a significant effect on the distance calculations.

## Experiment

Different values of `max_depth` were tested and training and testing
accuracy were compared.

The depth was increased up to 30 to observe how model performance changed.

### Observation

Test accuracy increased as the tree depth increased initially and reached
approximately **96% around a depth of 8**.

Increasing the depth beyond this point did not produce a noticeable
improvement in test accuracy for this dataset and train/test split.

## What I Practiced

- Decision Tree classification
- Train/test splitting
- `DecisionTreeClassifier`
- Controlling tree depth with `max_depth`
- Training and testing accuracy
- Visualizing model performance
- Observing the effect of model complexity

## Tools

- Python
- NumPy
- Matplotlib
- scikit-learn

## Status

Completed