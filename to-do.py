import json
import os

tasks = []
TASKS_FILE = "tasks.json"

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
                # Ensure all task IDs are integers
                for task in tasks:
                    task['id'] = int(task.get('id', 0))
            except (json.JSONDecodeError, ValueError, KeyError):
                tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id():
    if not tasks:
        return 1
    valid_ids = [int(task.get('id', 0)) for task in tasks if str(task.get('id', '')).isdigit()]
    return max(valid_ids, default=0) + 1

def show_menu():
    print("\n--- To-do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Update Task")
    print("5. Delete Task") 
    print("6. Exit")

def task_exists(task_name):
    for task in tasks:
        if task["task"].lower() == task_name.lower():
            return True
    return False

def add_task():
    print("Enter tasks one by one. Type 'done' to stop.")
    while True:
        task = input("Task: ").strip()
        if task.lower() == 'done':
            break
        if task:
            if not task_exists(task):
                task_id = get_next_id()
                tasks.append({"id": task_id, "task": task, "done": False})
                print(f"✅ Task '{task}' added with ID {task_id}")
            else:
                print(f"⚠️ Task '{task}' already exists.")
    save_tasks()

def view_task():
    if not tasks:
        print("📭 No tasks yet!")
        return
    print("\n📋 Your Tasks:")
    for task in tasks:
        status = "✔ Done" if task["done"] else "✘ Not Done"
        print(f"🆔 {task['id']}: {task['task']} [{status}]")

def get_task_by_id(task_id):
    for task in tasks:
        if int(task["id"]) == task_id:
            return task
    return None

def mark_done():
    view_task()
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to mark as done: "))
        task = get_task_by_id(task_id)
        if task:
            task["done"] = True
            print(f"✅ Task '{task['task']}' marked as done!")
            save_tasks()
        else:
            print("❌ No task with that ID.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def update_task():
    view_task()
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to update: "))
        task = get_task_by_id(task_id)
        if task:
            new_task = input("Enter the updated task: ").strip()
            if new_task:
                task["task"] = new_task
                print("🔁 Task updated successfully!")
                save_tasks()
            else:
                print("⚠️ Task cannot be empty.")
        else:
            print("❌ No task with that ID.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = get_task_by_id(task_id)
        if task:
            tasks.remove(task)
            print(f"🗑️ Task '{task['task']}' deleted.")
            save_tasks()
        else:
            print("❌ No task with that ID.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Load tasks from file
load_tasks()

# Main menu loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        update_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")

