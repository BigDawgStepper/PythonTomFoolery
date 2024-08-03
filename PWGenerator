import webbrowser
import time
import random
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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

new = 1
url = "https://github.com/BigDawgStepper"
url2 = "https://fakecrime.bio/eac"
url3 = "https://stackoverflow.com/users/25127168/thebigdawgstepper"
url4 = "https://www.youtube.com/channel/UC-oNk1pimzmEwkCtvSoJRgw"
url5 = "https://www.unknowncheats.me/forum/members/6145201.html"
url6 = "https://discord.gg/2cTFTugDrU"

root = tk.Tk()
root.title("Random Password Generator")
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
my_notebook.add(my_tab3, text="Credits")

# Tab 1 Labels
Label(my_tab1, text="Hello, welcome to the Password generator tab").pack()
Label(my_tab1, text="Just click the generate button and you will have a secure password").pack()
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
Label(my_tab3, text="This random password generator was made by Thebigdawgstepper").pack()
Label(my_tab3, text="Im also more known as eac so if u see my username is eac that is also me.").pack()
Label(my_tab3, text="You should check out some of these links here").pack()
Label(my_tab3, text="They have more info on me and my other projects").pack()

# Tab 1 Buttons
Button(my_tab1, text="Generate 12 Character PW with uppercase and special char", command=generator12).pack()
Button(my_tab1, text="Generate 8 Character PW with uppercase and special char", command=generator8).pack()
Button(my_tab1, text="Generate 12 Character PW with uppercase and no special char", command=generator12n).pack()
Button(my_tab1, text="Generate 8 Character PW with uppercase and no special char", command=generator8n).pack()

# Tab 2 Buttons
Button(my_tab2, text="Discord for dm", command=discord).pack()
Button(my_tab2, text="Github for source", command=Github).pack()

# Tab 3 Buttons
Button(my_tab3, text="My Github", command=Github).pack()
Button(my_tab3, text="My Bio Page", command=Biosite).pack()
Button(my_tab3, text="My Stack Overflow profile", command=stackoverflow).pack()
Button(my_tab3, text="My youtube profile", command=youtube).pack()
Button(my_tab3, text="My UnknownCheats profile", command=unknown).pack()
Button(my_tab3, text="My discord server", command=discord).pack()

root.mainloop()
