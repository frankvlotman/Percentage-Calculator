import tkinter as tk
from tkinter import ttk
from PIL import Image

def calculate_percentage(event=None):
    try:
        old_value = float(old_entry.get())
        new_value = float(new_entry.get())
        difference = new_value - old_value
        percentage = (difference / old_value) * 100
        result_label.config(text="Percentage Change: {:.2f}%".format(percentage))
        
        desktop_steps = (
            f"Step 1: Subtract old value from new value: {new_value:.2f} - {old_value:.2f} = {difference:.2f}\n"
            f"Step 2: Divide the difference by the old value: {difference:.2f} / {old_value:.2f} = {difference / old_value:.2f}\n"
            f"Step 3: Multiply the result by 100 to get the percentage: ({difference / old_value:.2f}) * 100 = {percentage:.2f}%"
        )
        
        excel_steps = (
            "=((New Value - Old Value) / Old Value) * 100\n"
            f"Example: =(({new_value:.2f} - {old_value:.2f}) / {old_value:.2f}) * 100"
        )
        
        desktop_steps_label.config(text=desktop_steps)
        excel_steps_label.config(text=excel_steps)
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def clear_values(event=None):
    old_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    result_label.config(text="Percentage Change: ")
    desktop_steps_label.config(text="")
    excel_steps_label.config(text="")

def move_to_next(event):
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_new_value(event=None):
    try:
        old_value = float(old_value_entry.get())
        percent_value = float(percent_value_entry.get())
        operation = operation_var.get()

        if operation == "Increase":
            new_value = old_value * (1 + percent_value / 100)
            operation_text = f"{old_value:.2f} * (1 + {percent_value / 100:.2f})"
        elif operation == "Decrease":
            new_value = old_value * (1 - percent_value / 100)
            operation_text = f"{old_value:.2f} * (1 - {percent_value / 100:.2f})"
        else:
            raise ValueError("Invalid operation selected")

        new_value_entry.delete(0, tk.END)
        new_value_entry.insert(0, "{:.2f}".format(new_value))
        clear_button2.focus()  # Focus on Clear button after calculation
        
        desktop_steps = (
            f"Step 1: Determine the operation: {operation}\n"
            f"Step 2: Apply the operation: {operation_text} = {new_value:.2f}"
        )
        
        excel_steps = (
            "=Old Value * (1 + (Percent Value / 100)) (for Increase)\n"
            "=Old Value * (1 - (Percent Value / 100)) (for Decrease)\n"
            f"Example for Increase: ={old_value:.2f} * (1 + ({percent_value:.2f} / 100))\n"
            f"Example for Decrease: ={old_value:.2f} * (1 - ({percent_value:.2f} / 100))"
        )
        
        desktop_steps_label2.config(text=desktop_steps)
        excel_steps_label2.config(text=excel_steps)
    except ValueError:
        result_label2.config(text="Please enter valid numeric values for old value and percent value.")

def clear_values2(event=None):
    old_value_entry.delete(0, tk.END)
    percent_value_entry.delete(0, tk.END)
    new_value_entry.delete(0, tk.END)
    result_label2.config(text="")
    desktop_steps_label2.config(text="")
    excel_steps_label2.config(text="")
    old_value_entry.focus()

def toggle_calculations():
    widgets = [
        desktop_heading, desktop_steps_label, excel_heading, excel_steps_label,
        desktop_heading2, desktop_steps_label2, excel_heading2, excel_steps_label2
    ]
    for widget in widgets:
        if widget.winfo_viewable():
            widget.grid_remove()
        else:
            widget.grid()

root = tk.Tk()
root.title("Calculator")

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Calculator 1')
tab_control.add(tab2, text='Calculator 2')

tab_control.pack(expand=1, fill='both')

# Common style for calculation steps
steps_style = {"font": ("Helvetica", 8), "fg": "grey", "justify": tk.LEFT}

# Calculator 1
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

desktop_steps_label = tk.Label(frame1, text="", **steps_style, anchor="center")
desktop_steps_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label.grid_remove()

excel_heading = tk.Label(frame1, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading.grid(row=7, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading.grid_remove()

excel_steps_label = tk.Label(frame1, text="", **steps_style, anchor="center")
excel_steps_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label.grid_remove()

toggle_button = tk.Button(frame1, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="we")

root.bind('<Return>', move_to_next)
old_entry.bind('<Return>', move_to_next)
new_entry.bind('<Return>', calculate_percentage)
clear_button.bind('<Return>', clear_values)

# Calculator 2
frame2 = tk.Frame(tab2)
frame2.pack(padx=10, pady=10)

tk.Label(frame2, text="Old Value:").grid(row=0, column=0, padx=5, pady=5)
old_value_entry = tk.Entry(frame2)
old_value_entry.grid(row=0, column=1, padx=5, pady=5)
old_value_entry.bind("<Return>", lambda event: percent_value_entry.focus())

tk.Label(frame2, text="Percent Value:").grid(row=1, column=0, padx=5, pady=5)
percent_value_entry = tk.Entry(frame2)
percent_value_entry.grid(row=1, column=1, padx=5, pady=5)
percent_value_entry.bind("<Return>", lambda event: operation_combobox.focus())

tk.Label(frame2, text="Operation:").grid(row=2, column=0, padx=5, pady=5)
operation_var = tk.StringVar(frame2)
operation_combobox = ttk.Combobox(frame2, textvariable=operation_var, values=["Increase", "Decrease"])
operation_combobox.grid(row=2, column=1, padx=5, pady=5)
operation_combobox.current(0)
operation_combobox.bind("<Return>", lambda event: calculate_button2.focus())

calculate_button2 = tk.Button(frame2, text="Calculate", command=calculate_new_value, bg="#d0e8f1", font=("Helvetica", 8))
calculate_button2.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
calculate_button2.bind("<Return>", lambda event: calculate_new_value())

tk.Label(frame2, text="New Value:").grid(row=4, column=0, padx=5, pady=5)
new_value_entry = tk.Entry(frame2)
new_value_entry.grid(row=4, column=1, padx=5, pady=5)

clear_button2 = tk.Button(frame2, text="Clear", command=clear_values2, bg="#d0e8f1", font=("Helvetica", 8))
clear_button2.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
clear_button2.bind("<Return>", lambda event: clear_values2())
clear_button2.bind("<Tab>", lambda event: old_value_entry.focus())

toggle_button2 = tk.Button(frame2, text="Show Calculations", command=toggle_calculations, bg="#f9f9f9", font=("Helvetica", 7))
toggle_button2.grid(row=6, column=1, columnspan=1, padx=5, pady=5, sticky="we")

result_label2 = tk.Label(frame2, text="")
result_label2.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

desktop_heading2 = tk.Label(frame2, text="Desktop Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
desktop_heading2.grid(row=8, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
desktop_heading2.grid_remove()

desktop_steps_label2 = tk.Label(frame2, text="", **steps_style, anchor="center")
desktop_steps_label2.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")
desktop_steps_label2.grid_remove()

excel_heading2 = tk.Label(frame2, text="Excel Calculation", font=("Helvetica", 8, "bold", "underline"), fg="grey", anchor="center")
excel_heading2.grid(row=10, column=0, columnspan=2, padx=5, pady=(20, 5), sticky="we")
excel_heading2.grid_remove()

excel_steps_label2 = tk.Label(frame2, text="", **steps_style, anchor="center")
excel_steps_label2.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")
excel_steps_label2.grid_remove()

root.mainloop()
