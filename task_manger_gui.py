import tkinter as tk
from tkinter import messagebox
import task_manager_main as core

def gui_add_task():
    core.add_task()

def gui_view_tasks():
    core.load_tasks_from_file()
    display = ""
    for i, task in enumerate(core.tasks, 1):
        display += f"{i}. {task[0]} | {task[1]} | {task[2].capitalize()} | {task[3]}\n"
    if not display:
        display = "No tasks available."
    messagebox.showinfo("Task List", display)
