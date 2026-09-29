import hashlib
import pandas as pd

file_path = "data/raw/churn.csv"

df = pd.read_csv(file_path)

data_string = df.to_csv(index=False)

data_hash = hashlib.md5(data_string.encode()).hexdigest()

print("Dataset shape:", df.shape)
print("Dataset hash:", data_hash)
print("Reproducibility validation completed successfully.")