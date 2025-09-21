import csv
from os.path import exists


def export_to_csv(file_path, students, fieldnames):
    if not students:
        print("No data to export.")
        return False
    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        return True
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
        return False


def import_from_csv(file_path):
    if not exists(file_path):
        print(f"No data file found at {file_path}. Please export data first.")
        return []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
        return []
