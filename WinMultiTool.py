import os

print("Welcome to BigDawgSteppers Windows Multi Tool")

def open_calculator():
    try:
        os.system("start calc")
        print("Calculator is open")
    except Exception as e:
        print("An error occured: {e}")


def open_task_manager():
    try: 
        os.system("start taskmgr")
        print("Task manager should be opened")
    except Exception as e:
        print(f"An error occured: {e}")

def multiple_choice():
    print("1. Open Task Manager")
    print("2. Open Calculator")
    print("3. Open System Info")
    print("4. Work in progress")
    print("5. Work in progress")
    choice = int(input("Choose a tool by typing the number of which you want: "))
    if choice == 1:
     print("Opening Task Manager.")
     open_task_manager()
     input("Press enter to quit...")
    elif choice == 2:
        print("Opening Calculator")
        open_calculator()
        input("Press enter to quit...")
  
if __name__ == "__main__":
    multiple_choice()
