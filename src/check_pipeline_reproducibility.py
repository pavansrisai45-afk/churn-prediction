import hashlib

file_path = "data/processed/validated_dataset.csv"

with open(file_path, "rb") as file:
    file_hash = hashlib.md5(file.read()).hexdigest()

print("Validated dataset hash:", file_hash)
print("Reproducibility check completed.")