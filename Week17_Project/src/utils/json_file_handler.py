import json


def load_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File not found: {file_path}, a new file will be created."
        )
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error decoding JSON from the file: {file_path}")


def save_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise IOError(f"Error saving to file: {e}")
