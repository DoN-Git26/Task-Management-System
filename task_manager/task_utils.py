from datetime import datetime
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

tasks = []


def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title. It cannot be empty.")
        return
    if not validate_task_description(description):
        print("Invalid description. It cannot be empty.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date. Use format YYYY-MM-DD.")
        return
    tasks.append({
        "title": title,
        "description": description,
        "due_date": datetime.strptime(due_date, "%Y-%m-%d"),
        "completed": False,
    })
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int) or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [(i, t) for i, t in enumerate(tasks, 1) if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    for i, t in pending:
        print(f"{i}. {t['title']} - {t['description']} "
              f"(Due: {t['due_date'].strftime('%Y-%m-%d')})")


def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        progress = sum(1 for t in tasks if t["completed"]) / len(tasks) * 100
    print(f"Progress: {progress:.2f}%")
    return progress
