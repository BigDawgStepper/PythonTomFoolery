import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import webbrowser
import time
import os
import subprocess
import wmi

# Creating all the functions of the program

def Open_Discord():
    webbrowser.open(url,new=new)
    
def biosite():
    webbrowser.open(url2,new=new)
    
def mygithub():
    webbrowser.open(url3, new=new)
    
def taskmgr():
    time.sleep(0.3)
    os.system("start taskmgr")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Task Manager is Running!")
    
def ctrlpanel():
    time.sleep(0.3)
    os.system("start control")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Control Panel is Running!")
    
def notepad():
    time.sleep(0.3)
    os.system("start notepad")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Notepad is Running!")
    
def open_explorer():
    time.sleep(0.3)
    os.system("start explorer")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="File Explorer is Open!")
    
def open_settings():
    time.sleep(0.3)
    os.system("start ms-settings:")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Settings are Open!")

def open_display_settings():
    time.sleep(0.3)
    os.system("start ms-settings:display")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Display Settings are Open!")

def open_virus_settings():
    time.sleep(0.3)
    os.system("start windowsdefender:")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Virus Settings are Open!")
    
def open_reg_edit():
    time.sleep(0.3)
    os.system("start regedit")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Registry Edit is Running!")
    
def open_calculator():
    time.sleep(0.3)
    os.system("start calc")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Calculator is Open!")
    
def open_system_information():
    time.sleep(0.3)
    os.system("start msinfo32")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="System Info is Running!")
    
def restart_computer():
    if os.name == 'nt':
        tkinter.messagebox.showinfo(title="Multi Tool", message="Restarting in 15 seconds save any unsaved data!!")
        time.sleep(15)
        os.system('shutdown /r /t 1')
    else:
        tkinter.messagebox.showinfo(title="Multi Tool", message="Restart tool dosent support your os")
        
def open_cmd():
    time.sleep(0.3)
    os.system("start cmd")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Cmd is Running!")
    
def open_task_scheduler():
    time.sleep(0.3)
    os.system("start taskschd.msc")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="Task Scheduler is Running!")
    
def open_PowerShell():
    time.sleep(0.3)
    os.system("start PowerShell")
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Multi Tool", message="PowerShell is Running!")

def get_uuid():
    time.sleep(0.3)
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    time.sleep(0.3)
    tkinter.messagebox.showinfo(title="Multi Tool UUID Grabber", message=current_machine_id)

def get_gpu_serial_number():
    try:
        c = wmi.WMI()
        for gpu in c.Win32_VideoController():
            if hasattr(gpu, 'SerialNumber'):
                return gpu.SerialNumber 
    except Exception as e:
        print("Error:", e)
    return "Serial number not found"

def show_gpu_serial_number():
    serial_number = get_gpu_serial_number()
    tkinter.messagebox.showinfo(title="Multi Tool GPU Serial Grabber", message=serial_number,)

# Main settings of gui(title, size etc)
root = tk.Tk()
root.iconbitmap('C:/users/eac/Pictures/multitool.ico')
root.title("Multi Tool")
root.geometry("500x375")
root.resizable(False, False,)

# Choosing wether to open new tab or window then setting the actual url to goto
new = 1
url = "https://discord.gg/dbApbadrwD"
url2 = "https://fakecrime.bio/eac"
url3 = "https://github.com/BigDawgStepper"

# Creating main notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack(expand=1, fill='both')

# Adding the tabs to the notebook/packing them
my_tab1 = ttk.Frame(my_notebook)
my_notebook.add(my_tab1, text="Welcome")
my_tab2 = ttk.Frame(my_notebook)
my_notebook.add(my_tab2, text="Tools")
my_tab3 = ttk.Frame(my_notebook)
my_notebook.add(my_tab3, text="HWID")

# Tab 1 Labels
Label(my_tab1, text= "Welcome to BigDawgSteppers MultiTool", font= ('Helvetica 18 bold underline')).grid(row=0, column=0)
Label(my_tab1, text= "This Multi Tool has many features! Refer to the tabs at the top to locate tools!").grid(row=1, column=0)
Label(my_tab1, text= "Interested in my work or want to talk to me? Join the discord below!").grid(row=2, column=0)
Label(my_tab1, text= "You can join my disc using the button or copying this link! https://discord.gg/dbApbadrwD").grid(row=3, column=0)
Label(my_tab1, text= "Tool currently working for Win11 & Win10", font= ('Helvetica 18 bold')).grid(row=12, column=0)
Label(my_tab1, text= "Who is TheBigDawgStepper? Click the button below for more info...").grid(row=5, column=0)
Label(my_tab1, text= "This isnt the only tool ive made theres multiple version of this and more on my github!").grid(row=7, column=0)
Label(my_tab1, text= "^^^^AS OF 2024-05-22^^^^", font= ('Helvetica 18 bold')).grid(row=13, column=0)

# Tab 2 Labels
Label(my_tab2, text="Click a button to open the specified tool!", font= ('Helvetica 18 bold underline')).grid(row=0, column=0)
Label(my_tab2, text="HWID Checker on next tab!", font= ('Helvetica 16 bold underline')).grid(row=2, column=0)

# Tab 3 Labels
Label(my_tab3, text="HWID/Serial Checker | BigDawgStepper", font='Courier 16 bold underline').grid(row=0, column=0)

# Creating Frames
frame1 = Frame(my_tab2, width=450, height=450)
frame1.grid()
frame2 = Frame(my_tab3, padx=5, pady=5, width=450, height=450)
frame2.grid()

# Tab 1 Buttons
Button(my_tab1, text="Join my Discord Server Here!", padx=10, pady=10, command=Open_Discord).grid(row=8, column=0)
Button(my_tab1, text="Who even is TheBigDawgStepper?", padx=10, pady=10, command=biosite).grid(row=9, column=0)
Button(my_tab1, text="My github!", padx=10, pady=10, command=mygithub).grid(row=10, column=0)

# Tab 2 buttons
Button(frame1, text="Open Task Manager", padx=5, pady=5, command=taskmgr).grid(row=0, column=0, sticky="ew")
Button(frame1, text="Open Control Panel", padx=5, pady=5, command=ctrlpanel).grid(row=1, column=0, sticky="ew")
Button(frame1, text="Open Notepad", padx=5, pady=5, command=notepad).grid(row=2, column=0, sticky="ew")
Button(frame1, text="Open File Explorer", padx=5, pady=5, command=open_explorer).grid(row=3, column=0, sticky="ew")
Button(frame1, text="Open Settings", padx=5, pady=5, command=open_settings).grid(row=3, column=1, sticky="ew")
Button(frame1, text="Display Settings", padx=5, pady=5, command=open_display_settings).grid(row=2, column=1, sticky="ew")
Button(frame1, text="Virus Settings", padx=5, pady=5, command=open_virus_settings).grid(row=0, column=1, sticky="ew")
Button(frame1, text="Registry Edit", padx=5, pady=5, command=open_reg_edit).grid(row=1, column=1, sticky="ew")
Button(frame1, text="Open Calculator", padx=5, pady=5, command=open_calculator).grid(row=5, column=0, sticky="ew")
Button(frame1, text="Open System Info", padx=5, pady=5, command=open_system_information).grid(row=5, column=1, sticky="ew")
Button(frame1, text="Restart Computer", padx=5, pady=5, command=restart_computer).grid(row=6, column=0, sticky="ew")
Button(frame1, text="Open CMD", padx=5, pady=5, command=open_cmd).grid(row=6, column=1, sticky="ew")
Button(frame1, text="Task Scheduler", padx=5, pady=5, command=open_task_scheduler).grid(row=7, column=0, sticky="ew")
Button(frame1, text="Open PowerShell", padx=5, pady=5, command=open_PowerShell).grid(row=7, column=1, sticky="ew")

# Tab 3 Buttons
Button(frame2, text="Get System UUID", padx=10, pady=10, command=get_uuid).pack()
Button(frame2, text="Get GPU Serials", padx=10, pady=10, command=show_gpu_serial_number).pack()

root.mainloop()