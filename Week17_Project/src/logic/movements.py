from utils.json_file_handler import save_file


MOVEMENTS_FILE = "movements.json"
CATEGORIES_FILE = "categories.json"


def validate_new_movement(title, amount, category):
    if not title or not amount or not category:
        raise ValueError("All fields are required.")
    elif not amount.replace(".", "", 1).isdigit():
        raise ValueError("Amount must be a valid number.")

    return True


def save_movements(movements):
    movement_data = [movement.get_movement_info() for movement in movements]
    save_file(MOVEMENTS_FILE, movement_data)
