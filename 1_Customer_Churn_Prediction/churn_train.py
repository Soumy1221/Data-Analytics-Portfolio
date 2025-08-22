# Customer Churn Prediction (synthetic dataset)
# Run: python churn_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("synthetic_telco_churn.csv")
df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

X = df.drop(columns=["customerID","Churn"])
y = df["Churn"]

cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
num_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

preprocess = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ("num", "passthrough", num_cols)
])

clf = Pipeline([
    ("prep", preprocess),
    ("model", LogisticRegression(max_iter=2000, n_jobs=None))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save predictions
preds = pd.DataFrame({"y_true": y_test, "y_pred": y_pred})
preds.to_csv("predictions.csv", index=False)
print("Saved predictions.csv")
