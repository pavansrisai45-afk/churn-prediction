import pandas as pd

file_path = "data/processed/validated_dataset.csv"

df = pd.read_csv(file_path)

print("Starting Processed Data Validation...")

print("Dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nDuplicate records:", df.duplicated().sum())

print("\nTotalCharges datatype:", df["TotalCharges"].dtype)

print(
    "Invalid TotalCharges:",
    pd.to_numeric(df["TotalCharges"], errors="coerce").isna().sum()
)

print("\nProcessed data validation completed successfully.")