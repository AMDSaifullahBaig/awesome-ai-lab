# Titanic Survival Prediction

## Overview
Predicting passenger survival on the Titanic using engineered features and a 
model comparison across classical ML and a custom neural net.

## Approach
- EDA: identified Sex, Pclass as strongest raw predictors
- Cleaning: grouped-median imputation for Age (by Pclass+Sex), HasCabin flag 
  for 77%-missing Cabin column
- Feature engineering: Title (extracted + grouped rare titles), FamilySize, 
  IsAlone
- Encoding: one-hot with train/test category alignment via combined encoding

## Model Comparison (5-fold CV)
| Model | CV Accuracy |
|---|---|
| Gradient Boosting | 82.7% ± 1.9% |
| Logistic Regression | 82.5% ± 2.2% |
| Random Forest | 80.1% ± 4.0% |
| Custom PyTorch NN | 71.9% ± 3.4% |

**Selected: Logistic Regression** — statistically tied with Gradient Boosting, 
simpler and more interpretable.

## Key Finding
A hand-tuned neural net looked promising on single-split validation (up to 89%), 
but proper cross-validation revealed it generalized worse (71.9%) than a 5-line 
Logistic Regression. This dataset (891 rows, largely linear relationships) 
didn't justify the added complexity — a good reminder that model capacity 
should match the data, not intuition about "more sophisticated = better."

## Result
Kaggle leaderboard score: 0.768 (public)

## What I'd try next
- Feature refinement on Ticket (shared-group signal)
- GridSearchCV tuning on regularization strength