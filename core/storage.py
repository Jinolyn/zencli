import json
from pathlib import Path 


def load_data(file_path):
    """Load data from a JSON file."""
    if not Path(file_path).exists():
        return []
    with open(file_path, "r") as f:
        return json.load(f)


def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)