import FreeSimpleGUI as sg
from src.entities.FinanceHandler import FinanceHandler

NAME_KEY = "name"
SAVE_KEY = "Save"
CANCEL_KEY = "Cancel"


def open_add_category_subwindow(finance_handler: FinanceHandler):
    layout = [
        [sg.Text("Category Name:"), sg.Input(key=NAME_KEY)],
        [sg.Button(SAVE_KEY), sg.Button(CANCEL_KEY)],
    ]

    subwindow = sg.Window("Add Category", layout, modal=True)
    while True:
        event, values = subwindow.read()
        if event in (sg.WINDOW_CLOSED, CANCEL_KEY):
            break
        elif event == SAVE_KEY:
            try:
                finance_handler.add_category(name=values[NAME_KEY])
                sg.popup("Category added successfully!")
            except ValueError as e:
                sg.popup_error(f"Error adding category: {e}")
                continue
            break

    subwindow.close()
