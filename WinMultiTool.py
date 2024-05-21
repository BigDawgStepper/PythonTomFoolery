import os

print("Welcome to BigDawgSteppers Windows Multi Tool")

def open_task_manager():
    try: 
        os.system("start taskmgr")
        print("Task manager should be opened")
    except Exception as e:
        print(f"An error occured: {e}")


def multiple_choice():
    print("Make the choice of which tool ur tryna use")
    input("1.Open Task Manager:")
    
if __name__ == "__main__":
    multiple_choice()
    open_task_manager()