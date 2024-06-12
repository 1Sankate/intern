
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("400x400")

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        tasks.remove(task)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)


task_entry = tk.Entry(input_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)


add_task_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)


task_listbox = tk.Listbox(root, height=15, width=50)
task_listbox.pack(pady=10)


remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=10)

root.mainloop()
