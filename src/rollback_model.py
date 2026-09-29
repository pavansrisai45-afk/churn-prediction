import json

file_path = "models/registry/model_registry.json"

with open(file_path, "r") as file:
    registry = json.load(file)

registry["random_forest"]["v1"]["stage"] = "production"
registry["random_forest"]["v2"]["stage"] = "validation"

with open(file_path, "w") as file:
    json.dump(registry, file, indent=4)

print("Rollback completed successfully.")
print("V1 stage: production")
print("V2 stage: validation")