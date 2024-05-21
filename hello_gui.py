import tkinter as tk

def say_hello():
    label.config(text="Hello World!")
# Create the main application window
    
app = tk.Tk()

# Set the window title

app.title("BigDawgStepper is onto GUI")

# Create a label widget

label = tk.Label(app, text="Click the button for j1million bonkas")

# Pack the label widget into the window

label.pack()

# Create a button widget

button = tk.Button(app, text="bonkas")

# Pack the button widget into the window

button.pack()

# Start the Tkinter event loop

app.mainloop()
