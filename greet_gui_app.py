import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = entry.get()
    if name.strip():
        messagebox.showinfo("Greeting", f"Hello, {name}! Welcome 🎉")
    else:
        messagebox.showwarning("Input Error", "Please enter your name!")

# Create main window
root = tk.Tk()
root.title("Greeter App")
root.geometry("300x150")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Greet Me", command=greet_user)
button.pack(pady=10)

# Run the app
root.mainloop()