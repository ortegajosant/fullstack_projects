from src.utils.json_file_handler import save_file, load_file
from os.path import join


MOVEMENTS_FILE = "movements.json"


def validate_new_movement(title, amount, category):
    if not title.strip() or not amount.strip() or not category.strip():
        raise ValueError("All fields are required.")
    elif not amount.replace(".", "", 1).isdigit():
        raise ValueError("Amount must be a valid number.")

    return True


def save_movements(base_dir, movements):
    file_path = join(base_dir, MOVEMENTS_FILE)
    movement_data = [movement.to_dict() for movement in movements]
    save_file(file_path, movement_data)


def load_movements(base_dir):
    try:
        file_path = join(base_dir, MOVEMENTS_FILE)
        movements_data = load_file(file_path)
    except FileNotFoundError:
        movements_data = []
        save_file(file_path, movements_data)
    except Exception as e:
        raise Exception(f"Error loading movements: {e}")
    return movements_data
