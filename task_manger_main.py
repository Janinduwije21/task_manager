tasks = []

def load_tasks_from_file():
    tasks.clear()
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                if len(task_data) == 4:
                    tasks.append(task_data)
        print("Tasks loaded successfully!")
    except:
        print("No saved tasks found.")

def save_tasks_to_file():
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(",".join(task) + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task():
    more = "y"
    while more == "y":
        name = input("Enter task name: ")
        description = input("Enter task description: ")

        priority = input("Enter task priority |High, Medium, Low|: ").lower()
        while priority not in ["high", "medium", "low"]:
            print("Invalid priority!")
            priority = input("Enter task priority |High, Medium, Low|: ")

        while True:
            due_date = input("Enter task due date |YYYY-MM-DD|: ")
            date_parts = due_date.split("-")

            if len(date_parts) != 3:
                print("Invalid format! Please enter date in YYYY-MM-DD format.")
                continue

            try:
                month = int(date_parts[1])
                day = int(date_parts[2])

                if not (1 <= month <= 12):
                    print("Invalid month! Must be between 1 and 12.")
                    continue

                if not (1 <= day <= 31):
                    print("Invalid day! Must be between 1 and 31.")
                    continue

                break
            except ValueError:
                print("Invalid date! Please enter numeric values in YYYY-MM-DD format.")

        task = [name, description, priority, due_date]
        tasks.append(task)
        print("Task added successfully!")

        save_tasks_to_file()
        more = input("Do you want to enter More Data? (y/n): ").lower()
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}.\n Task Name = {task[0]}\n task Description = {task[1]}\n Priority = {task[2]}\n Due: {task[3]}")

def update_task():
    if len(tasks) == 0:
        print("No tasks available")
        return

    view_tasks()
    task_number = input("\nEnter task number to update: ")

    try:
        task_number = int(task_number)
        task = tasks[task_number - 1]

        task[0] = input("Enter new task name: ")
        task[1] = input("Enter new task description: ")
        priority = input("Enter new priority (High, Medium, Low): ").lower()
        while priority not in ["high", "medium", "low"]:
            print("Invalid priority! Try again.")
            priority = input("Enter new priority (High, Medium, Low): ").lower()
        task[2] = priority
        task[3] = input("Enter new due date (YYYY-MM-DD): ")

        print("Task updated successfully!")
        save_tasks_to_file()
    except IndexError:
        print("Invalid task number!")

def delete_task():
    if len(tasks) == 0:
        print("No tasks available")
        return

    view_tasks()
    task_number = input("\nEnter task number to delete: ")

    try:
        task_number = int(task_number)
        task = tasks[task_number - 1]
        tasks.remove(task)
        print("Task deleted successfully!")
        save_tasks_to_file()
    except IndexError:
        print("Invalid task number!")


if __name__ == "_main_":
    load_tasks_from_file()
    while True:
        menu = """
        |Task Manager Main Menu|
        |----------------------|
            |1. Add Task    |
            |2. View Tasks  |
            |3. Update Task |
            |4. Delete Task |
            |5. Exit        |
        """
        print(menu)
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter a number between 1-5")