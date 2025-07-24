import FreeSimpleGUI as sg
from .movements import layout_movements
from .expenses import open_add_expense_subwindow

TITLE_LAYOUT = [sg.Text("Tabla de movimientos financieros")]
BUTTONS_LAYOUT = [
    sg.Button("Agregar Gasto"),
    sg.Button("Agregar Ingreso"),
    sg.Button("Agregar Categoría"),
    sg.Button("Salir"),
]


def run_gui():
    layout = [TITLE_LAYOUT, layout_movements, BUTTONS_LAYOUT]
    ventana = sg.Window("Gestor de Finanzas Personales", layout)

    while True:
        layout = layout_movements
        evento, valores = ventana.read()
        if evento == sg.WINDOW_CLOSED or evento == "Salir":
            break
        elif evento == "Agregar Gasto":
            open_add_expense_subwindow(["Comida", "Transporte", "Salud"])
        elif evento == "Agregar Ingreso":
            sg.popup("Aquí iría la ventana para agregar un ingreso")
        elif evento == "Agregar Categoría":
            sg.popup("Aquí iría la ventana para agregar una categoría")

    ventana.close()
