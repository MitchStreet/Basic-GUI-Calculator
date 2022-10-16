# Programmed by Mitchell Street

# Import Python modules
import tkinter
from tkinter import *

# Initial variables
result = 0
global word_config
word_config = True

# GUI Window creation
# Window
calc = Tk()  # Name of window is "calc"
calc.title("Calculator")  # Title of window
calc.geometry("460x359")  # Size of window
calc.iconbitmap("icon.ico")  # Icon of window
calc.resizable(0, 0)  # Prevents window from being resized

# Output box
output_box = tkinter.Label(calc, text=(str(result)), font=("Arial", 20), bg="white", fg="black", width=20, height=2,
                           anchor="e")
output_box.grid(row=0, column=0, columnspan=4, sticky="nesw", pady=10)

# Calculate button
calculate_button = tkinter.Button(calc, text="Calculate", command="", font=("Arial bold", 15), bg="white", fg="black",
                                  width=2, height=2, anchor="center")
calculate_button.grid(row=4, column=3, columnspan=1, rowspan=2, sticky="nesw")

# Operator buttons
# Addition button
button_add = tkinter.Button(calc, text="+", font=("Arial bold", 12), bg="white", fg="black", height=2,
                            anchor="center")

# Subtraction button
button_sub = tkinter.Button(calc, text="-", font=("Arial bold", 12), bg="white", fg="black", height=2, width=10,
                            anchor="center")

# Multiplication button
button_mul = tkinter.Button(calc, text="x", font=("Arial bold", 12), bg="white", fg="black", height=2, width=10,
                            anchor="center")

# Division button
button_div = tkinter.Button(calc, text="÷", font=("Arial bold", 12), bg="white", fg="black", height=2, width=10,
                            anchor="center")


# Switch button - switches between word and symbol mode
def switch():
    global word_config
    if word_config is True:
        word_config = False
        button_add.config(text="Add")
        button_sub.config(text="Subtract")
        button_mul.config(text="Multiply")
        button_div.config(text="Divide")
    elif word_config is False:
        word_config = True
        button_add.config(text="+")
        button_sub.config(text="-")
        button_mul.config(text="x")
        button_div.config(text="÷")


switch_button = tkinter.Button(calc, text="Switch\n operators", command=switch, font=("Arial bold", 15), bg="white", fg="black",
                               width=10, height=2, anchor="center")
switch_button.grid(row=1, column=0, columnspan=1, sticky="nesw")

# Number keypad buttons
# Number 9
button_9 = tkinter.Button(calc, text="9", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_9.grid(row=2, column=2, columnspan=1, sticky="nesw")

# Number 8
button_8 = tkinter.Button(calc, text="8", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_8.grid(row=2, column=1, columnspan=1, sticky="nesw")

# Number 7
button_7 = tkinter.Button(calc, text="7", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_7.grid(row=2, column=0, columnspan=1, sticky="nesw")

# Number 6
button_6 = tkinter.Button(calc, text="6", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_6.grid(row=3, column=2, columnspan=1, sticky="nesw")

# Number 5
button_5 = tkinter.Button(calc, text="5", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_5.grid(row=3, column=1, columnspan=1, sticky="nesw")

# Number 4
button_4 = tkinter.Button(calc, text="4", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_4.grid(row=3, column=0, columnspan=1, sticky="nesw")

# Number 3
button_3 = tkinter.Button(calc, text="3", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_3.grid(row=4, column=2, columnspan=1, sticky="nesw")

# Number 2
button_2 = tkinter.Button(calc, text="2", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_2.grid(row=4, column=1, columnspan=1, sticky="nesw")

# Number 1
button_1 = tkinter.Button(calc, text="1", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_1.grid(row=4, column=0, columnspan=1, sticky="nesw")

# Number 0
button_0 = tkinter.Button(calc, text="0", font=("Arial", 12), bg="white", fg="black", height=2, anchor="center")
button_0.grid(row=5, column=0, columnspan=2, sticky="nesw")

# '.' button
button_dot = tkinter.Button(calc, text=".", font=("Arial bold", 12), bg="white", fg="black", height=2, anchor="center")
button_dot.grid(row=5, column=2, columnspan=1, sticky="nesw")


# Operation button positions
button_add.grid(row=2, column=3, columnspan=1, rowspan=2, sticky="nesw")
button_sub.grid(row=1, column=3, columnspan=1, sticky="nesw")
button_mul.grid(row=1, column=2, columnspan=1, sticky="nesw")
button_div.grid(row=1, column=1, columnspan=1, sticky="nesw")

# Display window
calc.mainloop()
