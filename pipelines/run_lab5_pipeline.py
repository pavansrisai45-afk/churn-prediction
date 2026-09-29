import subprocess
import sys

print("=========================================")
print("Starting Lab 5: Data Validation Pipeline")
print("=========================================")

scripts = [
    "src/validate_data.py",
    "src/validate_processed_data.py"
]

for script in scripts:

    print(f"\nRunning {script}...")

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:
        print(f"Pipeline failed at {script}.")
        sys.exit(1)

print("\nLab 5 Pipeline completed successfully!")