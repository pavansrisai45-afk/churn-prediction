import subprocess
import sys

print("=========================================")
print("Starting Lab 6: Model Registry")
print("=========================================")

scripts = [
    "src/train_model_v2.py",
    "src/evaluate_model_v2.py",
    "src/model_registry.py",
    "src/manage_model_stage.py",
    "src/promote_model.py",
    "src/rollback_model.py"
]

for script in scripts:

    print(f"\nRunning {script}...")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Pipeline failed at {script}.")
        sys.exit(1)

print("\nLab 6 Model Registry Pipeline completed successfully!")