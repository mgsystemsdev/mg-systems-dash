

# 📘 Scikit-learn Cheat Sheet

**Machine Learning with Python**

---

## 1. Import & Setup

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
```

---

## 2. Data Splitting

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 3. Preprocessing

| Task           | Example                                | Use                  |
| -------------- | -------------------------------------- | -------------------- |
| Standardize    | `StandardScaler().fit_transform(X)`    | Mean=0, SD=1         |
| Min-Max Scale  | `MinMaxScaler().fit_transform(X)`      | Range 0–1            |
| One-hot encode | `OneHotEncoder().fit_transform(cats)`  | Categorical → binary |
| Label encode   | `LabelEncoder().fit_transform(labels)` | Labels → ints        |
| Imputation     | `SimpleImputer(strategy="mean")`       | Fill missing values  |

---

## 4. Common Models

### Linear Models

```python
from sklearn.linear_model import LinearRegression, LogisticRegression
```

* `LinearRegression()` → regression
* `LogisticRegression()` → classification

### Tree-Based

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
```

### Support Vector Machines

```python
from sklearn.svm import SVC, SVR
```

### Neighbors

```python
from sklearn.neighbors import KNeighborsClassifier
```

### Clustering

```python
from sklearn.cluster import KMeans
```

### Dimensionality Reduction

```python
from sklearn.decomposition import PCA
```

---

## 5. Training & Prediction

```python
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

## 6. Model Evaluation

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error, r2_score
```

| Metric                | Example                                | Task           |
| --------------------- | -------------------------------------- | -------------- |
| Accuracy              | `accuracy_score(y_test,y_pred)`        | Classification |
| Confusion Matrix      | `confusion_matrix(y_test,y_pred)`      | Classification |
| Classification Report | `classification_report(y_test,y_pred)` | Classification |
| MSE                   | `mean_squared_error(y_test,y_pred)`    | Regression     |
| R²                    | `r2_score(y_test,y_pred)`              | Regression     |

---

## 7. Cross-Validation

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

---

## 8. Pipelines

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression())
])
pipe.fit(X_train, y_train)
```

---

## 9. Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {"C":[0.1,1,10]}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X_train, y_train)
grid.best_params_
```

---

## 10. Beginner Pitfalls

* ❌ Forgetting to **scale features** for SVM/KNN/Logistic Regression.
* ❌ Using `.fit_transform()` on **train & test** separately (causes data leakage) → only fit on train.
* ❌ Not setting `random_state` → results vary each run.
* ❌ Blindly trusting accuracy → check confusion matrix for imbalanced data.

---

✅ With this, you have the **Scikit-learn essentials**: preprocessing, models, training, evaluation, pipelines, and tuning.

