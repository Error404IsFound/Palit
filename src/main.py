import tkinter as tk

root = tk.Tk()
root.title("Frame Demo")
root.config(bg="#807E9D")

# Create Frame widget
frame = tk.Frame(root, width=500, height=700)
frame.pack(padx=10, pady=10)

root.mainloop()
