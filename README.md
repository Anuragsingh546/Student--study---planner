# Student Study Planner (Command-Line Python Project)

A small command-line application for keeping track of study tasks. It lets a user add tasks, view them, mark them complete, and delete them. Tasks are saved locally in `tasks.json`.

## Features
- Add a task with an optional due date and priority.
- View all tasks and their status.
- Mark a task as complete.
- Delete a task by its ID.
- Save data between runs using JSON.
- Uses only the Python standard library (no third-party packages).

## Requirements
- Python 3.9 or newer
- A terminal / command prompt

## Setup and run
1. Download or clone this repository.
2. Open a terminal in the project folder (the folder containing `main.py`).
3. Check Python is installed:
   ```bash
   python --version
   ```
   On some systems, use `python3 --version`.
4. No dependency installation is required because the project uses Python's standard library.
5. Run the program:
   ```bash
   python main.py
   ```
   If needed, use `python3 main.py`.
6. Follow the menu shown in the terminal. The program creates `tasks.json` automatically when a task is saved.

## Example workflow
1. Choose `1` and enter a task title, due date (or leave blank), and priority.
2. Choose `2` to view tasks and note the task ID.
3. Choose `3` and enter that ID to mark it complete.
4. Choose `4` and enter an ID to remove a task.
5. Choose `5` to exit.

## Project files
- `main.py` — application source code.
- `tasks.json` — created automatically to store task data.
- `PROJECT_REPORT.docx` — project report document.

## Notes
This is a learning project. Before submitting, run it yourself, understand the functions, and personalize the project and report based on your own work and the official course instructions. The course instruction document was not included in the message, so compare this structure with that document before submitting.
