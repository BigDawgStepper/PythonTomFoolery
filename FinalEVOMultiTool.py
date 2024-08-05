from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import os
import wmi
import subprocess
import time
import random
import string
from winsound import *

def chargen16(length=16, include_uppercase=True, include_digits=True, include_special_chars=True):
    if length < 8:  # Minimum length for a reasonable password
        raise ValueError("Password length should be at least 8 characters")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets based on flags
    all_characters = lowercase + uppercase + digits + special_chars
    if not all_characters:
        raise ValueError("At least one character set must be included")

    # Generate password
    password = [
        random.choice(lowercase)  # Ensure at least one character from each set
    ]
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special_chars:
        password.append(random.choice(special_chars))

    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

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

def open_sys_info():
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
        tkinter.messagebox.showinfo(title="Multi Tool", message="Restart tool doesn’t support your OS")

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
    try:
        # Execute the command and decode the output
        output = subprocess.check_output('wmic csproduct get uuid', shell=True).decode('utf-8')
        # Split the output by lines
        lines = output.splitlines()
        
        # Ensure there are enough lines to avoid index errors
        if len(lines) > 1:
            uuid = lines[1].strip()
            return uuid if uuid else "UUID not found"
        else:
            return "UUID not found"
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"

def get_gpu_serial_number():
    try:
        c = wmi.WMI()
        serial_numbers = []
        
        for gpu in c.Win32_VideoController():
            if hasattr(gpu, 'SerialNumber') and gpu.SerialNumber:
                serial_numbers.append(gpu.SerialNumber)
        
        if serial_numbers:
            return "\n".join(serial_numbers)
        else:
            return "Serial number not found or no serial number available\n PS This only works if this program is run as admin"
    
    except wmi.x_wmi as e:
        return f"WMI Error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Lists
options = [
    "16 Char with lowercase, uppercase, digits and special chars",
    "16 Char with lowercase, uppercase and digits",
    "16 Char with lowercase, digits and special chars",
    "16 Char with uppercase, digits and special chars",
    "16 Char with uppercase, and special chars",
    "16 Char with uppercase, and digits",
    "12 Char with lowercase, uppercase, digits and special chars",
    "12 Char with lowercase, uppercase, and digits",
    "12 Char with lowercase, uppercase, and special chars",
    "12 Char with uppercase, digits and special chars",
    "12 Char with uppercase, and digits",
    "12 Char with uppercase, and special chars",
    "8 Char with lowercase, uppercase, digits and special chars",
    "8 Char with lowercase, uppercase, and digits",
    "8 Char with lowercase, digits and special chars",
    "8 Char with uppercase, digits and special chars",
    "8 Char with uppercase, and digits",
    "8 Char with uppercase, and special chars",
]

times = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
        '32',
        '33',
        '34',
        '35',
        '36',
        '37',
        '38',
        '39',
        '40',
        '41',
        '42',
        '43',
        '44',
        '45',
        '46',
        '47',
        '48',
        '49',
        '50',
        '51',
        '52',
        '53',
        '54',
        '55',
        '56',
        '57',
        '58',
        '59',
        '60',
    ]

def generate_password():
    # Get the selected option from the dropdown
    selected_option = selected.get()
    
    # Extract the length and character types from the selected option
    length = int(selected_option.split()[0])  # Extract length from the option text
    include_uppercase = 'uppercase' in selected_option
    include_digits = 'digits' in selected_option
    include_special_chars = 'special chars' in selected_option

    # Generate the password using chargen16 function
    password = chargen16(length, include_uppercase, include_digits, include_special_chars)

    # Update the text box with the generated password
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, password)
    text_box.insert(tk.END, " \n\nOLD PW GETS DELETED ON NEW GENERATION MAKE SURE TO SAVE!!!")

def show_uuid():
    uuid = get_uuid()
    text_box2.delete(1.0, tk.END)
    text_box2.insert(tk.END, uuid)

def show_gpu_serial_number():
    serial_number = get_gpu_serial_number()
    text_box2.delete(1.0, tk.END)
    text_box2.insert(tk.END, serial_number)

def dontclick():
    time.sleep(1)
    PlaySound('C:\\Users\\eac\\Downloads\\danger-alarm-sound-effect.wav', SND_FILENAME)
    tkinter.messagebox.showinfo(title="Told you not to", message="You had multiple chances to not click it and u still did smh")

# Setting all the default GUI settings
root = tk.Tk()
root.title("Eac's Multi Tool for Windows")
root.geometry("505x380")
root.resizable(False, False)
root.iconbitmap('C:\\Users\\eac\\Desktop\\Big hacker things\\icons\\multi-tool.ico')

# Variables
selected = StringVar()
selected.set(options[16])
play = lambda: PlaySound('C:\\Users\\eac\\Downloads\\danger-alarm-sound-effect.wav', SND_FILENAME)
IntervalMenu = IntVar()
IntervalMenu.set(times[0])
IntervalMenu1 = IntVar()
IntervalMenu1.set(times[0])
IntervalMenu2 = IntVar()
IntervalMenu2.set(times[0])
IntervalMenu3 = IntVar()
IntervalMenu3.set(times[0])

# Creating the notebook
my_notebook = ttk.Notebook(root)
my_notebook.pack(expand=1, fill='both')

# Creating the tabs
my_tab1 = ttk.Frame(my_notebook)
my_notebook.add(my_tab1, text="Tools/PW Gen")
my_tab2 = ttk.Frame(my_notebook)
my_notebook.add(my_tab2, text="HWID Checker")
my_tab4 = ttk.Frame(my_notebook)
my_notebook.add(my_tab4, text="Auto Clicker")
my_tab3 = ttk.Frame(my_notebook)
my_notebook.add(my_tab3, text="Credits")

# Creating the frames
frame1 = LabelFrame(my_tab1, text="Tools", width=250, height=250, padx=15, pady=15)
frame1.grid_propagate(False)
frame1.grid(row=0, column=0, sticky='nsw')

frame2 = LabelFrame(my_tab1, text="Password Gen", width=250, height=495, padx=15, pady=15)
frame2.grid_propagate(False)
frame2.grid(row=0, column=1, sticky='nsw')

frame3 = LabelFrame(my_tab2, text="HWID Checker", width=500, height=360, padx=15, pady=15)
frame3.grid_propagate(False)
frame3.grid(row=0, column=0, sticky='w')

frame4 = LabelFrame(my_tab4, text="Click Interval", width=500, height=100, padx=10)
frame4.grid_propagate(False)
frame4.grid(row=0, column=0, sticky='w')

frame5 = LabelFrame(my_tab3, text="Credits", width=500, height=360, padx=15, pady=15)
frame5.grid_propagate(False)
frame5.grid(row=0, column=0, sticky='w')

frame6 = LabelFrame(my_tab4, text="Click options", width=240, height=150,)
frame6.grid_propagate(False)
frame6.grid(row=1, column=0, sticky='w')

frame7 = LabelFrame(my_tab4, text="Click repeat", width=240, height=150,)
frame7.grid_propagate(False)
frame7.grid(row=1, column=0, padx=260, sticky='ew')

frame8 = LabelFrame(my_tab4, text="Settings", width=500, height=105)
frame8.grid_propagate(False)
frame8.grid(row=2, column=0, sticky='w')

# Creating the Labels
Label1 = ttk.Label(frame1, text="Just press a button!", font='Helvetica 14 bold')
Label1.grid_propagate(False)
Label1.grid(row=1, column=0, columnspan=3)

Label2 = ttk.Label(frame2, text="Select the type of password you want", font='Helvetica 9 bold')
Label2.grid(row=0, column=0, columnspan=3, sticky='w')

Label3 = ttk.Label(frame2, text="then watch the magic happen!", font='Helvetica 9 bold')
Label3.grid(row=1, column=0, columnspan=3, sticky='w')

Label4 = ttk.Label(frame2, text="------------------------------------------------------", font='Helvetica 9 bold')
Label4.grid(row=2, column=0, columnspan=3, sticky='w')

Label5 = ttk.Label(frame3, text="Choose one of the button options and the result should print in the box!", font='Helvetica 10 bold')
Label5.grid(row=0, column=0)

Label6 = ttk.Label(frame5, text="This program was made by eac/thebigdawgstepper yes its only 1 person")
Label6.grid(row=0, column=0, sticky='w')

Label7 = ttk.Label(frame5, text="Its a pretty small program but i hope its useful, enjoy the tool!")
Label7.grid(row=1, column=0, sticky='w')

Label8 = ttk.Label(frame5, text="Please dont click the button once you do your in it for 10 seconds")
Label8.grid(row=2, column=0, sticky='w')

Label9 = ttk.Label(frame4, text="Hours", font='Helvetica 12 bold')
Label9.grid(row=0, column=0, padx=60, sticky='w')

Label10 = ttk.Label(frame4, text="Minutes", font='Helvetica 12 bold')
Label10.grid(row=1, column=0, padx=60, sticky='w')

Label11 = ttk.Label(frame4, text="Seconds", font='Helvetica 12 bold')
Label11.grid(row=0, column=1, padx=60)

Label12 = ttk.Label(frame4, text="Millisecs", font='Helvetica 12 bold')
Label12.grid(row=1, column=1, padx=60)

# Creating the Buttons
Button1 = Button(frame1, text="Task Mgr", padx=5, pady=5, width=8, height=1, command=taskmgr)
Button1.grid(row=2, column=0, sticky='ew')

Button2 = Button(frame1, text="Ctrl Panel", padx=5, pady=5, width=8, height=1, command=ctrlpanel)
Button2.grid(row=2, column=1, sticky='ew')

Button3 = Button(frame1, text="Notepad", padx=5, pady=5, width=8, height=1, command=notepad)
Button3.grid(row=2, column=2, sticky='ew')

Button4 = Button(frame1, text="Explorer", padx=5, pady=5, width=8, height=1, command=open_explorer)
Button4.grid(row=3, column=0, sticky='ew')

Button5 = Button(frame1, text="Settings", padx=5, pady=5, width=8, height=1, command=open_settings)
Button5.grid(row=3, column=1, sticky='ew')

Button6 = Button(frame1, text="WinDefender", padx=5, pady=5, width=8, height=1, command=open_virus_settings)
Button6.grid(row=3, column=2, sticky='ew')

Button7 = Button(frame1, text="Reg Edit", padx=5, pady=5, width=8, height=1, command=open_reg_edit)
Button7.grid(row=4, column=0, sticky='ew')

Button8 = Button(frame1, text="Calculator", padx=5, pady=5, width=8, height=1, command=open_calculator)
Button8.grid(row=4, column=1, sticky='ew')

Button9 = Button(frame1, text="Sys Info", padx=5, pady=5, width=8, height=1, command=open_sys_info)
Button9.grid(row=4, column=2, sticky='ew')

Button10 = Button(frame1, text="Restart PC", padx=5, pady=5, width=8, height=1, command=restart_computer)
Button10.grid(row=5, column=0, sticky='ew')

Button11 = Button(frame1, text="Open CMD", padx=5, pady=5, width=8, height=1, command=open_cmd)
Button11.grid(row=5, column=1, sticky='ew')

Button12 = Button(frame1, text="Task Scheduler", padx=5, pady=5, width=8, height=1, command=open_task_scheduler)
Button12.grid(row=5, column=2, sticky='ew')

Button13 = Button(frame1, text="Powershell", padx=5, pady=5, width=8, height=1, command=open_PowerShell)
Button13.grid(row=6, column=0, sticky='ew')

Button14 = Button(frame1, text="WIP", padx=5, pady=5, width=8, height=1)
Button14.grid(row=6, column=1, sticky='ew')

Button15 = Button(frame1, text="WIP", padx=5, pady=5, width=8, height=1)
Button15.grid(row=6, column=2, sticky='ew')

Button16 = Button(frame3, text="Get UUID", width=8, height=1, command=show_uuid)
Button16.grid(row=1, column=0, columnspan=1, padx=5, pady=3, sticky='w')

Button17 = Button(frame3, text="Get HWID", width=8, height=1, command=show_gpu_serial_number)
Button17.grid(row=2, column=0, columnspan=1, padx=5, pady=3, sticky='w')

Button18 = Button(frame5, text="DONT CLICK ME!!!", command=dontclick)
Button18.grid(row=3, column=3, sticky='w')

generate_pw_button = Button(frame2, text="Generate PW", padx=5, pady=5, width=8, height=1, command=generate_password)
generate_pw_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

# Creating Text Boxes
text_box = tk.Text(frame2, height=10, width=27)
text_box.grid(row=4, column=0, columnspan=3, pady=10, sticky='nesw')

text_box2 = tk.Text(frame3, height=12, width=60)
text_box2.grid(row=4, column=0, pady=15)

# Creating Drop Down Box
drop = OptionMenu(frame2, selected, *options)
drop.grid(columnspan=3, sticky='nesw')

drop1 = OptionMenu(frame4, IntervalMenu, *times)
drop1.grid(row=0, column=0, sticky='w')

drop2 = OptionMenu(frame4, IntervalMenu1, *times)
drop2.grid(row=1, column=0, sticky='w')

drop3 = OptionMenu(frame4, IntervalMenu2, *times)
drop3.grid(row=0, column=1, sticky='w')

drop4 = OptionMenu(frame4, IntervalMenu3, *times)
drop4.grid(row=1, column=1, sticky='w')

frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)
frame1.grid_columnconfigure(3, weight=1)
frame3.grid_columnconfigure(0, weight=1)
frame3.grid_columnconfigure(1, weight=1)
frame3.grid_columnconfigure(2, weight=1)
frame3.grid_columnconfigure(3, weight=1)
frame4.grid_rowconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)
frame4.grid_columnconfigure(1, weight=1)
frame4.grid_columnconfigure(2, weight=1)
frame4.grid_columnconfigure(3, weight=1)

root.mainloop()
