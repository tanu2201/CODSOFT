import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.configure(background="light grey")

        # Create frames
        self.frame_tasks = tk.Frame(self.root, bg="light grey")
        self.frame_tasks.pack(fill="both", expand=True)

        self.frame_buttons = tk.Frame(self.root, bg="light grey")
        self.frame_buttons.pack(fill="x")

        # Create task list
        self.task_list = tk.Listbox(self.frame_tasks, width=40, height=10, bg="white", fg="black")
        self.task_list.pack(side="left", fill="both", expand=True)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.frame_tasks)
        self.scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Create entry field
        self.entry_field = tk.Entry(self.frame_buttons, width=30, bg="white", fg="black")
        self.entry_field.pack(side="left", fill="x", expand=True)

        # Create buttons
        self.button_add = tk.Button(self.frame_buttons, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.button_add.pack(side="left", fill="x", expand=True)

        self.button_delete = tk.Button(self.frame_buttons, text="Delete Task", command=self.delete_task, bg="orange", fg="white")
        self.button_delete.pack(side="left", fill="x", expand=True)

        self.button_update = tk.Button(self.frame_buttons, text="Update Task", command=self.update_task, bg="blue", fg="white")
        self.button_update.pack(side="left", fill="x", expand=True)

        self.button_clear = tk.Button(self.frame_buttons, text="Clear All Tasks", command=self.clear_tasks, bg="purple", fg="white")
        self.button_clear.pack(side="left", fill="x", expand=True)

    def add_task(self):
        task = self.entry_field.get()
        if task:
            self.task_list.insert("end", task)
            self.entry_field.delete(0, "end")
            messagebox.showinfo("Success!", "Task added successfully!")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            messagebox.showinfo("Success!", "Task deleted successfully!")
        except:
            messagebox.showinfo("Error", "Select a task to delete")

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.entry_field.get()
            if task:
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.entry_field.delete(0, "end")
                messagebox.showinfo("Success!", "Task updated successfully!")
        except:
            messagebox.showinfo("Error", "Select a task to update")

    def clear_tasks(self):
        self.task_list.delete(0, "end")
        messagebox.showinfo("Success!", "All tasks cleared!")

root = tk.Tk()
app = ToDoList(root)
root.mainloop()
