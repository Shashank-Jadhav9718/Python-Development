tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

while True:
    print("\n==== To-Do List App ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
