import tkinter as tk
from tkinter import ttk
from PIL import Image

# Define the path for the blank icon
icon_path = 'C:\\Users\\Frank\\Desktop\\blank.ico'

# Create a blank (transparent) ICO file if it doesn't exist
def create_blank_ico(path):
    size = (16, 16)  # Size of the icon
    image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent image
    image.save(path, format="ICO")

# Create the blank ICO file
create_blank_ico(icon_path)

# Global variable to store decimal places (default to 2)
decimal_places = 2

# List to store references to decimal buttons
decimal_buttons = []

# Function to toggle between 2 and 5 decimal places
def toggle_decimal_places():
    global decimal_places
    decimal_places = 5 if decimal_places == 2 else 2
    # Update all decimal buttons with the current number of decimal places
    for button in decimal_buttons:
        button.config(text=f"Decimals: {decimal_places}")

# Function to calculate VAT (Add/Remove)
def calculate_vat(add_vat=True):
    try:
        initial_amount = float(vat_initial_amount_entry.get())
        vat_percentage = float(vat_percentage_entry.get())
        
        if add_vat:
            vat_value = (initial_amount * vat_percentage) / 100
            total_amount = initial_amount + vat_value
        else:
            total_amount = initial_amount / (1 + (vat_percentage / 100))
            vat_value = initial_amount - total_amount
        
        net_amount_label.config(text=f"Net Amount: {total_amount:.{decimal_places}f}")
        vat_result_label.config(text=f"VAT: {vat_value:.{decimal_places}f}")
        total_amount_label.config(text=f"Total: {initial_amount:.{decimal_places}f}")
    except ValueError:
        vat_result_label.config(text="Please enter valid numbers.")

# Percentage Change Calculator (Calculator 1)
def calculate_percentage(event=None):
    try:
        old_value = float(old_entry.get())
        new_value = float(new_entry.get())
        difference = new_value - old_value
        percentage = (difference / old_value) * 100
        result_label.config(text=f"Percentage Change: {percentage:.{decimal_places}f}%")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Increase/Decrease Calculator (Calculator 2)
def calculate_new_value(event=None):
    try:
        old_value = float(old_value_entry.get())
        percent_value = float(percent_value_entry.get())
        operation = operation_var.get()

        if operation == "Increase":
            new_value = old_value * (1 + percent_value / 100)
        elif operation == "Decrease":
            new_value = old_value * (1 - percent_value / 100)
        
        new_value_entry.delete(0, tk.END)
        new_value_entry.insert(0, f"{new_value:.{decimal_places}f}")
        result_label2.config(text=f"New Value: {new_value:.{decimal_places}f}")
    except ValueError:
        result_label2.config(text="Please enter valid numeric values.")

# Basic Calculator (Calculator 3)
def basic_calculate(event=None):
    try:
        expression = entry_expression.get()  
        result = eval(expression)  
        result_label_basic.config(text=f"Result: {result:.{decimal_places}f}")
    except (ValueError, SyntaxError, ZeroDivisionError):
        result_label_basic.config(text="Enter a valid expression")

# The main application starts here
root = tk.Tk()
root.title("Calculator")

# Set custom icon
root.iconbitmap(icon_path)

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_vat = ttk.Frame(tab_control)  

tab_control.add(tab1, text='Calculator 1')  
tab_control.add(tab2, text='Calculator 2')  
tab_control.add(tab3, text='Basic Calculator')
tab_control.add(tab_vat, text='VAT Calculator')  

tab_control.pack(expand=1, fill='both')

# VAT Calculator Tab
vat_frame = tk.Frame(tab_vat)
vat_frame.pack(padx=10, pady=10)

tk.Label(vat_frame, text="Initial Amount:").grid(row=0, column=0, padx=5, pady=5)
vat_initial_amount_entry = tk.Entry(vat_frame)
vat_initial_amount_entry.grid(row=0, column=1, padx=5, pady=5)
vat_initial_amount_entry.focus()

tk.Label(vat_frame, text="VAT %:").grid(row=1, column=0, padx=5, pady=5)
vat_percentage_entry = tk.Entry(vat_frame)
vat_percentage_entry.grid(row=1, column=1, padx=5, pady=5)

add_vat_button = tk.Button(vat_frame, text="Add VAT", command=lambda: calculate_vat(add_vat=True), bg="#d0e8f1", font=("Helvetica", 8))
add_vat_button.grid(row=2, column=0, padx=5, pady=5)

subtract_vat_button = tk.Button(vat_frame, text="Subtract VAT", command=lambda: calculate_vat(add_vat=False), bg="#d0e8f1", font=("Helvetica", 8))
subtract_vat_button.grid(row=2, column=1, padx=5, pady=5)

net_amount_label = tk.Label(vat_frame, text="Net Amount: ")
net_amount_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

vat_result_label = tk.Label(vat_frame, text="VAT: ")
vat_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

total_amount_label = tk.Label(vat_frame, text="Total: ")
total_amount_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Add Decimals button for VAT
decimal_button = tk.Button(vat_frame, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button)

# Calculator 1 Tab (Percentage Change)
frame1 = tk.Frame(tab1)
frame1.pack(padx=10, pady=10)

tk.Label(frame1, text="Old Value:").grid(row=0, column=0, padx=5, pady=5)
old_entry = tk.Entry(frame1)
old_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame1, text="New Value:").grid(row=1, column=0, padx=5, pady=5)
new_entry = tk.Entry(frame1)
new_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame1, text="Calculate", command=calculate_percentage, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(frame1, text="Percentage Change: ")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Add Decimals button for Calculator 1
decimal_button1 = tk.Button(frame1, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button1.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button1)

# Calculator 2 Tab (Increase/Decrease)
frame2 = tk.Frame(tab2)
frame2.pack(padx=10, pady=10)

tk.Label(frame2, text="Old Value:").grid(row=0, column=0, padx=5, pady=5)
old_value_entry = tk.Entry(frame2)
old_value_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame2, text="Percent Value:").grid(row=1, column=0, padx=5, pady=5)
percent_value_entry = tk.Entry(frame2)
percent_value_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame2, text="Operation:").grid(row=2, column=0, padx=5, pady=5)
operation_var = tk.StringVar(frame2)
operation_combobox = ttk.Combobox(frame2, textvariable=operation_var, values=["Increase", "Decrease"], width=10)
operation_combobox.grid(row=2, column=1, padx=5, pady=5)
operation_combobox.current(0)

calculate_button2 = tk.Button(frame2, text="Calculate", command=calculate_new_value, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

tk.Label(frame2, text="New Value:").grid(row=4, column=0, padx=5, pady=5)
new_value_entry = tk.Entry(frame2)
new_value_entry.grid(row=4, column=1, padx=5, pady=5)

result_label2 = tk.Label(frame2, text="New Value: ")
result_label2.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Add Decimals button for Calculator 2
decimal_button2 = tk.Button(frame2, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button2.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button2)

# Basic Calculator Tab (Calculator 3)
frame3 = tk.Frame(tab3)
frame3.pack(padx=10, pady=10)

tk.Label(frame3, text="Expression:").grid(row=0, column=0, padx=5, pady=5)
entry_expression = tk.Entry(frame3)
entry_expression.grid(row=0, column=1, padx=5, pady=5)

calculate_button_basic = tk.Button(frame3, text="Calculate", command=basic_calculate, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button_basic.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

result_label_basic = tk.Label(frame3, text="Result: ")
result_label_basic.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Add Decimals button for Basic Calculator
decimal_button3 = tk.Button(frame3, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button3.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button3)

# Bind Enter key for all tabs and fields
old_entry.bind('<Return>', lambda event: new_entry.focus())
new_entry.bind('<Return>', lambda event: calculate_button.focus())
old_value_entry.bind('<Return>', lambda event: percent_value_entry.focus())
percent_value_entry.bind('<Return>', lambda event: operation_combobox.focus())
operation_combobox.bind('<Return>', lambda event: calculate_button2.focus())
entry_expression.bind('<Return>', lambda event: calculate_button_basic.focus())
vat_initial_amount_entry.bind('<Return>', lambda event: vat_percentage_entry.focus())
vat_percentage_entry.bind('<Return>', lambda event: add_vat_button.focus())

# Bind Enter key to trigger 'Calculate' buttons for all tabs
calculate_button.bind('<Return>', calculate_percentage)
calculate_button2.bind('<Return>', calculate_new_value)
calculate_button_basic.bind('<Return>', basic_calculate)

# Bind Enter key for VAT buttons
add_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=True))
subtract_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=False))

# Main loop
root.mainloop()
