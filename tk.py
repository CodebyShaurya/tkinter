import tkinter as tk
from tkinter import messagebox
import random


def on_no_click():
    # Change the coordinates of the "No" button
    x=random.randrange(50,100)
    y=random.randrange(100, 200)
    #print(x,y)
    no_button.place(x=x,y=y)

def on_yes_click():
    # Display "I knew it" message
    messagebox.showinfo("Response", "I knew it")

# Create the main window
root = tk.Tk()
root.title("Are you dumb?")

# Create the question label
question_label = tk.Label(root, text="Are you dumb?")
question_label.pack()

# Create the "Yes" button
yes_button = tk.Button(root, text="Yes", command=on_yes_click)
yes_button.pack(side=tk.LEFT, padx=10)

# Create the "No" button
no_button = tk.Button(root, text="No", command=on_no_click)
no_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event
