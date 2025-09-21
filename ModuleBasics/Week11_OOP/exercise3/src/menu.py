import src.actions as actions


def display_menu():
    print("Student Management CLI")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Averages")
    print("4. View Top 3 Students")
    print("5. Import Students from CSV")
    print("6. Export Students to CSV")
    print("0. Exit")


def get_user_choice():
    choice = input("Please select an option: ")
    return choice


def validate_choice(choice, valid_options):
    return choice in valid_options


def handle_menu_choice(choice):
    if choice == "1":
        actions.add_student()
    elif choice == "2":
        actions.view_students()
    elif choice == "3":
        actions.calculate_averages()
    elif choice == "4":
        actions.top_students()
    elif choice == "5":
        actions.import_data()
    elif choice == "6":
        actions.export_data()
    elif choice == "0":
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True
