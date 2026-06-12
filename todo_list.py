import json
import os


class Color:
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"
    WHITE   = "\033[97m"
    MAGENTA = "\033[95m"


DATA_FILE = "tasks.json"

def load_tasks():
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, title):
   
    task = {
        "id"    : len(tasks) + 1,
        "task"  : title,
        "done"  : False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"\n{Color.GREEN}✔ Task added:{Color.RESET} '{title}'")

def view_tasks(tasks):
   
    print(f"\n{Color.BOLD}{Color.CYAN}{'─'*40}")
    print(f"  📋  YOUR TO-DO LIST")
    print(f"{'─'*40}{Color.RESET}")

    if not tasks:
        print(f"  {Color.YELLOW}No tasks yet. Add one!{Color.RESET}")
    else:
        for index, task in enumerate(tasks, start=1):
            status = f"{Color.GREEN}✔{Color.RESET}" if task["done"] else f"{Color.RED}○{Color.RESET}"
            title  = task["task"]
            print(f"  {Color.WHITE}{index}.{Color.RESET} {status}  {title}")

    print(f"{Color.CYAN}{'─'*40}{Color.RESET}\n")

def mark_done(tasks, number):
    """Mark a task as completed."""
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print(f"\n{Color.GREEN}✔ Task {number} marked as done!{Color.RESET}")
    else:
        print(f"\n{Color.RED}✘ Invalid task number.{Color.RESET}")

def delete_task(tasks, number):
    """Remove a task from the list."""
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        # Re-assign IDs to keep them consistent
        for i, task in enumerate(tasks, start=1):
            task["id"] = i
        save_tasks(tasks)
        print(f"\n{Color.RED}🗑 Deleted:{Color.RESET} '{removed['task']}'")
    else:
        print(f"\n{Color.RED}✘ Invalid task number.{Color.RESET}")

# ─────────────────────────────────────────
#  USER INTERFACE (View Layer)
# ─────────────────────────────────────────
def show_menu():
    print(f"\n{Color.BOLD}{Color.MAGENTA}{'═'*40}")
    print(f"   🚀  DECODELABs TO-DO ENGINE")
    print(f"{'═'*40}{Color.RESET}")
    print(f"  {Color.YELLOW}1.{Color.RESET} Add Task")
    print(f"  {Color.YELLOW}2.{Color.RESET} View Tasks")
    print(f"  {Color.YELLOW}3.{Color.RESET} Mark Task as Done")
    print(f"  {Color.YELLOW}4.{Color.RESET} Delete Task")
    print(f"  {Color.YELLOW}5.{Color.RESET} Exit")
    print(f"{Color.MAGENTA}{'═'*40}{Color.RESET}")


def main():
    tasks = load_tasks()  

    while True:
        show_menu()
        choice = input(f"  {Color.CYAN}Enter your choice (1-5): {Color.RESET}").strip()

        if choice == "1":
            title = input(f"  {Color.WHITE}Enter task: {Color.RESET}").strip()
            if title:
                add_task(tasks, title)
            else:
                print(f"\n{Color.RED}✘ Task cannot be empty.{Color.RESET}")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            try:
                num = int(input(f"  {Color.WHITE}Enter task number to mark done: {Color.RESET}"))
                mark_done(tasks, num)
            except ValueError:
                print(f"\n{Color.RED}✘ Please enter a valid number.{Color.RESET}")

        elif choice == "4":
            view_tasks(tasks)
            try:
                num = int(input(f"  {Color.WHITE}Enter task number to delete: {Color.RESET}"))
                delete_task(tasks, num)
            except ValueError:
                print(f"\n{Color.RED}✘ Please enter a valid number.{Color.RESET}")

        elif choice == "5":
            print(f"\n{Color.GREEN}👋 Goodbye! Keep building — DecodeLabs 🚀{Color.RESET}\n")
            break

        else:
            print(f"\n{Color.RED}✘ Invalid choice. Pick 1–5.{Color.RESET}")


if __name__ == "__main__":
    main()