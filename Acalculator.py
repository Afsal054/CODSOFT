import tkinter as tk

def add_to_display(value):
    current = display.get()
    display.set(current + str(value))

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.set(result)
    except Exception as e:
        display.set("Error")

def clear_display():
    display.set("")

root = tk.Tk()
root.title("Colorful Calculator")

display = tk.StringVar()
display.set("")


display_entry = tk.Entry(root, textvariable=display, font=('Arial', 18), bd=10, insertwidth=4, width=15, justify='right')
display_entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in buttons:
    if text != '=':
        button = tk.Button(root, text=text, padx=20, pady=10, font=('Arial', 14), command=lambda t=text: add_to_display(t))
        button.grid(row=row, column=col, padx=5, pady=5)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, font=('Arial', 14), bg='green', fg='white', command=calculate)
        button.grid(row=row, column=col, padx=5, pady=5)
    if text == 'C':
        button.configure(bg='red', command=clear_display)

root.mainloop()
