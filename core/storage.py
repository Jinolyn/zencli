import json
from pathlib inport Path 


def load_data(file_path: str):
    file = Path(file_path)
    if not file.exists():
        return []

    with open(file, "r") as f:
        json.load(f)


def save_data(file_path: str, data: list):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)