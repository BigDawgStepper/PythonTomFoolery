import tkinter as tk
import os

def open_task_manager():
    os.system("start taskmgr")
    label.config(text="Task Manager is running!")
    
app = tk.Tk()
app.title("BigDawgSteppers Win MultiTool but GUI")
label_frame = tk.LabelFrame(app, text="Tools")
label_frame.pack(padx=10, pady=10)
label = tk.Label(label_frame, text="Click the select button to open task manager")
label.pack()
button = tk.Button(label_frame, text="Task Manager", command=open_task_manager)
button.pack()

app.mainloop()
