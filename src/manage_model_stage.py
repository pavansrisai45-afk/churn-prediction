import json
import os

registry = {
    "random_forest": {
        "v1": {
            "stage": "validation"
        },
        "v2": {
            "stage": "staging"
        }
    }
}

os.makedirs("models/registry", exist_ok=True)

with open("models/registry/model_registry.json", "w") as file:
    json.dump(registry, file, indent=4)

print("Model lifecycle registry created successfully.")
print("V1 stage: validation")
print("V2 stage: staging")