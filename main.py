"""
Student Study Planner — a command-line Python project.
Stores study tasks in a local JSON file.
"""

import json
from pathlib import Path
from datetime import date

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from JSON; return an empty list if the file does not exist."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read tasks.json. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to JSON."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    due_date = input("Due date (YYYY-MM-DD, or press Enter to skip): ").strip()
    if due_date:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return
    priority = input("Priority (low/medium/high): ").strip().lower()
    if priority not in {"low", "medium", "high"}:
        print("Invalid priority. Using medium.")
        priority = "medium"

    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({
        "id": next_id,
        "title": title,
        "due_date": due_date or "Not set",
        "priority": priority,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Study Tasks ---")
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(
            f'#{task["id"]} | {task["title"]} | Due: {task["due_date"]} '
            f'| Priority: {task["priority"]} | {status}'
        )


def complete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked complete.")
            return
    print("Task ID not found.")


def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f'“{removed["title"]}” deleted.')
            return
    print("Task ID not found.")


def show_menu():
    print("\n===== Student Study Planner =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
