from tkinter import *
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()

    if task != "":
        task_list.insert(END, "❌ " + task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def complete_task():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)

        if task.startswith("❌"):
            task = task.replace("❌", "✅", 1)
            task_list.delete(selected)
            task_list.insert(selected, task)

    except:
        messagebox.showwarning("Warning", "Select a task first!")

def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)

    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Window
root = Tk()
root.title("Smart To-Do List")
root.geometry("500x500")
root.resizable(False, False)

# Heading
title = Label(
    root,
    text="SMART TO-DO LIST",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Entry Frame
frame = Frame(root)
frame.pack(pady=10)

task_entry = Entry(frame, width=35, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=5)

add_btn = Button(
    frame,
    text="Add Task",
    command=add_task,
    width=12,
    bg="lightgreen"
)
add_btn.grid(row=0, column=1)

# Task List
task_list = Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 12)
)
task_list.pack(pady=20)

# Buttons Frame
btn_frame = Frame(root)
btn_frame.pack()

complete_btn = Button(
    btn_frame,
    text="Complete",
    command=complete_task,
    width=15,
    bg="lightblue"
)
complete_btn.grid(row=0, column=0, padx=10)

delete_btn = Button(
    btn_frame,
    text="Delete",
    command=delete_task,
    width=15,
    bg="salmon"
)
delete_btn.grid(row=0, column=1, padx=10)

root.mainloop()
