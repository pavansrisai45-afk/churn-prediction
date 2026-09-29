import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("data/raw/churn.csv")

X = data.drop("Churn", axis=1)
y = data["Churn"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

mlflow.set_experiment("Churn Prediction - Experiment 4")

with mlflow.start_run():

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    mlflow.log_param("model", "Random Forest")
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("random_state", 42)
    mlflow.log_param("dataset", "data/raw/churn.csv")
    mlflow.log_param("dataset_rows", len(data))
    mlflow.log_param("dataset_columns", len(data.columns))
    mlflow.log_param("preprocessing", "One-hot encoding")

    data.to_csv("data/processed/mlflow_processed_data.csv", index=False)
    mlflow.log_artifact("data/processed/mlflow_processed_data.csv")

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)

    mlflow.sklearn.log_model(
        model,
        "model",
        skops_trusted_types=["sklearn.tree._tree.Tree"]
    )

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

print("MLflow experiment completed successfully.")