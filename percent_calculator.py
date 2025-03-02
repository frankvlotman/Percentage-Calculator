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

# Global variables for Basic Calculator results
basic_result_value = ""   # Formatted for display
basic_result_plain = ""   # Plain value for copying

# Global variables for VAT Calculator plain values
net_amount_plain = ""
vat_plain = ""
total_plain = ""

# Function to toggle between 2, 5, and 8 decimal places
def toggle_decimal_places():
    global decimal_places
    if decimal_places == 2:
        decimal_places = 5
    elif decimal_places == 5:
        decimal_places = 8
    else:
        decimal_places = 2
    for button in decimal_buttons:
        button.config(text=f"Decimals: {decimal_places}")

# ----------------- VAT Calculator Functions -----------------
def calculate_vat(add_vat=True):
    global net_amount_plain, vat_plain, total_plain
    try:
        initial_amount = float(vat_initial_amount_entry.get())
        vat_percentage = float(vat_percentage_entry.get())
        
        if add_vat:
            vat_value = (initial_amount * vat_percentage) / 100
            total_amount = initial_amount + vat_value
        else:
            total_amount = initial_amount / (1 + (vat_percentage / 100))
            vat_value = initial_amount - total_amount
        
        # Formatted for display (with thousand separators)
        net_amount_display = f"{total_amount:,.{decimal_places}f}"
        vat_display = f"{vat_value:,.{decimal_places}f}"
        total_display = f"{initial_amount:,.{decimal_places}f}"
        net_amount_label.config(text=f"Net Amount: {net_amount_display}")
        vat_result_label.config(text=f"VAT: {vat_display}")
        total_amount_label.config(text=f"Total: {total_display}")
        
        # Plain (without thousand separators)
        net_amount_plain = f"{total_amount:.{decimal_places}f}"
        vat_plain = f"{vat_value:.{decimal_places}f}"
        total_plain = f"{initial_amount:.{decimal_places}f}"
    except ValueError:
        vat_result_label.config(text="Please enter valid numbers.")
        net_amount_plain = vat_plain = total_plain = ""

def clear_vat_calculator():
    vat_initial_amount_entry.delete(0, tk.END)
    vat_percentage_entry.delete(0, tk.END)
    net_amount_label.config(text="Net Amount: ")
    vat_result_label.config(text="VAT: ")
    total_amount_label.config(text="Total: ")
    vat_initial_amount_entry.focus_set()

def clear_vat_calculator_and_focus(event=None):
    clear_vat_calculator()
    vat_initial_amount_entry.focus_set()

def copy_net_amount(event):
    if net_amount_plain:
        root.clipboard_clear()
        root.clipboard_append(net_amount_plain)
        net_copy_label.config(text="Copied")
        net_copy_label.after(1500, lambda: net_copy_label.config(text=""))

def copy_vat(event):
    if vat_plain:
        root.clipboard_clear()
        root.clipboard_append(vat_plain)
        vat_copy_label.config(text="Copied")
        vat_copy_label.after(1500, lambda: vat_copy_label.config(text=""))

def copy_total(event):
    if total_plain:
        root.clipboard_clear()
        root.clipboard_append(total_plain)
        total_copy_label.config(text="Copied")
        total_copy_label.after(1500, lambda: total_copy_label.config(text=""))

# ----------------- Calculator 1 (Percentage Change) Functions -----------------
def calculate_percentage(event=None):
    try:
        old_value = float(old_entry.get())
        new_value = float(new_entry.get())
        difference = new_value - old_value
        percentage = (difference / old_value) * 100
        result_label.config(text=f"Percentage Change: {percentage:,.{decimal_places}f}%")
        desktop_steps = (
            f"Step 1: {new_value:,.{decimal_places}f} - {old_value:,.{decimal_places}f} = {difference:,.{decimal_places}f}\n"
            f"Step 2: {difference:,.{decimal_places}f} / {old_value:,.{decimal_places}f} = {difference/old_value:,.{decimal_places}f}\n"
            f"Step 3: ({difference/old_value:,.{decimal_places}f}) * 100 = {percentage:,.{decimal_places}f}%"
        )
        desktop_steps_label.config(text=desktop_steps)
        excel_steps = (
            f"=((New Value - Old Value) / Old Value) * 100\n"
            f"Example: =(({new_value:,.{decimal_places}f} - {old_value:,.{decimal_places}f}) / {old_value:,.{decimal_places}f}) * 100"
        )
        excel_steps_label.config(text=excel_steps)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def clear_calculator1():
    old_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    result_label.config(text="Percentage Change: ")
    desktop_steps_label.config(text="")
    excel_steps_label.config(text="")
    old_entry.focus_set()

def calculate_percentage_and_focus(event=None):
    calculate_percentage()
    clear_button1.focus_set()

def clear_calculator1_and_focus(event=None):
    clear_calculator1()
    old_entry.focus_set()

# ----------------- Calculator 2 (Increase/Decrease) Functions -----------------
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
        desktop_steps2 = (
            f"Step 1: Operation: {operation}\n"
            f"Step 2: {old_value:,.{decimal_places}f} * (1 {'+' if operation == 'Increase' else '-'} {percent_value:,.{decimal_places}f}%) = {new_value:,.{decimal_places}f}"
        )
        desktop_steps_label2.config(text=desktop_steps2)
        excel_steps2 = (
            f"=Old Value * (1 + (Percent Value / 100)) (for Increase)\n"
            f"=Old Value * (1 - (Percent Value / 100)) (for Decrease)\n"
            f"Example: = {old_value:,.{decimal_places}f} * (1 {'+' if operation == 'Increase' else '-'} {percent_value/100:,.{decimal_places}f})"
        )
        excel_steps_label2.config(text=excel_steps2)
    except ValueError:
        result_label2.config(text="Please enter valid numeric values.")

def clear_calculator2():
    old_value_entry.delete(0, tk.END)
    percent_value_entry.delete(0, tk.END)
    operation_combobox.current(0)
    new_value_entry.delete(0, tk.END)
    result_label2.config(text="New Value: ")
    desktop_steps_label2.config(text="")
    excel_steps_label2.config(text="")
    old_value_entry.focus_set()

def calculate_new_value_and_focus(event=None):
    calculate_new_value()
    clear_button2.focus_set()

def clear_calculator2_and_focus(event=None):
    clear_calculator2()
    old_value_entry.focus_set()

# ----------------- Basic Calculator Functions -----------------
def basic_calculate(event=None):
    global basic_result_value, basic_result_plain
    try:
        expression = entry_expression.get()  
        result = eval(expression)  
        formatted_result = f"{result:,.{decimal_places}f}"
        plain_result = f"{result:.{decimal_places}f}"
        basic_result_value = formatted_result
        basic_result_plain = plain_result
        result_label_basic.config(text=f"Result: {formatted_result}")
        basic_steps = f"Calculation performed: {expression} = {formatted_result}"
        basic_steps_label.config(text=basic_steps)
    except (ValueError, SyntaxError, ZeroDivisionError):
        result_label_basic.config(text="Enter a valid expression")
        basic_result_value = ""
        basic_result_plain = ""

def clear_basic_calculator():
    entry_expression.delete(0, tk.END)
    result_label_basic.config(text="Result: ")
    basic_steps_label.config(text="")
    entry_expression.focus_set()

def basic_calculate_and_focus(event=None):
    basic_calculate()
    clear_button_basic.focus_set()

def clear_basic_calculator_and_focus(event=None):
    clear_basic_calculator()
    entry_expression.focus_set()

def copy_basic_result(event):
    global basic_result_plain
    if basic_result_plain:
        root.clipboard_clear()
        root.clipboard_append(basic_result_plain)
        copy_confirmation_label.config(text="Copied")
        copy_confirmation_label.after(1500, lambda: copy_confirmation_label.config(text=""))

# ----------------- Custom Calculator Functions -----------------
def custom_calculate(event=None):
    try:
        expression1 = entry_custom_expression1.get()
        expression2 = entry_custom_expression2.get()
        operation = custom_operation_var.get()
        result1 = eval(expression1)
        result2 = eval(expression2)
        if operation == "Addition":
            grand_total = result1 + result2
            operation_symbol = '+'
        elif operation == "Subtraction":
            grand_total = result1 - result2
            operation_symbol = '-'
        elif operation == "Multiplication":
            grand_total = result1 * result2
            operation_symbol = '*'
        elif operation == "Division":
            if result2 == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            grand_total = result1 / result2
            operation_symbol = '/'
        else:
            grand_total = 0
            operation_symbol = '?'
        formatted_result1 = f"{result1:,.{decimal_places}f}"
        formatted_result2 = f"{result2:,.{decimal_places}f}"
        formatted_grand_total = f"{grand_total:,.{decimal_places}f}"
        result_label_custom1.config(text=f"Result 1: {formatted_result1}")
        result_label_custom2.config(text=f"Result 2: {formatted_result2}")
        grand_total_label_custom.config(text=f"Grand Total: {formatted_grand_total}")
        custom_steps = (
            f"Calculation 1: {expression1} = {formatted_result1}\n"
            f"Calculation 2: {expression2} = {formatted_result2}\n"
            f"Grand Total ({operation_symbol}): {formatted_result1} {operation_symbol} {formatted_result2} = {formatted_grand_total}"
        )
        custom_steps_label.config(text=custom_steps)
    except (ValueError, SyntaxError):
        result_label_custom1.config(text="Result 1: Error")
        result_label_custom2.config(text="Result 2: Error")
        grand_total_label_custom.config(text="Grand Total: Error")
        custom_steps_label.config(text="Enter valid expressions")
    except ZeroDivisionError:
        result_label_custom1.config(text=f"Result 1: {result1:,.{decimal_places}f}")
        result_label_custom2.config(text="Result 2: Error (Division by Zero)")
        grand_total_label_custom.config(text="Grand Total: Error")
        custom_steps_label.config(text="Cannot divide by zero.")

def clear_custom_calculator():
    entry_custom_expression1.delete(0, tk.END)
    entry_custom_expression2.delete(0, tk.END)
    result_label_custom1.config(text="Result 1: ")
    result_label_custom2.config(text="Result 2: ")
    grand_total_label_custom.config(text="Grand Total: ")
    custom_steps_label.config(text="")
    entry_custom_expression1.focus_set()

def custom_calculate_and_focus(event=None):
    custom_calculate()
    clear_button_custom.focus_set()

def clear_custom_calculator_and_focus(event=None):
    clear_custom_calculator()
    entry_custom_expression1.focus_set()

# ----------------- Toggle Calculations Visibility -----------------
def toggle_calculations():
    widgets = [
        desktop_heading, desktop_steps_label, excel_heading, excel_steps_label,
        desktop_heading2, desktop_steps_label2, excel_heading2, excel_steps_label2,
        basic_heading, basic_steps_label,
        custom_heading, custom_steps_label
    ]
    for widget in widgets:
        if widget.winfo_viewable():
            widget.grid_remove()
        else:
            widget.grid()

# ----------------- Main Application Setup -----------------
root = tk.Tk()
root.title("Calculator")
root.attributes('-topmost', True)
root.iconbitmap(icon_path)

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_custom = ttk.Frame(tab_control)
tab_vat = ttk.Frame(tab_control)

tab_control.add(tab1, text='Calculator 1')  
tab_control.add(tab2, text='Calculator 2')  
tab_control.add(tab3, text='Basic Calculator')
tab_control.add(tab_custom, text='Custom')
tab_control.add(tab_vat, text='VAT Calculator')  
tab_control.pack(expand=1, fill='both')

# Set "Basic Calculator" as the default tab
tab_control.select(tab3)

# ----------------- VAT Calculator Tab -----------------
vat_frame = tk.Frame(tab_vat)
vat_frame.pack(padx=10, pady=10)

tk.Label(vat_frame, text="Initial Amount:").grid(row=0, column=0, padx=5, pady=5)
vat_initial_amount_entry = tk.Entry(vat_frame)
vat_initial_amount_entry.grid(row=0, column=1, padx=5, pady=5)
vat_initial_amount_entry.focus()

tk.Label(vat_frame, text="VAT %:").grid(row=1, column=0, padx=5, pady=5)
vat_percentage_entry = tk.Entry(vat_frame)
vat_percentage_entry.grid(row=1, column=1, padx=5, pady=5)
vat_percentage_entry.insert(0, "20")  # Default VAT percentage

button_frame_vat = tk.Frame(vat_frame)
button_frame_vat.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
add_vat_button = tk.Button(button_frame_vat, text="Add VAT", command=lambda: calculate_vat(add_vat=True), bg="#d0e8f1", font=("Helvetica", 8))
add_vat_button.pack(side=tk.LEFT, padx=(0, 5))
subtract_vat_button = tk.Button(button_frame_vat, text="Subtract VAT", command=lambda: calculate_vat(add_vat=False), bg="#d0e8f1", font=("Helvetica", 8))
subtract_vat_button.pack(side=tk.LEFT, padx=(5, 5))
clear_vat_button = tk.Button(button_frame_vat, text="Clear", command=clear_vat_calculator_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_vat_button.pack(side=tk.LEFT, padx=(5, 0))

# Center result labels by spanning two columns and using sticky="ew"
net_amount_label = tk.Label(vat_frame, text="Net Amount: ", font=("Helvetica", 10, "bold"), anchor="center")
net_amount_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
net_copy_label = tk.Label(vat_frame, text="", font=("Helvetica", 8), fg="green")
net_copy_label.grid(row=3, column=2, padx=5, pady=5, sticky="w")

vat_result_label = tk.Label(vat_frame, text="VAT: ", anchor="center")
vat_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
vat_copy_label = tk.Label(vat_frame, text="", font=("Helvetica", 8), fg="green")
vat_copy_label.grid(row=4, column=2, padx=5, pady=5, sticky="w")

total_amount_label = tk.Label(vat_frame, text="Total: ", anchor="center")
total_amount_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
total_copy_label = tk.Label(vat_frame, text="", font=("Helvetica", 8), fg="green")
total_copy_label.grid(row=5, column=2, padx=5, pady=5, sticky="w")

decimal_button_vat = tk.Button(vat_frame, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button_vat.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
decimal_buttons.append(decimal_button_vat)

net_amount_label.bind("<Button-3>", copy_net_amount)
vat_result_label.bind("<Button-3>", copy_vat)
total_amount_label.bind("<Button-3>", copy_total)

# ----------------- Calculator 1 (Percentage Change) Tab -----------------
frame1 = tk.Frame(tab1)
frame1.pack(padx=10, pady=10)
tk.Label(frame1, text="Old Value:").grid(row=0, column=0, padx=5, pady=5)
old_entry = tk.Entry(frame1)
old_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame1, text="New Value:").grid(row=1, column=0, padx=5, pady=5)
new_entry = tk.Entry(frame1)
new_entry.grid(row=1, column=1, padx=5, pady=5)
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
decimal_button1 = tk.Button(frame1, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button1.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button1)

# ----------------- Calculator 2 (Increase/Decrease) Tab -----------------
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
decimal_button2 = tk.Button(frame2, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button2.grid(row=11, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button2)

# ----------------- Basic Calculator Tab -----------------
frame3 = tk.Frame(tab3)
frame3.pack(padx=10, pady=10)
tk.Label(frame3, text="Expression:").grid(row=0, column=0, padx=5, pady=5)
entry_expression = tk.Entry(frame3, width=50)
entry_expression.grid(row=0, column=1, padx=5, pady=5, sticky="we")
frame3.columnconfigure(1, weight=1)
button_frame3 = tk.Frame(frame3)
button_frame3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
calculate_button_basic = tk.Button(button_frame3, text="Calculate", command=basic_calculate_and_focus, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button_basic.pack(side=tk.LEFT, padx=(0, 5))
clear_button_basic = tk.Button(button_frame3, text="Clear", command=clear_basic_calculator_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_button_basic.pack(side=tk.LEFT, padx=(5, 0))
result_label_basic = tk.Label(frame3, text="Result: ", anchor="center", font=("Helvetica", 10))
result_label_basic.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
copy_confirmation_label = tk.Label(frame3, text="", font=("Helvetica", 8), fg="green")
copy_confirmation_label.grid(row=3, column=0, columnspan=2, padx=5, pady=2)
result_label_basic.bind("<Button-3>", copy_basic_result)
basic_heading = tk.Label(frame3, text="Basic Calculation Steps", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
basic_heading.grid(row=4, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
basic_heading.grid_remove()
basic_steps_label = tk.Label(frame3, text="", font=("Helvetica", 8), fg="grey", anchor="center")
basic_steps_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
basic_steps_label.grid_remove()
toggle_button_basic = tk.Button(frame3, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button_basic.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
decimal_button3 = tk.Button(frame3, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button3.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button3)

# ----------------- Custom Calculator Tab -----------------
frame_custom = tk.Frame(tab_custom)
frame_custom.pack(padx=10, pady=10)
tk.Label(frame_custom, text="Expression 1:").grid(row=0, column=0, padx=5, pady=5)
entry_custom_expression1 = tk.Entry(frame_custom, width=50)
entry_custom_expression1.grid(row=0, column=1, padx=5, pady=5, sticky="we")
tk.Label(frame_custom, text="Expression 2:").grid(row=1, column=0, padx=5, pady=5)
entry_custom_expression2 = tk.Entry(frame_custom, width=50)
entry_custom_expression2.grid(row=1, column=1, padx=5, pady=5, sticky="we")
tk.Label(frame_custom, text="Operation:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
custom_operation_var = tk.StringVar(value="Addition")
operation_frame = tk.Frame(frame_custom)
operation_frame.grid(row=2, column=1, padx=5, pady=5, sticky="w")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
for op in operations:
    tk.Radiobutton(operation_frame, text=op, variable=custom_operation_var, value=op, font=("Helvetica", 8)).pack(side=tk.LEFT, padx=5)
frame_custom.columnconfigure(1, weight=1)
button_frame_custom = tk.Frame(frame_custom)
button_frame_custom.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
calculate_button_custom = tk.Button(button_frame_custom, text="Calculate", command=custom_calculate_and_focus, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button_custom.pack(side=tk.LEFT, padx=(0, 5))
clear_button_custom = tk.Button(button_frame_custom, text="Clear", command=clear_custom_calculator_and_focus, bg="#f1d0d0", font=("Helvetica", 8))
clear_button_custom.pack(side=tk.LEFT, padx=(5, 0))
result_label_custom1 = tk.Label(frame_custom, text="Result 1: ")
result_label_custom1.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
result_label_custom2 = tk.Label(frame_custom, text="Result 2: ")
result_label_custom2.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
grand_total_label_custom = tk.Label(frame_custom, text="Grand Total: ")
grand_total_label_custom.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
custom_heading = tk.Label(frame_custom, text="Custom Calculation Steps", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
custom_heading.grid(row=7, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
custom_heading.grid_remove()
custom_steps_label = tk.Label(frame_custom, text="", font=("Helvetica", 8), fg="grey", anchor="center")
custom_steps_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
custom_steps_label.grid_remove()
toggle_button_custom = tk.Button(frame_custom, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button_custom.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
decimal_button_custom = tk.Button(frame_custom, text=f"Decimals: {decimal_places}", command=toggle_decimal_places, bg="#f9f9f9", font=("Helvetica", 8))
decimal_button_custom.grid(row=10, column=0, columnspan=2, padx=5, pady=5)
decimal_buttons.append(decimal_button_custom)

# ----------------- Bindings -----------------
def bind_vat_calculator():
    vat_initial_amount_entry.bind('<Return>', lambda event: vat_percentage_entry.focus_set())
    vat_percentage_entry.bind('<Return>', lambda event: add_vat_button.focus_set())
    add_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=True))
    subtract_vat_button.bind('<Return>', lambda event: calculate_vat(add_vat=False))
    clear_vat_button.bind('<Return>', lambda event: clear_vat_calculator_and_focus())

def bind_calculator1():
    old_entry.bind('<Return>', lambda event: new_entry.focus_set())
    new_entry.bind('<Return>', lambda event: calculate_button1.invoke())
    calculate_button1.bind('<Return>', lambda event: clear_button1.focus_set())
    clear_button1.bind('<Return>', lambda event: clear_calculator1())

def bind_calculator2():
    old_value_entry.bind('<Return>', lambda event: percent_value_entry.focus_set())
    percent_value_entry.bind('<Return>', lambda event: operation_combobox.focus_set())
    operation_combobox.bind('<Return>', lambda event: calculate_button2.invoke())
    calculate_button2.bind('<Return>', lambda event: clear_button2.focus_set())
    clear_button2.bind('<Return>', lambda event: clear_calculator2())

def bind_basic_calculator():
    entry_expression.bind('<Return>', lambda event: calculate_button_basic.invoke())
    calculate_button_basic.bind('<Return>', lambda event: clear_button_basic.focus_set())
    clear_button_basic.bind('<Return>', lambda event: clear_basic_calculator())

def bind_custom_calculator():
    entry_custom_expression1.bind('<Return>', lambda event: entry_custom_expression2.focus_set())
    entry_custom_expression2.bind('<Return>', lambda event: calculate_button_custom.invoke())
    calculate_button_custom.bind('<Return>', lambda event: clear_button_custom.focus_set())
    clear_button_custom.bind('<Return>', lambda event: clear_custom_calculator())

bind_vat_calculator()
bind_calculator1()
bind_calculator2()
bind_basic_calculator()
bind_custom_calculator()

def add_hover_effect(button, hover_color="#ffff99"):
    original_bg = button.cget("bg")
    button.bind("<Enter>", lambda event: button.config(bg=hover_color))
    button.bind("<Leave>", lambda event: button.config(bg=original_bg))

hover_buttons = [
    add_vat_button, subtract_vat_button, clear_vat_button, decimal_button_vat,
    calculate_button1, clear_button1, toggle_button, decimal_button1,
    calculate_button2, clear_button2, toggle_button2, decimal_button2,
    calculate_button_basic, clear_button_basic, toggle_button_basic, decimal_button3,
    calculate_button_custom, clear_button_custom, toggle_button_custom, decimal_button_custom
]
for btn in hover_buttons:
    add_hover_effect(btn)

# Set focus to the Expression input in the Basic Calculator when the app opens.
entry_expression.focus_set()

root.mainloop()
