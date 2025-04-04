import src.data as data
from src.StudentModel import Student

SUBJECTS = ["Spanish", "English", "Social Studies", "Science"]
FIELDNAMES = [
    "name",
    "group",
    "spanish",
    "english",
    "social studies",
    "science",
    "average",
]
CSV_EXTENSION = ".csv"
DEFAULT_FILE_PATH = f"students_data{CSV_EXTENSION}"

data_file_path = DEFAULT_FILE_PATH
students = []


def show_student_average_grade(student):
    print(f"Name: {student.name}, Average Grade: {student.average:.2f}")


def initialize_students_data():
    global students
    print("Initialization of students data file is required.")
    print("Whould you like to initialize the data file? (y/n)")
    choice = input()
    if choice.strip().lower() == "y":
        success = import_data()
        if success:
            return
    print("No file is loaded, initializing students as default.")
    students = []


def insert_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_student():
    if len(students) == 0:
        initialize_students_data()

    name = input("Enter the student's name: ")
    group = input("Enter the student's group: ")

    grades = {}
    for subject in SUBJECTS:
        grades[subject.lower()] = insert_grade(subject)

    student = Student(name, group, grades)
    students.append(student)
    print(f"Student {name} added successfully.")


def view_students():
    if not students:
        print("No students have been added yet.")
        return
    for student in students:
        print(f"Name: {student.name}\nGroup: {student.group}\nGrades:")
        for subject, grade in student.grades.items():
            print(f"\t{subject.capitalize()}: {grade}")
        print()


def calculate_averages():
    if not students:
        print("No students have been added yet.")
        return
    for student in students:
        show_student_average_grade(student)


def get_sorted_students_by_average_grade():
    # This can be done more efficiently using the built-in `sorted` function
    # however, I used the selection sort algorithm just to refresh the knowledge
    sorted_students = students[:]
    for i in range(len(sorted_students)):
        max_idx = i
        for j in range(i + 1, len(sorted_students)):
            if sorted_students[j].average > sorted_students[max_idx].average:
                max_idx = j
        sorted_students[i], sorted_students[max_idx] = (
            sorted_students[max_idx],
            sorted_students[i],
        )
    return sorted_students


def get_sorted_students_by_average_grade():
    return sorted(students, key=lambda student: student.average, reverse=True)


def top_students():
    if not students:
        print("No students have been added yet.")
        return

    sorted_students = get_sorted_students_by_average_grade()
    print("Top 3 Students:")
    for student in sorted_students[:3]:
        show_student_average_grade(student)


def create_student(student_data):
    grades = {subject: float(student_data[subject.lower()]) for subject in SUBJECTS}
    student = Student(student_data["name"], student_data["group"], grades)
    return student


def get_students_from_imported_csv(data):
    imported_students = []
    for student_data in data:
        imported_students.append(create_student(student_data))
    return imported_students


def import_data():
    global students, data_file_path
    file_path = input(
        f"Enter the file path to import (leave empty for default: {data_file_path}): "
    ).strip()
    if not file_path:
        file_path = data_file_path
    else:
        data_file_path = file_path

    imported_data = data.import_from_csv(file_path)
    if imported_data:
        imported_students = get_students_from_imported_csv(imported_data)
        students.extend(imported_students)
        print(f"Data successfully imported from {file_path}.")
        return True
    print("No data was imported. The file might be empty or invalid.")
    return False


def export_data():
    global data_file_path
    print(f"Current data file path is: {data_file_path}")
    print("Would you like to use this path? (y/n)")
    choice = input().strip().lower()
    if choice != "y" and len(choice) != 0:
        while True:
            file_path = input("Enter a valid file path to export the data: ").strip()
            if file_path.endswith(CSV_EXTENSION):
                data_file_path = file_path
                break
            else:
                print("Invalid file path. Please provide a path to a .csv file.")
    is_written = data.export_to_csv(
        data_file_path, [student.to_dict() for student in students], FIELDNAMES
    )
    if is_written:
        print(f"Data successfully exported to {data_file_path}.")
    else:
        print("Failed to export data. Please check the file path and try again.")
