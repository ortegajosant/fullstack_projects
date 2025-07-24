import FreeSimpleGUI as sg

movements = []

# Key for the movements table
TABLE_KEY = "movements_table"
# Table headers
HEADERS = ["Title", "Amount", "Category", "Type"]

# Main window layout
layout_movements = [
    sg.Table(
        values=movements,
        headings=HEADERS,
        max_col_width=25,
        auto_size_columns=True,
        display_row_numbers=False,
        justification="center",
        num_rows=10,
        key=TABLE_KEY,
        row_height=25,
        enable_events=False,
    )
]
