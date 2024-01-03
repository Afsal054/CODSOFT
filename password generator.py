import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        password_result.set("Invalid length")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_result.set(password)

root = tk.Tk()
root.title("Password Generator")

password_result = tk.StringVar()

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_display = tk.Label(root, textvariable=password_result, relief="sunken")
password_display.pack()

root.mainloop()
