import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name.strip() == '' or phone.strip() == '':
        messagebox.showwarning("Warning", "Please enter both name and phone number.")
    else:
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

def remove_contact():
    selected_item = contact_list.curselection()
    if selected_item:
        contact_list.delete(selected_item)
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

root = tk.Tk()
root.title("Contact Book")

 
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)


add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


contact_list = tk.Listbox(root, width=40, height=10)
contact_list.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Contact", command=remove_contact)
remove_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
