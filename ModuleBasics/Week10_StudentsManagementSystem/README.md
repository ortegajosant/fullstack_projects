# Student Management CLI

This project is a command-line interface application for managing student information. It allows users to add, view, and manage student data, including calculating averages and identifying top-performing students.

## Features

- Add student information
- View all students
- Calculate average grades
- Determine the top 3 students based on their average grades
- Import and export student data to and from CSV files

## Project Structure

```
.
├── src          
│   ├── menu.py          # Menu logic and user input handling
│   ├── actions.py       # Actions related to student management
│   ├── data.py          # Data import/export functionality
│   └── __init__.py      # Package initialization
├── main.py              # Entry point of the application source code
└── README.md            # Project documentation
```

## Usage

To run the application, execute the following command in your terminal:

```
python main.py
```

Follow the on-screen menu to navigate through the different functionalities of the application.
