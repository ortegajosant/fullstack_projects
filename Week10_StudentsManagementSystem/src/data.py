import csv
from os.path import exists


def export_to_csv(file_path, students, fieldnames):
    result = False
    if not students:
        print("No data to export.")
        return
    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        result = True
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the file path.")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
    return result


def import_from_csv(file_path):
    empty_list = []
    if not exists(file_path):
        print(f"No data file found at {file_path}. Please export data first.")
        return empty_list
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]
            return students
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the file path.")
        return empty_list
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
        return empty_list
