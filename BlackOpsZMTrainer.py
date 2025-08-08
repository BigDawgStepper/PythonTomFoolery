import tkinter as tk
from tkinter import ttk, messagebox
import ctypes
import psutil
import struct
import threading
import time

# Windows constants
PROCESS_ALL_ACCESS = 0x1F0FFF

godThread = None
infiniteAmmoThread = None

def memoryHelper():
    procName = "BlackOps.exe"
    pid = None

    # Find process PID
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] == procName:
            pid = proc.info['pid']
            break

    if pid is None:
        messagebox.showerror("Error", "BlackOps.exe not found.")
        return

    # Open process
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if not handle:
        messagebox.showerror("Error", "Failed to open process. Run as admin.")
        return

    else:
        messagebox.showinfo("Success", "BlackOps.exe successfully opened.")
        return handle

def infiniteAmmo():
    handle = memoryHelper()
    secondaryAmmoAddress = 0x1C08F00
    primaryAmmoAddress = 0x1C08F10
    ammoAmnt = 999

    if handle is None:
        messagebox.showerror("Error", "Failed to open process. Run as admin.")
        return

    while infiniteAmmoToggled.get():
        data = struct.pack("<i", ammoAmnt)

        bytes_written = ctypes.c_size_t(0)
        ctypes.windll.kernel32.WriteProcessMemory(
            handle,
            secondaryAmmoAddress,
            data,
            len(data),
            ctypes.byref(bytes_written),
        )

        ctypes.windll.kernel32.WriteProcessMemory(
            handle,
            primaryAmmoAddress,
            data,
            len(data),
            ctypes.byref(bytes_written),
        )

        time.sleep(0.1)

    ctypes.windll.kernel32.CloseHandle(handle)
    messagebox.showinfo("Trainer", "Infinite Ammo toggled off")

def onInfiniteAmmoToggle():
    global infiniteAmmoThread
    if infiniteAmmoToggled.get():
        if infiniteAmmoThread is None or not infiniteAmmoThread.is_alive():
            infiniteAmmoThread = threading.Thread(target=infiniteAmmo, daemon=True)
            infiniteAmmoThread.start()
    else:
        pass

def godMode():
    handle = memoryHelper()
    healthAddress = 0x1A7987C
    healthAmnt = 2000

    if handle is None:
        messagebox.showerror("Error", "Failed to open process. Run as admin.")
        return

    ## This mimics cheat engines "Freeze" feature im using this for godmode method
    while godToggled.get():
        # Convert our value to bytes
        data = struct.pack("<i", healthAmnt)

        # Write memory
        bytes_written = ctypes.c_size_t(0)
        success = ctypes.windll.kernel32.WriteProcessMemory(
            handle,
            healthAddress,
            data,
            len(data),
            ctypes.byref(bytes_written)
        )
        time.sleep(0.1)

    ctypes.windll.kernel32.CloseHandle(handle)
    messagebox.showinfo("Trainer", "Godmode toggled off")

def onGodToggle():
    global godThread
    if godToggled.get():
        if godThread is None or not godThread.is_alive():
            godThread = threading.Thread(target=godMode, daemon=True)
            godThread.start()
    else:
        # Just let the loop exit naturally on next iteration
        pass

def addMoney():
    try:
        moneyAmnt = int(addMoneyInput.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    handle = memoryHelper()

    moneyAddress = 0x01C0A6C8
    # Convert our value to bytes
    data = struct.pack("<i", moneyAmnt)

    # Write memory
    bytes_written = ctypes.c_size_t(0)
    success = ctypes.windll.kernel32.WriteProcessMemory(
        handle,
        moneyAddress,
        data,
        len(data),
        ctypes.byref(bytes_written)
    )

    if success:
        messagebox.showinfo("Success", f"Wrote {moneyAmnt} to {hex(moneyAddress)}.")
    else:
        messagebox.showerror("Error", "Failed to write memory.")

    ctypes.windll.kernel32.CloseHandle(handle)

def unloadTrainer():
    return 0

# GUI
root = tk.Tk()
root.geometry("300x300")
root.title("ecxb's bozm trainer")
root.resizable(False, False)
root.iconbitmap("icon.ico")

## Notebook (For tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

## Aimbot frame
aimbotFrame = ttk.Frame(notebook)
notebook.add(aimbotFrame, text="Aimbot")

checkToggled = tk.IntVar()
aimbotCheckBox = ttk.Checkbutton(aimbotFrame, variable=checkToggled)
aimbotCheckBox.grid(column=1, row=0)

aimbotLabel = ttk.Label(aimbotFrame, text="Aimbot")
aimbotLabel.grid(column=0, row=0)

hitboxLabel = ttk.Label(aimbotFrame, text="Aimbot Hitbox")
hitboxLabel.grid(column=0, row=1)

selectedOption = tk.StringVar()
hitboxDropdown = ttk.Combobox(aimbotFrame, textvariable=selectedOption, width=10, height=5)
hitboxDropdown['values'] = ("Head", "Chest", "Legs")
hitboxDropdown.grid(column=1, row=1)
hitboxDropdown.current(0)

aimSmoothLabel = ttk.Label(aimbotFrame, text="Smoothing %")
aimSmoothLabel.grid(column=0, row=2)

aimSmoothValue = tk.IntVar()
aimSmoothingSlider = tk.Scale(aimbotFrame, from_=0, to=100, orient="horizontal")
aimSmoothingSlider.grid(column=1, row=2)

## Weapon frame
weaponFrame = ttk.Frame(notebook)
notebook.add(weaponFrame, text="Weapon")

infiniteAmmoLabel = ttk.Label(weaponFrame, text="Infinite Ammo")
infiniteAmmoLabel.grid(column=0, row=2)
infiniteAmmoToggled = tk.IntVar()
infiniteAmmoCheckBox = ttk.Checkbutton(weaponFrame, variable=infiniteAmmoToggled)
infiniteAmmoCheckBox.grid(column=1, row=2)
infiniteAmmoCheckBox.config(command=onInfiniteAmmoToggle)

## Misc Frame
miscFrame = ttk.Frame(notebook)
notebook.add(miscFrame, text="Misc")

addMoneyInput = ttk.Entry(miscFrame, width=10)
addMoneyInput.grid(row=0, column=1, padx=10, pady=10)
addMoneyBtn = ttk.Button(miscFrame, text="Add Money", command=addMoney)
addMoneyBtn.grid(row=0, column=0, padx=10, pady=10)

godModeLabel = ttk.Label(miscFrame, text="God Mode")
godModeLabel.grid(row=1, column=0)

godToggled = tk.IntVar()
godModeCheckBox = ttk.Checkbutton(miscFrame, variable=godToggled)
godModeCheckBox.config(command=onGodToggle)
godModeCheckBox.grid(column=1, row=1)

## Settings Frame
settingsFrame = ttk.Frame(notebook)
notebook.add(settingsFrame, text="Settings")

developerLabel = ttk.Label(settingsFrame, text="Developer = ecxb")
developerLabel.grid(row=0, column=0, padx=20, pady=10)

versionLabel = ttk.Label(settingsFrame, text="Version = 1.0")
versionLabel.grid(row=0, column=1)

unloadBtn = ttk.Button(settingsFrame, text="Unload trainer", command=unloadTrainer)
unloadBtn.grid(row=2, column=0)

root.mainloop()
