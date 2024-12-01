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
        
        net_amount_label.config(text=f"Net Amount: {total_amount:,.{decimal_places}f}")
        vat_result_label.config(text=f"VAT: {vat_value:,.{decimal_places}f}")
        total_amount_label.config(text=f"Total: {initial_amount:,.{decimal_places}f}")
    except ValueError:
        vat_result_label.config(text="Please enter valid numbers.")

# Function to clear VAT Calculator fields and focus
def clear_vat_calculator():
    vat_initial_amount_entry.delete(0, tk.END)
    vat_percentage_entry.delete(0, tk.END)
    net_amount_label.config(text="Net Amount: ")
    vat_result_label.config(text="VAT: ")
    total_amount_label.config(text="Total: ")
    vat_initial_amount_entry.focus_set()

# Function to clear VAT Calculator and shift focus
def clear_vat_calculator_and_focus(event=None):
    clear_vat_calculator()
    vat_initial_amount_entry.focus_set()

# Percentage Change Calculator (Calculator 1)
def calculate_percentage(event=None):
    try:
        old_value = float(old_entry.get())
        new_value = float(new_entry.get())
        difference = new_value - old_value
        percentage = (difference / old_value) * 100
        result_label.config(text=f"Percentage Change: {percentage:,.{decimal_places}f}%")

        # Desktop steps
        desktop_steps = (
            f"Step 1: Subtract old value from new value: {new_value:,.{decimal_places}f} - {old_value:,.{decimal_places}f} = {difference:,.{decimal_places}f}\n"
            f"Step 2: Divide the difference by the old value: {difference:,.{decimal_places}f} / {old_value:,.{decimal_places}f} = {difference / old_value:,.{decimal_places}f}\n"
            f"Step 3: Multiply by 100 to get the percentage: ({difference / old_value:,.{decimal_places}f}) * 100 = {percentage:,.{decimal_places}f}%"
        )
        desktop_steps_label.config(text=desktop_steps)
        
        # Excel steps
        excel_steps = (
            f"=((New Value - Old Value) / Old Value) * 100\n"
            f"Example: =(({new_value:,.{decimal_places}f} - {old_value:,.{decimal_places}f}) / {old_value:,.{decimal_places}f}) * 100"
        )
        excel_steps_label.config(text=excel_steps)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Function to clear Calculator 1 fields and focus
def clear_calculator1():
    old_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    result_label.config(text="Percentage Change: ")
    desktop_steps_label.config(text="")
    excel_steps_label.config(text="")
    old_entry.focus_set()

# Function to calculate and focus
def calculate_percentage_and_focus(event=None):
    calculate_percentage()
    clear_button1.focus_set()

# Function to clear and focus
def clear_calculator1_and_focus(event=None):
    clear_calculator1()
    old_entry.focus_set()

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
        new_value_entry.insert(0, f"{new_value:,.{decimal_places}f}")
        result_label2.config(text=f"New Value: {new_value:,.{decimal_places}f}")

        # Desktop steps for Increase/Decrease
        desktop_steps2 = (
            f"Step 1: Operation chosen: {operation}\n"
            f"Step 2: Calculation: {old_value:,.{decimal_places}f} * (1 {'+' if operation == 'Increase' else '-'} {percent_value:,.{decimal_places}f}%) = {new_value:,.{decimal_places}f}"
        )
        desktop_steps_label2.config(text=desktop_steps2)
        
        # Excel steps for Increase/Decrease
        excel_steps2 = (
            f"=Old Value * (1 + (Percent Value / 100)) (for Increase)\n"
            f"=Old Value * (1 - (Percent Value / 100)) (for Decrease)\n"
            f"Example for Increase: = {old_value:,.{decimal_places}f} * (1 + {percent_value / 100:,.{decimal_places}f})\n"
            f"Example for Decrease: = {old_value:,.{decimal_places}f} * (1 - {percent_value / 100:,.{decimal_places}f})"
        )
        excel_steps_label2.config(text=excel_steps2)
    except ValueError:
        result_label2.config(text="Please enter valid numeric values.")

# Function to clear Calculator 2 fields and focus
def clear_calculator2():
    old_value_entry.delete(0, tk.END)
    percent_value_entry.delete(0, tk.END)
    operation_combobox.current(0)  # Reset to default operation
    new_value_entry.delete(0, tk.END)
    result_label2.config(text="New Value: ")
    desktop_steps_label2.config(text="")
    excel_steps_label2.config(text="")
    old_value_entry.focus_set()

# Function to calculate and focus
def calculate_new_value_and_focus(event=None):
    calculate_new_value()
    clear_button2.focus_set()

# Function to clear and focus
def clear_calculator2_and_focus(event=None):
    clear_calculator2()
    old_value_entry.focus_set()

# Basic Calculator (Calculator 3)
def basic_calculate(event=None):
    try:
        expression = entry_expression.get()  
        result = eval(expression)  
        formatted_result = f"{result:,.{decimal_places}f}"
        result_label_basic.config(text=f"Result: {formatted_result}")

        # Show basic calculation steps with thousand separators
        basic_steps = f"Calculation performed: {expression} = {formatted_result}"
        basic_steps_label.config(text=basic_steps)
    except (ValueError, SyntaxError, ZeroDivisionError):
        result_label_basic.config(text="Enter a valid expression")

# Function to clear Basic Calculator fields and move focus
def clear_basic_calculator():
    entry_expression.delete(0, tk.END)
    result_label_basic.config(text="Result: ")
    basic_steps_label.config(text="")
    entry_expression.focus_set()

# Function to calculate and focus
def basic_calculate_and_focus(event=None):
    basic_calculate()
    clear_button_basic.focus_set()

# Function to clear and focus
def clear_basic_calculator_and_focus(event=None):
    clear_basic_calculator()
    entry_expression.focus_set()

# Toggle visibility of Desktop and Excel steps
def toggle_calculations():
    widgets = [
        desktop_heading, desktop_steps_label, excel_heading, excel_steps_label,
        desktop_heading2, desktop_steps_label2, excel_heading2, excel_steps_label2,
        basic_heading, basic_steps_label  # Including basic calculation steps toggle
    ]
    for widget in widgets:
        if widget.winfo_viewable():
            widget.grid_remove()
        else:
            widget.grid()

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

# Frame to hold Add, Subtract, and Clear VAT buttons side by side
button_frame_vat = tk.Frame(vat_frame)
button_frame_vat.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

add_vat_button = tk.Button(button_frame_vat, text="Add VAT", command=lambda: calculate_vat(add_vat=True), bg="#d0e8f1", font=("Helvetica", 8))
add_vat_button.pack(side=tk.LEFT, padx=(0, 5))

subtract_vat_button = tk.Button(button_frame_vat, text="Subtract VAT", command=lambda: calculate_vat(add_vat=False), bg="#d0e8f1", font=("Helvetica", 8))
subtract_vat_button.pack(side=tk.LEFT, padx=(5, 5))

clear_vat_button = tk.Button(button_frame_vat, text="Clear", command=clear_vat_calculator_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_vat_button.pack(side=tk.LEFT, padx=(5, 0))

net_amount_label = tk.Label(vat_frame, text="Net Amount: ")
net_amount_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

vat_result_label = tk.Label(vat_frame, text="VAT: ")
vat_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

total_amount_label = tk.Label(vat_frame, text="Total: ")
total_amount_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Add Decimals button for VAT
decimal_button_vat = tk.Button(vat_frame, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button_vat.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button_vat)

# Calculator 1 Tab (Percentage Change)
frame1 = tk.Frame(tab1)
frame1.pack(padx=10, pady=10)

tk.Label(frame1, text="Old Value:").grid(row=0, column=0, padx=5, pady=5)
old_entry = tk.Entry(frame1)
old_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame1, text="New Value:").grid(row=1, column=0, padx=5, pady=5)
new_entry = tk.Entry(frame1)
new_entry.grid(row=1, column=1, padx=5, pady=5)

# Frame to hold Calculate and Clear buttons side by side
button_frame1 = tk.Frame(frame1)
button_frame1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

calculate_button1 = tk.Button(button_frame1, text="Calculate", command=calculate_percentage_and_focus, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button1.pack(side=tk.LEFT, padx=(0, 5))

clear_button1 = tk.Button(button_frame1, text="Clear", command=clear_calculator1_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_button1.pack(side=tk.LEFT, padx=(5, 0))

result_label = tk.Label(frame1, text="Percentage Change: ")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

desktop_heading = tk.Label(frame1, text="Desktop Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
desktop_heading.grid(row=4, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
desktop_heading.grid_remove()

desktop_steps_label = tk.Label(frame1, text="", font=("Helvetica", 8), fg="grey", anchor="center")
desktop_steps_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label.grid_remove()

excel_heading = tk.Label(frame1, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading.grid(row=6, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading.grid_remove()

excel_steps_label = tk.Label(frame1, text="", font=("Helvetica", 8), fg="grey", anchor="center")
excel_steps_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label.grid_remove()

toggle_button = tk.Button(frame1, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Add Decimals button for Calculator 1
decimal_button1 = tk.Button(frame1, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button1.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
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
operation_combobox = ttk.Combobox(frame2, textvariable=operation_var, values=["Increase", "Decrease"], width=10, state='readonly')
operation_combobox.grid(row=2, column=1, padx=5, pady=5)
operation_combobox.current(0)

# Frame to hold Calculate and Clear buttons side by side
button_frame2 = tk.Frame(frame2)
button_frame2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

calculate_button2 = tk.Button(button_frame2, text="Calculate", command=calculate_new_value_and_focus, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button2.pack(side=tk.LEFT, padx=(0, 5))

clear_button2 = tk.Button(button_frame2, text="Clear", command=clear_calculator2_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_button2.pack(side=tk.LEFT, padx=(5, 0))

tk.Label(frame2, text="New Value:").grid(row=4, column=0, padx=5, pady=5)
new_value_entry = tk.Entry(frame2)
new_value_entry.grid(row=4, column=1, padx=5, pady=5)

result_label2 = tk.Label(frame2, text="New Value: ")
result_label2.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

desktop_heading2 = tk.Label(frame2, text="Desktop Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
desktop_heading2.grid(row=6, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
desktop_heading2.grid_remove()

desktop_steps_label2 = tk.Label(frame2, text="", font=("Helvetica", 8), fg="grey", anchor="center")
desktop_steps_label2.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label2.grid_remove()

excel_heading2 = tk.Label(frame2, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading2.grid(row=8, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading2.grid_remove()

excel_steps_label2 = tk.Label(frame2, text="", font=("Helvetica", 8), fg="grey", anchor="center")
excel_steps_label2.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label2.grid_remove()

toggle_button2 = tk.Button(frame2, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button2.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Add Decimals button for Calculator 2
decimal_button2 = tk.Button(frame2, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button2.grid(row=11, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button2)

# Basic Calculator Tab (Calculator 3)
frame3 = tk.Frame(tab3)
frame3.pack(padx=10, pady=10)

tk.Label(frame3, text="Expression:").grid(row=0, column=0, padx=5, pady=5)
entry_expression = tk.Entry(frame3)
entry_expression.grid(row=0, column=1, padx=5, pady=5)

# Frame to hold Calculate and Clear buttons side by side
button_frame3 = tk.Frame(frame3)
button_frame3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

calculate_button_basic = tk.Button(button_frame3, text="Calculate", command=basic_calculate_and_focus, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button_basic.pack(side=tk.LEFT, padx=(0, 5))

clear_button_basic = tk.Button(button_frame3, text="Clear", command=clear_basic_calculator_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_button_basic.pack(side=tk.LEFT, padx=(5, 0))

result_label_basic = tk.Label(frame3, text="Result: ")
result_label_basic.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

basic_heading = tk.Label(frame3, text="Basic Calculation Steps", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
basic_heading.grid(row=3, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
basic_heading.grid_remove()

basic_steps_label = tk.Label(frame3, text="", font=("Helvetica", 8), fg="grey", anchor="center")
basic_steps_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
basic_steps_label.grid_remove()

toggle_button_basic = tk.Button(frame3, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button_basic.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Add Decimals button for Basic Calculator
decimal_button3 = tk.Button(frame3, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button3.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button3)

# Enter Key Bindings for VAT Calculator
def bind_vat_calculator():
    vat_initial_amount_entry.bind('<Return>', lambda event: vat_percentage_entry.focus_set())
    vat_percentage_entry.bind('<Return>', lambda event: add_vat_button.focus_set())
    add_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=True))
    subtract_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=False))
    clear_vat_button.bind('<Return>', lambda event: clear_vat_calculator_and_focus())

# Enter Key Bindings for Calculator 1
def bind_calculator1():
    old_entry.bind('<Return>', lambda event: new_entry.focus_set())
    new_entry.bind('<Return>', lambda event: calculate_button1.invoke())
    calculate_button1.bind('<Return>', lambda event: clear_button1.focus_set())
    clear_button1.bind('<Return>', lambda event: clear_calculator1())

# Enter Key Bindings for Calculator 2
def bind_calculator2():
    old_value_entry.bind('<Return>', lambda event: percent_value_entry.focus_set())
    percent_value_entry.bind('<Return>', lambda event: operation_combobox.focus_set())
    operation_combobox.bind('<Return>', lambda event: calculate_button2.invoke())
    calculate_button2.bind('<Return>', lambda event: clear_button2.focus_set())
    clear_button2.bind('<Return>', lambda event: clear_calculator2())

# Enter Key Bindings for Basic Calculator
def bind_basic_calculator():
    entry_expression.bind('<Return>', lambda event: calculate_button_basic.invoke())
    calculate_button_basic.bind('<Return>', lambda event: clear_button_basic.focus_set())
    clear_button_basic.bind('<Return>', lambda event: clear_basic_calculator())

# Call the binding functions
bind_vat_calculator()
bind_calculator1()
bind_calculator2()
bind_basic_calculator()

# Main loop
root.mainloop()
