import tkinter as tk
from tkinter import messagebox
import task_manger_main as core

def gui_add_task():
    def save_task():
        name = name_entry.get()
        desc = desc_entry.get()
        priority = priority_var.get()
        due_date = date_entry.get()

        if not name or not desc or not priority or not due_date:
            messagebox.showerror("Error", "All fields are required.")
            return

        task = [name, desc, priority.lower(), due_date]
        core.tasks.append(task)
        core.save_tasks_to_file()
        messagebox.showinfo("Success", "Task added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Task")
    add_window.geometry("300x300")

    tk.Label(add_window, text="Task Name").pack()
    name_entry = tk.Entry(add_window, width=30)
    name_entry.pack()

    tk.Label(add_window, text="Description").pack()
    desc_entry = tk.Entry(add_window, width=30)
    desc_entry.pack()

    tk.Label(add_window, text="Priority").pack()
    priority_var = tk.StringVar()
    priority_menu = tk.OptionMenu(add_window, priority_var, "High", "Medium", "Low")
    priority_menu.pack()

    tk.Label(add_window, text="Due Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(add_window, width=30)
    date_entry.pack()

    tk.Button(add_window, text="Save Task", command=save_task).pack(pady=10)

def gui_view_tasks():
    core.load_tasks_from_file()
    display = ""
    for i, task in enumerate(core.tasks, 1):
        display += f"{i}. {task[0]} | {task[1]} | {task[2].capitalize()} | {task[3]}\n"
    if not display:
        display = "No tasks available."
    messagebox.showinfo("Task List", display)

def gui_update_task():
    core.update_task()

def gui_delete_task():
    core.delete_task()

def start_gui():
    window = tk.Tk()
    window.title("Task Manager")
    window.geometry("300x300")

    tk.Label(window, text="Task Manager GUI", font=("Arial", 16)).pack(pady=10)

    tk.Button(window, text="Add Task", width=20, command=gui_add_task).pack(pady=5)
    tk.Button(window, text="View Tasks", width=20, command=gui_view_tasks).pack(pady=5)
    tk.Button(window, text="Update Task", width=20, command=gui_update_task).pack(pady=5)
    tk.Button(window, text="Delete Task", width=20, command=gui_delete_task).pack(pady=5)
    tk.Button(window, text="Exit", width=20, command=window.destroy).pack(pady=20)

    core.load_tasks_from_file()
    window.mainloop()

if __name__ == "__main__":
    start_gui()