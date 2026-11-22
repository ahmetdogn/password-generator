import tkinter as tk
from tkinter import messagebox
from password import generate_password


def generate():
    password = generate_password(length.get(), upper.get(), lower.get(), numbers.get(), symbols.get())
    if password is None:
        messagebox.showerror("Error", "You have to choose at least one option!")
        return
    output.delete(0, tk.END)
    output.insert(0, password)


def copy():
    root.clipboard_clear()
    root.clipboard_append(output.get())


root = tk.Tk()
root.title("Password Generator")

length = tk.IntVar(value=12)
upper = tk.BooleanVar(value=True)
lower = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)

tk.Label(root, text="Length").pack()
tk.Scale(root, from_=4, to=50, orient="horizontal", variable=length).pack()

tk.Checkbutton(root, text="Uppercase", variable=upper).pack()
tk.Checkbutton(root, text="Lowercase", variable=lower).pack()
tk.Checkbutton(root, text="Numbers", variable=numbers).pack()
tk.Checkbutton(root, text="Symbols", variable=symbols).pack()

output = tk.Entry(root, width=30)
output.pack(pady=10)

tk.Button(root, text="Generate", command=generate).pack()
tk.Button(root, text="Copy", command=copy).pack(pady=5)

root.mainloop()
