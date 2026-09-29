import json

file_path = "models/registry/model_registry.json"

with open(file_path, "r") as file:
    registry = json.load(file)

registry["random_forest"]["v2"]["stage"] = "production"
registry["random_forest"]["v1"]["stage"] = "validation"

with open(file_path, "w") as file:
    json.dump(registry, file, indent=4)

print("Model V2 promoted to production.")
print("V2 stage: production")
print("V1 stage: validation")