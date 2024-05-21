import tkinter as tk

def claim_bonkas():
    label.config(text="Claimed j1million bonkas!!!")
# Create the main application window
    
app = tk.Tk()

# Set the window title

app.title("BigDawgStepper is onto GUI")

# Create a label widget

label = tk.Label(app, text="Click the button for j1million bonkas!!!")

# Pack the label widget into the window

label.pack()

# Create a button widget

button = tk.Button(app, text="Claim Bonkas!!!!", command=claim_bonkas)

# Pack the button widget into the window

button.pack()

# Start the Tkinter event loop

app.mainloop()
