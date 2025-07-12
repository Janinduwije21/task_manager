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
