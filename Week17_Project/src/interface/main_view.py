import FreeSimpleGUI as sg
from src.interface.movements import generate_movements_layout, TABLE_KEY
from src.interface.expenses import open_add_expense_subwindow
from src.interface.incomes import open_add_income_subwindow
from src.interface.categories import open_add_category_subwindow
from src.entities.FinanceHandler import FinanceHandler

# CONSTANTS
INCOME_BUTTON_KEY = "income_button"
EXPENSE_BUTTON_KEY = "expense_button"
CATEGORY_BUTTON_KEY = "category_button"
ADD_EXPENSE_BUTTON_TEXT = "Agregar Gasto"
ADD_INCOME_BUTTON_TEXT = "Agregar Ingreso"
ADD_CATEGORY_BUTTON_TEXT = "Agregar Categoría"
EXIT_BUTTON_TEXT = "Salir"

# LAYOUTS
BUTTONS_LAYOUT = [
    sg.Button(ADD_EXPENSE_BUTTON_TEXT, key=EXPENSE_BUTTON_KEY),
    sg.Button(ADD_INCOME_BUTTON_TEXT, key=INCOME_BUTTON_KEY),
    sg.Button(ADD_CATEGORY_BUTTON_TEXT, key=CATEGORY_BUTTON_KEY),
    sg.Button(EXIT_BUTTON_TEXT),
]

TITLE_LAYOUT = [sg.Text("Tabla de movimientos financieros")]


def update_movements_table(window, movements_list):
    window.find_element(TABLE_KEY).update(values=movements_list)


def create_window(finance_handler: FinanceHandler):
    layout_movements = generate_movements_layout(finance_handler.movements)
    layout = [TITLE_LAYOUT, layout_movements, BUTTONS_LAYOUT]
    window = sg.Window("Gestor de Finanzas Personales", layout)
    return window


def run_gui(finance_handler: FinanceHandler):
    window = create_window(finance_handler)
    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == EXIT_BUTTON_TEXT:
            break
        elif event == EXPENSE_BUTTON_KEY:
            open_add_expense_subwindow(finance_handler)
            update_movements_table(window, finance_handler.movements)
        elif event == INCOME_BUTTON_KEY:
            open_add_income_subwindow(finance_handler)
            update_movements_table(window, finance_handler.movements)
        elif event == CATEGORY_BUTTON_KEY:
            open_add_category_subwindow(finance_handler)

    window.close()
