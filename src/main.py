import tkinter as tk

root = tk.Tk()
root.title("Hello World")

label = tk.Label(root, text="Hello World")
label.pack()
root.geometry("300x200")
root.mainloop()

