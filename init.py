import tkinter as tk
import functions as f
import inspect

colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

# Get a list of all functions in functions.py
function_list = [name for name in inspect.getmembers(f, inspect.isfunction)]

isOdd = (len(function_list) % 2) == 1
lenFunctions = len(function_list)
if isOdd:
    lenFunctions += 1
sizeX = lenFunctions * 35
# Create the main window
root = tk.Tk()

# Set the window to always be on top
root.attributes('-topmost', True)

root.geometry(f"300x{sizeX}+800+250")

def on_button_click(function):
    function()

def close_program(event=None):
    print("Ctrl+C pressed. Closing the program.")
    root.destroy()

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  # Add some padding around the frame

# Create a button for each function in function_list
for index, (function_name, function_obj) in enumerate(function_list):
    button = tk.Button(
        button_frame,
        text=function_name,  # Use the function name as the button label
        command=lambda func=function_obj: on_button_click(func),  # Pass the function to on_button_click
        background=colour2,
        foreground=colour4,
        activebackground=colour3,
        activeforeground=colour4,
        highlightthickness=2,
        highlightcolor='WHITE',
        width=15,
        height=2,
        border=0,
        cursor='hand1',
        font=("Courier", 10, "bold")
    )
    # Place the button in a grid (2 columns)
    row = index // 2  # Determine the row
    col = index % 2   # Determine the column (0 or 1)
    button.grid(row=row, column=col, padx=10, pady=10)

root.bind("<Control-c>", close_program)
root.overrideredirect(True)
root.mainloop()