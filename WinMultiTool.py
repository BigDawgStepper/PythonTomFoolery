import os
import time

print("Welcome to BigDawgSteppers Windows Multi Tool")
time.sleep(2)
print("Loading...")
time.sleep(3)

def restart_computer():
    if os.name == 'nt':
        print("ANY UNSAVED DATA WILL BE LOST ON RESTART")
        print("15 seconds until restart")
        time.sleep(15)
        os.system('shutdown /r /t 1')
    else:
        print("Restart tool does not support your os.")

def open_file_explorer():
    try:
        time.sleep(2)
        os.system("start explorer")
        print("File Explorer is Running!")
    except Exception as e:
        print(f"An error occured: {e}")

def open_control_panel():
    try:
        time.sleep(2)
        os.system("start control")
        print("Control Panel Is Running!")
    except Exception as e:
        print(f"An error has occured: {e}")

def open_system_info():
    try:
        time.sleep(2)
        os.system("start msinfo32")
        print("System Information is Running!")
    except Exception as e:
        print(f"An error occured: {e}")

def open_calculator():
    try:
        time.sleep(2)
        os.system("start calc")
        print("Calculator is open!")
    except Exception as e:
        print("An error occured: {e}")

def open_task_manager():
    try: 
        time.sleep(2)
        os.system("start taskmgr")
        print("Task manager should be opened!")
    except Exception as e:
        print(f"An error occured: {e}")
        
def open_notepad():
    try:
        time.sleep(2)
        os.system("start notepad")
        print("Notepad is Running!")
    except Exception as e:
        print(f"An error occured: {e}")

def multiple_choice():
    print("1. Open Task Manager")
    print("2. Open Calculator")
    print("3. Open System Info")
    print("4. Open Control Panel")
    print("5. Open File Explorer")
    print("6. Restart Computer")
    print("7. Open Notepad")
    choice = int(input("Choose a tool by typing the number of which you want: "))
    if choice == 1:
     print("Opening Task Manager.")
     open_task_manager()
     input("Press enter to quit...")
    elif choice == 2:
        print("Opening Calculator")
        open_calculator()
        input("Press enter to quit...")
    elif choice == 3:
        print("Opening System Information")
        open_system_info()
        input("Press enter to quit...")
    elif choice == 4:
        print("Opening Control Panel")
        open_control_panel()
        input("Press enter to quit...")
    elif choice == 5:
        print("Opening File Explorer")
        open_file_explorer()
        input("Press enter to quit...")
    elif choice == 6:
        print("SAVE ANY UNSAVED DATA!!")
        restart_computer()
    elif choice == 7:
        print("Opening Notepad")
        open_notepad()
        input("Press enter to quit...")
 
if __name__ == "__main__":
    multiple_choice()
