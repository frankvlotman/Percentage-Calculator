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
        
        net_amount_label.config(text=f"Net Amount: {total_amount:.2f}")
        vat_result_label.config(text=f"VAT: {vat_value:.2f}")
        total_amount_label.config(text=f"Total: {initial_amount:.2f}")
    except ValueError:
        vat_result_label.config(text="Please enter valid numbers.")

# Percentage Change Calculator (Calculator 1)
def calculate_percentage(event=None):
    try:
        old_value = float(old_entry.get())
        new_value = float(new_entry.get())
        difference = new_value - old_value
        percentage = (difference / old_value) * 100
        result_label.config(text="Percentage Change: {:.2f}%".format(percentage))

        # Desktop steps
        desktop_steps = (
            f"Step 1: Subtract old value from new value: {new_value:.2f} - {old_value:.2f} = {difference:.2f}\n"
            f"Step 2: Divide the difference by the old value: {difference:.2f} / {old_value:.2f} = {difference / old_value:.2f}\n"
            f"Step 3: Multiply by 100 to get the percentage: ({difference / old_value:.2f}) * 100 = {percentage:.2f}%"
        )
        desktop_steps_label.config(text=desktop_steps)
        
        # Excel steps
        excel_steps = (
            "=((New Value - Old Value) / Old Value) * 100\n"
            f"Example: =(({new_value:.2f} - {old_value:.2f}) / {old_value:.2f}) * 100"
        )
        excel_steps_label.config(text=excel_steps)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def clear_values(event=None):
    old_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    result_label.config(text="Percentage Change: ")
    desktop_steps_label.config(text="")
    excel_steps_label.config(text="")

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
        new_value_entry.insert(0, "{:.2f}".format(new_value))
        result_label2.config(text=f"New Value: {new_value:.2f}")

        # Desktop steps for Increase/Decrease
        desktop_steps2 = (
            f"Step 1: Operation chosen: {operation}\n"
            f"Step 2: Calculation: {old_value:.2f} * (1 {'+' if operation == 'Increase' else '-'} {percent_value:.2f}%) = {new_value:.2f}"
        )
        desktop_steps_label2.config(text=desktop_steps2)
        
        # Excel steps for Increase/Decrease
        excel_steps2 = (
            f"=Old Value * (1 + (Percent Value / 100)) (for Increase)\n"
            f"=Old Value * (1 - (Percent Value / 100)) (for Decrease)\n"
            f"Example for Increase: ={old_value:.2f} * (1 + {percent_value / 100:.2f})\n"
            f"Example for Decrease: ={old_value:.2f} * (1 - {percent_value / 100:.2f})"
        )
        excel_steps_label2.config(text=excel_steps2)
    except ValueError:
        result_label2.config(text="Please enter valid numeric values.")

def clear_values2(event=None):
    old_value_entry.delete(0, tk.END)
    percent_value_entry.delete(0, tk.END)
    new_value_entry.delete(0, tk.END)
    result_label2.config(text="")
    desktop_steps_label2.config(text="")
    excel_steps_label2.config(text="")

# Basic Calculator (Calculator 3)
def basic_calculate(event=None):
    try:
        expression = entry_expression.get()  
        result = eval(expression)  
        result_label_basic.config(text="Result: {:,.6f}".format(result).rstrip('0').rstrip('.'))

        # Show basic calculation steps (for simplicity, just echoing the expression)
        basic_steps = f"Calculation performed: {expression} = {result:.2f}"
        basic_steps_label.config(text=basic_steps)

    except (ValueError, SyntaxError, ZeroDivisionError):
        result_label_basic.config(text="Enter a valid expression")

def clear_basic(event=None):
    entry_expression.delete(0, tk.END)
    result_label_basic.config(text="Result: ")
    basic_steps_label.config(text="")
    entry_expression.focus()

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

# Bind Enter key for VAT Calculator
vat_initial_amount_entry.bind('<Return>', lambda event: vat_percentage_entry.focus())
vat_percentage_entry.bind('<Return>', lambda event: add_vat_button.focus())
add_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=True))
subtract_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=False))

# Calculator 1 Tab (Percentage Change)
frame1 = tk.Frame(tab1)
frame1.pack(padx=10, pady=10)

old_label = tk.Label(frame1, text="Old Value:")
old_label.grid(row=0, column=0, padx=5, pady=5)
old_entry = tk.Entry(frame1)
old_entry.grid(row=0, column=1, padx=5, pady=5)
old_entry.focus()

new_label = tk.Label(frame1, text="New Value:")
new_label.grid(row=1, column=0, padx=5, pady=5)
new_entry = tk.Entry(frame1)
new_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame1, text="Calculate", command=calculate_percentage, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button.grid(row=2, column=0, padx=2, pady=5, sticky="we")

clear_button = tk.Button(frame1, text="Clear", command=clear_values, bg="#d0e8f1", font=("Helvetica", 8))
clear_button.grid(row=2, column=1, padx=2, pady=5, sticky="we")

result_label = tk.Label(frame1, text="Percentage Change: ", anchor="center")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

desktop_heading = tk.Label(frame1, text="Desktop Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
desktop_heading.grid(row=5, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
desktop_heading.grid_remove()

desktop_steps_label = tk.Label(frame1, text="", font=("Helvetica", 8), fg="grey", anchor="center")
desktop_steps_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label.grid_remove()

excel_heading = tk.Label(frame1, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading.grid(row=7, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading.grid_remove()

excel_steps_label = tk.Label(frame1, text="", font=("Helvetica", 8), fg="grey", anchor="center")
excel_steps_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label.grid_remove()

toggle_button = tk.Button(frame1, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="we")

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

result_label2 = tk.Label(frame2, text="")
result_label2.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

desktop_heading2 = tk.Label(frame2, text="Desktop Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
desktop_heading2.grid(row=8, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
desktop_heading2.grid_remove()

desktop_steps_label2 = tk.Label(frame2, text="", font=("Helvetica", 8), fg="grey", anchor="center")
desktop_steps_label2.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label2.grid_remove()

excel_heading2 = tk.Label(frame2, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading2.grid(row=10, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading2.grid_remove()

excel_steps_label2 = tk.Label(frame2, text="", font=("Helvetica", 8), fg="grey", anchor="center")
excel_steps_label2.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label2.grid_remove()

toggle_button2 = tk.Button(frame2, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button2.grid(row=6, column=1, columnspan=1, padx=5, pady=5, sticky="we")

# Basic Calculator Tab (Calculator 3)
frame3 = tk.Frame(tab3)
frame3.pack(padx=10, pady=10)

tk.Label(frame3, text="Expression:").grid(row=0, column=0, padx=5, pady=5)
entry_expression = tk.Entry(frame3)
entry_expression.grid(row=0, column=1, padx=5, pady=5)
entry_expression.focus()

calculate_button_basic = tk.Button(frame3, text="Calculate", command=basic_calculate, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button_basic.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

clear_button_basic = tk.Button(frame3, text="Clear", command=clear_basic, bg="#d0e8f1", font=("Helvetica", 8))
clear_button_basic.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label_basic = tk.Label(frame3, text="Result: ")
result_label_basic.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

basic_heading = tk.Label(frame3, text="Basic Calculation Steps", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
basic_heading.grid(row=4, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
basic_heading.grid_remove()

basic_steps_label = tk.Label(frame3, text="", font=("Helvetica", 8), fg="grey", anchor="center")
basic_steps_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
basic_steps_label.grid_remove()

toggle_button_basic = tk.Button(frame3, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button_basic.grid(row=6, column=1, columnspan=1, padx=5, pady=5, sticky="we")

# Bind Enter key for all fields
old_entry.bind('<Return>', lambda event: new_entry.focus())
new_entry.bind('<Return>', lambda event: calculate_button.focus())
old_value_entry.bind('<Return>', lambda event: percent_value_entry.focus())
percent_value_entry.bind('<Return>', lambda event: operation_combobox.focus())
operation_combobox.bind('<Return>', lambda event: calculate_button2.focus())
entry_expression.bind('<Return>', lambda event: calculate_button_basic.focus())
calculate_button.bind('<Return>', calculate_percentage)
calculate_button2.bind('<Return>', calculate_new_value)
calculate_button_basic.bind('<Return>', basic_calculate)

# Main loop
root.mainloop()
