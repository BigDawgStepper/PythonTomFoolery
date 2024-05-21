import tkinter as tk
import ctypes
import os
import time

def open_task_manager():
    time.sleep(0.3)
    os.system("start taskmgr")
    ctypes.windll.user32.MessageBoxW(0, "Task Manager is Running", "Multi Tool")
    
def open_system_information():
    time.sleep(0.3)
    os.system("start msinfo32")
    ctypes.windll.user32.MessageBoxW(0, "System Information is Running", "Multi Tool")          
    
def open_control_panel():
    time.sleep(0.3)
    os.system("start control")
    ctypes.windll.user32.MessageBoxW(0, "Control Panel is Running", "Multi Tool")
    
def open_notepad():
    time.sleep(0.3)
    os.system("start notepad")
    ctypes.windll.user32.MessageBoxW(0, "Notepad is Running", "Multi Tool")
    
def open_file_explorer():
    time.sleep(0.3)
    os.system("start explorer")
    ctypes.windll.user32.MessageBoxW(0, "File Explorer is Running", "Multi Tool")
    
def quit_button():
    time.sleep(0.3)
    ctypes.windll.user32.MessageBoxW(0,"!Bye thanks for using the tool hope it was useful for you", "Multi Tool")                                
    app.destroy()
    
def open_calculator():
    time.sleep(0.3)
    os.system("start calc")
    ctypes.windll.user32.MessageBoxW(0, "Calculator is Running", "Multi Tool")
    
def restart_computer():
    if os.name == 'nt':
        print("ANY UNSAVED DATA WILL BE LOST ON RESTART")
        print("15 seconds until restart")
        time.sleep(15)
        os.system('shutdown /r /t 1')
    else:
        print("Restart tool does not support your os.")
        
def open_settings():
    time.sleep(0.3)
    os.system("start ms-settings:")
    ctypes.windll.user32.MessageBoxW(0, "Settings is Running", "Multi Tool")
    
app = tk.Tk()
app.title("BigDawgSteppers Win MultiTool but GUI")
app.geometry('500x500')
app.resizable(False, False)
label_frame = tk.LabelFrame(app, text="Tools")
label_frame.pack(padx=80, pady=110)
label = tk.Label(label_frame).pack()
button1 = tk.Button(label_frame, text="Task Manager", width=17, bg='green', command=open_task_manager).pack()
button2 = tk.Button(label_frame, text="System Information", width=17, bg='green', command=open_system_information).pack()
button3 = tk.Button(label_frame, text="Control Panel", width=17, bg='green', command=open_control_panel).pack()
button4 = tk.Button(label_frame, text="Notepad", width=17, bg='green', command=open_notepad).pack()
button5 = tk.Button(label_frame, text="File Explorer", width=17, bg='green', command=open_file_explorer).pack()
button6 = tk.Button(label_frame, text="Calculator", width=17, bg='green', command=open_calculator).pack()
button7 = tk.Button(label_frame, text="System Restart", width=17, bg='green', command=restart_computer).pack()
button8 = tk.Button(label_frame, text="Windows Settings", width=17, bg='green', command=open_settings).pack()
button = tk.Button(label_frame, text="Quit", width=17, bg='red', command=quit_button).pack()

app.mainloop()
