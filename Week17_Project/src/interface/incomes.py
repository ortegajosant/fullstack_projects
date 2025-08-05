import FreeSimpleGUI as sg
from src.entities.FinanceHandler import FinanceHandler

TITLE_KEY = "title"
AMOUNT_KEY = "amount"
CATEGORY_KEY = "category"
SAVE_KEY = "Save"
CANCEL_KEY = "Cancel"


def open_add_income_subwindow(finance_handler: FinanceHandler):
    if not finance_handler.categories:
        sg.popup_error("You must add at least one category before recording an income!")
        return

    layout = [
        [sg.Text("Income Title:"), sg.Input(key=TITLE_KEY)],
        [sg.Text("Amount:"), sg.Input(key=AMOUNT_KEY)],
        [
            sg.Text("Category:"),
            sg.Combo(finance_handler.categories, key=CATEGORY_KEY, readonly=True),
        ],
        [sg.Button(SAVE_KEY), sg.Button(CANCEL_KEY)],
    ]

    subwindow = sg.Window("Add Income", layout, modal=True)
    while True:
        event, values = subwindow.read()
        if event in (sg.WINDOW_CLOSED, CANCEL_KEY):
            break
        elif event == SAVE_KEY:
            try:
                finance_handler.add_income(
                    title=values[TITLE_KEY],
                    amount=values[AMOUNT_KEY],
                    category=values[CATEGORY_KEY],
                )
                sg.popup("Income added successfully!")
            except ValueError as e:
                sg.popup_error(f"Error adding income: {e}")
                continue
            break

    subwindow.close()
