import subprocess

def get_gpu_hwid():
    try:
        lspci_output = subprocess.check_output(["lspci"]).decode("utf-8")
        gpu_lines = [line.strip() for line in lspci_output.split('\n') if "VGA compatible controller" in line]

        if not gpu_lines:
            print("No GPU found.")
            return None

        hwid = gpu_lines[0].split()[0]
        return hwid
    except Exception as e:
        print("Error:", e)
        return None    

def TaskViewer():
    try:
        print("If your wondering how to leave just close task viewer")
        subprocess.run(["gnome-system-monitor"])
    except Exception as e:
        print("Error:", e)

def Calculator():
    try:
        print("Want to leave? Just type quit.")
        subprocess.run(["qalc"])
    except Exception as e:
        print("Error:", e)    

def choose_tool(choices):
    print("WELCOME TO BIGDAWGSTEPPERS LINUX MULTI TOOL!")
    print("All features last working on Ubuntu 24, anything other than linux wont work!!!")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        user_input = input("Choose Tool: (1, 2 or 3): ")
        if user_input in ["1", "2", "3"]:
            return int(user_input)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    choices = ["Get GPU HWID", "Open Task Viewer(GNOME UBUNTU ONLY!!)", "Advacned calculator (Must install qalc if not already present)"]
    user_choice = choose_tool(choices)
    print("Picked:", choices[user_choice - 1])
    if user_choice == 1:
        get_gpu_hwid()
        gpu_hwid = get_gpu_hwid()
        if gpu_hwid:
            print("GPU HWID:", gpu_hwid)
    elif user_choice == 2:
        TaskViewer()
    elif user_choice == 3:
        Calculator()

if __name__ == "__main__":
    main()