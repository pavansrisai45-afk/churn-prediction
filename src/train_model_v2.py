import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data/raw/churn.csv")

X = data.drop("Churn", axis=1)
y = data["Churn"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

os.makedirs("models/random_forest_v2", exist_ok=True)

joblib.dump(
    model,
    "models/random_forest_v2/random_forest_v2.pkl"
)

print("Model Version 2 trained successfully.")
print("Model: random_forest")
print("Version: v2")
print("n_estimators: 300")
print("max_depth: 10")
print("Model saved successfully.")