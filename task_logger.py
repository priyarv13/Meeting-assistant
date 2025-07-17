import json
import os

TASK_FILE = "tasks.json"

def save_task_entry(name, email, task, date, status="Scheduled"):
    task_data = {
        "name": name,
        "email": email,
        "task": task,
        "date": date,
        "status": status
    }

    # Load existing tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            all_tasks = json.load(f)
    else:
        all_tasks = []

    all_tasks.append(task_data)

    # Save back
    with open(TASK_FILE, "w") as f:
        json.dump(all_tasks, f, indent=4)

    print(f"📦 Task saved for {name}")
