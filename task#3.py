import json
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

TASK_FILE = "tasks.json"
tasks: list[dict] = []

# ==================== Utility Functions ====================

def load_tasks():
    """Load tasks from file and ensure all keys exist."""
    global tasks
    try:
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    # Ensure backward compatibility (auto-fix missing fields)
    for t in tasks:
        t.setdefault("title", "Untitled Task")
        t.setdefault("priority", "Medium")
        t.setdefault("due_date", "N/A")
        t.setdefault("created_at", datetime.now().strftime("%Y-%m-%d %H:%M"))
        t.setdefault("completed", False)

def save_tasks():
    """Save tasks safely to JSON."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def colored(text, color):
    return color + text + Style.RESET_ALL

# ==================== Core Features ====================

def add_task():
    title = input(colored("📝 Enter task title: ", Fore.CYAN)).strip()
    if not title:
        print(colored("❌ Task title cannot be empty!", Fore.RED))
        return

    priority = input(colored("Set priority (Low/Medium/High): ", Fore.YELLOW)).capitalize() or "Medium"
    due_date = input(colored("Set due date (YYYY-MM-DD) or leave blank: ", Fore.CYAN)).strip()

    task = {
        "title": title,
        "priority": priority if priority in ["Low", "Medium", "High"] else "Medium",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "due_date": due_date if due_date else "N/A",
        "completed": False
    }

    tasks.append(task)
    save_tasks()
    print(colored(f"✅ Task '{title}' added successfully!", Fore.GREEN))

def view_tasks(sorted_by=None):
    """Display tasks in the console with optional sorting."""
    if not tasks:
        print(colored("No tasks found.", Fore.YELLOW))
        return

    if sorted_by == "priority":
        order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(tasks, key=lambda t: order.get(t["priority"], 4))
    elif sorted_by == "date":
        sorted_tasks = sorted(tasks, key=lambda t: t["created_at"])
    else:
        sorted_tasks = tasks

    print(colored("\n📋 Your To-Do List:", Fore.MAGENTA))
    for i, task in enumerate(sorted_tasks, 1):
        status = "✔️ Done" if task["completed"] else "⏳ Pending"
        color = Fore.GREEN if task["completed"] else Fore.CYAN
        print(f"{color}{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']} | {status}")

def mark_completed():
    """Mark a selected task as done."""
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input(colored("Enter task number to mark completed: ", Fore.CYAN)))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks()
            print(colored(f"🎉 Task '{tasks[num-1]['title']}' marked as completed!", Fore.GREEN))
        else:
            print(colored("Invalid number.", Fore.RED))
    except ValueError:
        print(colored("Please enter a valid number.", Fore.RED))

def remove_task():
    """Remove a task by its index."""
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input(colored("Enter task number to delete: ", Fore.CYAN)))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print(colored(f"🗑️ Task '{removed['title']}' deleted successfully.", Fore.GREEN))
        else:
            print(colored("Invalid number.", Fore.RED))
    except ValueError:
        print(colored("Please enter a valid number.", Fore.RED))

def search_task():
    """Search tasks by title keyword."""
    keyword = input(colored("🔍 Enter keyword to search: ", Fore.CYAN)).lower()
    results = [t for t in tasks if keyword in t["title"].lower()]
    if results:
        print(colored("\nSearch Results:", Fore.MAGENTA))
        for i, task in enumerate(results, 1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{i}. {task['title']} ({task['priority']}) — {status}")
    else:
        print(colored("No matching tasks found.", Fore.YELLOW))

def show_summary():
    """Show analytics-style summary."""
    total = len(tasks)
    completed = sum(t["completed"] for t in tasks)
    pending = total - completed
    print(colored("\n📊 Task Summary:", Fore.BLUE))
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    if total > 0:
        progress = (completed / total) * 100
        print(f"Progress: {progress:.2f}% ✅")

def reminder_check():
    """Alert user if tasks are due today."""
    now = datetime.now().strftime("%Y-%m-%d")
    due_today = [t for t in tasks if t.get("due_date") == now and not t.get("completed", False)]
    if due_today:
        print(colored("\n⏰ Reminder! Tasks due today:", Fore.YELLOW))
        for t in due_today:
            print(f"➡️ {t['title']} (Priority: {t.get('priority', 'Medium')})")

# ==================== Main Menu ====================

def main():
    load_tasks()
    reminder_check()
    while True:
        print(colored("\n==== TO-DO LIST PRO 2025 ====", Fore.LIGHTBLUE_EX))
        print("1️⃣  Add Task")
        print("2️⃣  View Tasks")
        print("3️⃣  View Sorted by Priority")
        print("4️⃣  View Sorted by Date")
        print("5️⃣  Search Task")
        print("6️⃣  Mark Task Completed")
        print("7️⃣  Remove Task")
        print("8️⃣  Show Summary")
        print("9️⃣  Exit")

        choice = input(colored("Enter your choice: ", Fore.CYAN)).strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks(sorted_by="priority")
        elif choice == "4":
            view_tasks(sorted_by="date")
        elif choice == "5":
            search_task()
        elif choice == "6":
            mark_completed()
        elif choice == "7":
            remove_task()
        elif choice == "8":
            show_summary()
        elif choice == "9":
            print(colored("💡 Exiting... Have a productive day!", Fore.GREEN))
            time.sleep(1)
            break
        else:
            print(colored("❌ Invalid option. Try again.", Fore.RED))

if __name__ == "__main__":
    main()
