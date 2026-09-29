import os
import json
from datetime import datetime

model_name = "random_forest"
version = "v2"

version_folder = "models/random_forest_v2"

metadata = {
    "model_name": model_name,
    "version": version,
    "stage": "validation",
    "created_at": datetime.now().isoformat(),
    "model_file": "random_forest_v2.pkl",
    "dataset": "data/raw/churn.csv",
    "processed_dataset": "data/processed/validated_dataset.csv",
    "preprocessing": [
        "One-hot encoding"
    ],
    "parameters": {
        "n_estimators": 300,
        "max_depth": 10,
        "random_state": 42
    },
    "metrics": {
        "accuracy": 0.730305,
        "precision": 0.533346,
        "recall": 0.730305,
        "f1_score": 0.616476
    }
}

os.makedirs(version_folder, exist_ok=True)

with open(f"{version_folder}/metadata.json", "w") as file:
    json.dump(metadata, file, indent=4)

print("Model Version 2 registered successfully.")
print("Model:", model_name)
print("Version:", version)
print("Stage: validation")
print("Metrics and lineage recorded.")