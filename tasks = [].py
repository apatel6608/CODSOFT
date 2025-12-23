tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to remove: "))
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Stay productive 💙")
        break
    else:
        print("Invalid choice. Please try again.")
