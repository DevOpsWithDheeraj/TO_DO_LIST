import tkinter as tk
from tkinter import messagebox

tasks = []  # List to store tasks

# --- Functions --- #
def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        tasks.append(task)
        update_list()
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        del tasks[selected_index]
        update_list()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete!")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_list()

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# --- GUI --- #
root = tk.Tk()
root.title("To-Do List")
root.geometry("320x400")
root.config(bg="#f0f8ff")

tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=10)

# Input box
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="#F44336", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_all, bg="#FF9800", fg="white", width=15).pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()

