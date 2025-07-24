# Personal Finance Manager

## Overview

This project is a **graphical application** built with the `FreeSimpleGUI` library to help users manage their personal finances easily. The application is designed to reinforce key concepts from Module 1, including:

- **Modularization**: Code is organized into logical modules.
- **File Handling**: Data is saved and loaded automatically.
- **Validation**: User input is validated for correctness.
- **Functions**: Logic is split into reusable functions.
- **Object-Oriented Programming (OOP)**: Main entities are represented as classes.
- **Separation of Logic and Presentation**: UI and business logic are kept separate.

---

## Features

- **Movements Table**: Displays all expenses and incomes.
- **Add Category**: Button opens a window to create new categories (e.g., Food, Transport, Entertainment).
- **Add Expense**: Button opens a window to enter expense details (title, amount, category).
- **Add Income**: Button opens a window to enter income details (title, amount, category).
- **Error Handling**: Shows an error message if trying to add an expense/income without available categories.

---

## Data Persistence

- All changes are **automatically saved** to files.
- On startup, the app **loads previously saved data** if available.

---

## Development Guidelines

- Use **classes** for main entities: `Movimiento`, `Categoria`, `GestorFinanzas`, etc.
- Split logic into **small, reusable functions**.
- Organize code into **modules**: `interfaces.py`, `logica.py`, `persistencia.py`, etc.
- Use **clear identifiers** for variables, functions, and classes.
- Apply **basic validations** in all forms.
- Implement **unit tests** for core logic and validations.

---

## Unit Testing

- At least **8 unit tests** are required.
- Focus tests on **business logic and important validations**.
- Organize tests in a separate file, e.g., `test_logica.py`.

---

## Getting Started

1. Install dependencies:  
   `pip install FreeSimpleGUI`
2. Run the application:  
   `python main.py`
3. Run tests:  
   `python -m unittest test_logica.py`

---

## File Structure Example

```
Week17_Project/
├── src/
│   ├── ...
│   └── main.py
├── test/
│   └── ...
├── data/
│   └── ...
└── README.md
```

---

## Author

Created by [Your Name].  
Contact: [your.email@example.com]