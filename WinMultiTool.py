import os

print("Welcome to BigDawgSteppers Windows Multi Tool")

def open_task_manager():
    try: 
        os.system("start taskmgr")
        print("Task manager should be opened")
    except Exception as e:
        print(f"An error occured: {e}")

def multiple_choice():
    print("1. Open Task Manager")
    print("2. Open cmd")
    print("3. Open System Info")
    print("4. Work in progress")
    print("5. Work in progress")
    choice = int(input("Choose a tool by typing the number of which you want: "))
    if choice == 1:
     print("Opening Task Manager.")
     open_task_manager()
    
if __name__ == "__main__":
    multiple_choice()
