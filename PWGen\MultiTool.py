import webbrowser
import os
import subprocess
import wmi
import time
import random
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def generator16kk(length=16):
    if length < 16:
        raise ValueError("Password length should be at least 16 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(lowercase),
    ]

    all_characters = lowercase + digits
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator16k(length=16):
    if length < 16:
        raise ValueError("Password length should be at least 16 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator16(length=16):
    if length < 16:
        raise ValueError("Password length should be at least 16 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + uppercase + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator16n(length=16):
    if length < 16:
        raise ValueError("Password length should be at least 16 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(uppercase),
    ]

    all_characters = lowercase + digits + uppercase
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator12(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + uppercase + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator12k(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator12kk(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(lowercase),
    ]

    all_characters = lowercase + digits
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator8(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + uppercase + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator12n(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 8 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(uppercase),
    ]

    all_characters = lowercase + digits + uppercase
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator8n(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(uppercase),
    ]

    all_characters = lowercase + digits + uppercase
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator8k(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(special_chars),
    ]

    all_characters = lowercase + digits + special_chars
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def generator8kk(length=8):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    lowercase = string.ascii_lowercase
    digits = string.digits

    password = [
        random.choice(lowercase)
    ]

    all_characters = lowercase + digits
    password += random.choices(all_characters, k=length - 2)
    random.shuffle(password)
    tkinter.messagebox.showinfo(title="Your PW succesfully generated!", message=password)
    return ''.join(password)

def Github():
    time.sleep(0.5)
    webbrowser.open(url, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="GitHub Opened", message="Github page succesfully opened!")

def Biosite():
    time.sleep(0.5)
    webbrowser.open(url2, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Bio Site Opened", message="Bio site succesfully opened!")

def stackoverflow():
    time.sleep(0.5)
    webbrowser.open(url3, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="StackOverFlow Opened", message="Stackoverflow profile succesfully opened!")

def youtube():
    time.sleep(0.5)
    webbrowser.open(url4, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Youtube profile opened", message="My youtube profile has been opened!")

def unknown():
    time.sleep(0.5)
    webbrowser.open(url5, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Unknown Cheats profile opened", message="My UnknownCheats profile has been opened!")

def discord():
    time.sleep(0.5)
    webbrowser.open(url6, new=new)
    time.sleep(0.2)
    tkinter.messagebox.showinfo(title="Discord server joined!", message="My discord server has been opened!")

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

new = 1
url = "https://github.com/BigDawgStepper"
url2 = "https://fakecrime.bio/eac"
url3 = "https://stackoverflow.com/users/25127168/thebigdawgstepper"
url4 = "https://www.youtube.com/channel/UC-oNk1pimzmEwkCtvSoJRgw"
url5 = "https://www.unknowncheats.me/forum/members/6145201.html"
url6 = "https://discord.gg/2cTFTugDrU"

root = tk.Tk()
root.title("Multi Tool")
root.iconbitmap('C:\\Users\\eac\\Desktop\\Big hacker things\\icons\\lock.ico')
root.geometry("400x475")
root.resizable(False, False)

# Creating the notebook and making sure to connect it to the root
my_notebook = ttk.Notebook(root)
my_notebook.pack(expand=1, fill='both')

# Creating tab 1 and adding it to the main notebook
my_tab1 = ttk.Frame(my_notebook)
my_notebook.add(my_tab1, text="Password Generator")
my_tab2 = ttk.Frame(my_notebook)
my_notebook.add(my_tab2, text="How is it secure?")
my_tab3 = ttk.Frame(my_notebook)
my_notebook.add(my_tab3, text="Tools")
my_tab4 = ttk.Frame(my_notebook)
my_notebook.add(my_tab4 , text="HWID")
my_tab5 = ttk.Frame(my_notebook)
my_notebook.add(my_tab5, text="Credits")

# Tab 1 Labels
Label(my_tab1, text="Welcome to the Password generator tab", font=('Helvetica 14 bold')).pack()
Label(my_tab1, text="Choose the button that meets your specifications and click",).pack()
Label(my_tab1, text="------------------------------------------------------------------").pack()

# Tab 2 Labels
Label(my_tab2, text="So your wondering how exactly is this secure? This tab will explain it all!").pack()
Label(my_tab2, text="The passwords are completely random i use a couple things to ensure that.").pack()
Label(my_tab2, text="Every password that gets generated is different and random.").pack()
Label(my_tab2, text="And once a certian amount of PW get generated it all gets shuffled").pack()
Label(my_tab2, text="And that is how i ensure that the PW that get generated are random").pack()
Label(my_tab2, text="-----------------------------------------------------------------------").pack()
Label(my_tab2, text="If you have any questions or would like to see the source dm me").pack()

# Tab 3 Labels
Label(my_tab3, text="Click a button to open specified tool!", font=('Helvetica 16 bold')).pack()
# Tab 4 Labels
Label(my_tab4, text="Welcome to the HWID tab!", font=('Helvetica 16 bold')).pack()
Label(my_tab4, text="This tab is a HWID/Serial checker for windows 10/11").pack()
Label(my_tab4, text="If you are on linux there is a version for that on my github").pack()
Label(my_tab4, text="But the linux ver is very lightweight and has way less features than this ver").pack()

# Tab 5 Labels
Label(my_tab5, text="Owner/Dev is Thebigdawgstepper", font=('Helvetica 16 bold underline')).pack()
Label(my_tab5, text="Im also more known as eac so if u see my username is eac that is also me.").pack()
Label(my_tab5, text="You should check out some of these links here").pack()
Label(my_tab5, text="They have more info on me and my other projects").pack()

# Tab 1 Buttons
Button(my_tab1, text="Generate 16 Character PW with uppercase and special char", command=generator16).pack()
Button(my_tab1, text="Generate 16 Character PW with uppercase and NO special char", command=generator16n).pack()
Button(my_tab1, text="Generate 16 Character PW with lowercase and special char", command=generator16k).pack()
Button(my_tab1, text="Generate 16 Character PW with lowercase and NO special char", command=generator16kk).pack()
Button(my_tab1, text="Generate 12 Character PW with uppercase and special char", command=generator12).pack()
Button(my_tab1, text="Generate 12 Character PW with uppercase and NO special char", command=generator12n).pack()
Button(my_tab1, text="Generate 12 Character PW with lowercase and special char", command=generator12k).pack()
Button(my_tab1, text="Generate 12 Character PW with lowercase and NO special char", command=generator12kk).pack()
Button(my_tab1, text="Generate 8 Character PW with uppercase and special char", command=generator8).pack()
Button(my_tab1, text="Generate 8 Character PW with uppercase and NO special char", command=generator8n).pack()
Button(my_tab1, text="Generate 8 Character PW with lowercase and special char", command=generator8k).pack()
Button(my_tab1, text="Generate 8 Character PW with lowercase and NO special char", command=generator8kk).pack()

# Tab 2 Buttons
Button(my_tab2, text="Discord for dm", command=discord).pack()
Button(my_tab2, text="Github for source", command=Github).pack()

# Tab 3 Buttons
Button(my_tab3, text="Open Task Manager", command=taskmgr).pack()
Button(my_tab3, text="Open Control Panel", command=ctrlpanel).pack()
Button(my_tab3, text="Open Notepad", command=notepad).pack()
Button(my_tab3, text="Open File Explorer", command=open_explorer).pack()
Button(my_tab3, text="Open Settings", command=open_settings).pack()
Button(my_tab3, text="Open Display Settings", command=open_display_settings).pack()
Button(my_tab3, text="Open Virus Settings", command=open_virus_settings).pack()
Button(my_tab3, text="Open Registry Edit", command=open_reg_edit).pack()
Button(my_tab3, text="Open Calculator", command=open_calculator).pack()
Button(my_tab3, text="Open System Info", command=open_system_information).pack()
Button(my_tab3, text="Restart Computer", command=restart_computer).pack()
Button(my_tab3, text="Open CMD", command=open_cmd).pack()
Button(my_tab3, text="Open Task Scheduler", command=open_task_scheduler).pack()
Button(my_tab3, text="Open Powershell", command=open_PowerShell).pack()

# Tab 4 Buttons
Button(my_tab4, text="Get UUID", command=get_uuid).pack()
Button(my_tab4, text="Get GPU Serials", command=show_gpu_serial_number).pack()

# Tab 5 Buttons
Button(my_tab5, text="My Github", command=Github).pack()
Button(my_tab5, text="My Bio Page", command=Biosite).pack()
Button(my_tab5, text="My Stack Overflow profile", command=stackoverflow).pack()
Button(my_tab5, text="My youtube profile", command=youtube).pack()
Button(my_tab5, text="My UnknownCheats profile", command=unknown).pack()
Button(my_tab5, text="My discord server", command=discord).pack()

root.mainloop()
