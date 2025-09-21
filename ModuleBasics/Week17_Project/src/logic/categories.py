from src.utils.json_file_handler import save_file, load_file
from os.path import join, exists


CATEGORIES_FILE = "categories.json"
CATEGORIES_KEY = "categories"


def validate_category(category, categories):
    category = category.strip()
    if not category:
        raise ValueError("Category cannot be empty.")
    elif category in categories:
        raise ValueError("Category already exists.")
    return True


def save_categories(base_dir, categories):
    file_path = join(base_dir, CATEGORIES_FILE)
    category_data = {CATEGORIES_KEY: categories}

    save_file(file_path, category_data)


def load_categories(base_dir):
    try:
        file_path = join(base_dir, CATEGORIES_FILE)
        category_data = load_file(file_path)
    except FileNotFoundError:
        save_categories(base_dir, [])
        category_data = {CATEGORIES_KEY: []}
    except Exception as e:
        raise Exception(f"Error loading categories: {e}")
    if CATEGORIES_KEY not in category_data:
        raise ValueError("Invalid category data format.")
    return category_data[CATEGORIES_KEY]
