# src/main.py
from storage import load_tasks, save_tasks
from task_manager import add_task, list_tasks, mark_completed, delete_task

DATA_FILE = "data/tasks.json"


def print_menu() -> None:
    print("\n=== TASK MANAGER ===")
    print("1) Add a new task")
    print("2) View tasks")
    print("3) Mark task as completed")
    print("4) Delete a task")
    print("5) Exit")


def show_tasks(tasks) -> None:
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- Your Tasks ---")
    for t in tasks:
        status = "✅ Done" if t.get("completed") else "⏳ Pending"
        print(f"ID: {t.get('id')} | {status} | {t.get('title')}")
        if t.get("description"):
            print(f"   Description: {t.get('description')}")
        if t.get("created_at"):
            print(f"   Created: {t.get('created_at')}")
        print("-" * 30)


def read_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("❌ Please enter a valid number.")


def main() -> None:
    tasks = load_tasks(DATA_FILE)

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter description (optional): ").strip()
            try:
                task = add_task(tasks, title, description)
                save_tasks(DATA_FILE, tasks)
                print(f"✅ Task added (ID: {task['id']})")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == "2":
            show_tasks(list_tasks(tasks))

        elif choice == "3":
            task_id = read_int("Enter task ID to mark completed: ")
            if mark_completed(tasks, task_id):
                save_tasks(DATA_FILE, tasks)
                print("✅ Task marked completed.")
            else:
                print("❌ Task ID not found.")

        elif choice == "4":
            task_id = read_int("Enter task ID to delete: ")
            if delete_task(tasks, task_id):
                save_tasks(DATA_FILE, tasks)
                print("✅ Task deleted.")
            else:
                print("❌ Task ID not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
