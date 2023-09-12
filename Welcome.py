import tkinter as tk

# Create the window
window = tk.Tk()

# Set the title of the window
window.title("Welcome")

# Create a label to display the welcome message
label = tk.Label(text="Welcome to my program!")

# Pack the label into the window
label.pack()

# Create a button to close the window
button = tk.Button(text="Close", command=window.quit)

# Pack the button into the window
button.pack()

# Start the mainloop of the window
window.mainloop()
