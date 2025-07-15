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
    core.load_tasks_from_file()

    def load_task():
        try:
            index = int(task_number_entry.get()) - 1
            if index < 0 or index >= len(core.tasks):
                raise IndexError
            task = core.tasks[index]

            name_entry.delete(0, tk.END)
            name_entry.insert(0, task[0])
            desc_entry.delete(0, tk.END)
            desc_entry.insert(0, task[1])
            priority_var.set(task[2].capitalize())
            date_entry.delete(0, tk.END)
            date_entry.insert(0, task[3])
        except:
            messagebox.showerror("Error", "Invalid task number.")

    def save_update():
        index = int(task_number_entry.get()) - 1
        if index < 0 or index >= len(core.tasks):
            messagebox.showerror("Error", "Invalid task number.")
            return

        name = name_entry.get()
        desc = desc_entry.get()
        priority = priority_var.get()
        due_date = date_entry.get()

        if not name or not desc or not priority or not due_date:
            messagebox.showerror("Error", "All fields are required.")
            return

        core.tasks[index] = [name, desc, priority.lower(), due_date]
        core.save_tasks_to_file()
        messagebox.showinfo("Success", "Task updated successfully!")
        update_window.destroy()

    update_window = tk.Toplevel()
    update_window.title("Update Task")
    update_window.geometry("300x400")

    tk.Label(update_window, text="Enter Task Number to Update").pack()
    task_number_entry = tk.Entry(update_window, width=30)
    task_number_entry.pack()

    tk.Button(update_window, text="Load Task", command=load_task).pack(pady=5)

    tk.Label(update_window, text="Task Name").pack()
    name_entry = tk.Entry(update_window, width=30)
    name_entry.pack()

    tk.Label(update_window, text="Description").pack()
    desc_entry = tk.Entry(update_window, width=30)
    desc_entry.pack()

    tk.Label(update_window, text="Priority").pack()
    priority_var = tk.StringVar()
    priority_menu = tk.OptionMenu(update_window, priority_var, "High", "Medium", "Low")
    priority_menu.pack()

    tk.Label(update_window, text="Due Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(update_window, width=30)
    date_entry.pack()

    tk.Button(update_window, text="Save Update", command=save_update).pack(pady=10)


def gui_delete_task():
    core.load_tasks_from_file()

    def delete_selected():
        try:
            index = int(task_number_entry.get()) - 1
            if index < 0 or index >= len(core.tasks):
                raise IndexError
            deleted = core.tasks.pop(index)
            core.save_tasks_to_file()
            messagebox.showinfo("Deleted", f"Deleted task: {deleted[0]}")
            delete_window.destroy()
        except:
            messagebox.showerror("Error", "Invalid task number.")

    delete_window = tk.Toplevel()
    delete_window.title("Delete Task")
    delete_window.geometry("300x150")

    tk.Label(delete_window, text="Enter Task Number to Delete").pack(pady=10)
    task_number_entry = tk.Entry(delete_window, width=30)
    task_number_entry.pack()

    tk.Button(delete_window, text="Delete Task", command=delete_selected).pack(pady=10)


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