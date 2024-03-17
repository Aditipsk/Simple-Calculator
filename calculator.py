import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Function to perform arithmetic operation
def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!", parent=root)
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!", parent=root)
            return

        result_label.config(text=f"Result: {result}", fg="#FFC107")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers.", parent=root)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.configure(bg="#212121")

# Create custom font
custom_font = font.Font(family="Helvetica", size=16)

# Create input fields for numbers
num1_label = tk.Label(root, text="Number 1:", font=custom_font, fg="#FFFFFF", bg="#212121")
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1_entry = tk.Entry(root, font=custom_font, bg="#424242", fg="#FFFFFF")
num1_entry.grid(row=0, column=1, padx=10, pady=10)

num2_label = tk.Label(root, text="Number 2:", font=custom_font, fg="#FFFFFF", bg="#212121")
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2_entry = tk.Entry(root, font=custom_font, bg="#424242", fg="#FFFFFF")
num2_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a dropdown menu for operation choice
operation_label = tk.Label(root, text="Operation:", font=custom_font, fg="#FFFFFF", bg="#212121")
operation_label.grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar()
operation_dropdown = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_dropdown.config(font=custom_font, bg="#424242", fg="#FFFFFF", activebackground="#616161", activeforeground="#FFFFFF")
operation_dropdown.grid(row=2, column=1, padx=10, pady=10)

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=custom_font, bg="#FFC107", fg="#212121", activebackground="#FFD54F", activeforeground="#212121")
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=custom_font, bg="#212121", fg="#FFFFFF")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()