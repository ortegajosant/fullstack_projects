import src.menu as menu
import src.actions as actions


def main():
    while True:
        menu.display_menu()
        choice = menu.get_user_choice()
        program_continues = menu.handle_menu_choice(choice)
        if not program_continues:
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()
