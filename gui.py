import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Anwesendheitkontrolle")
root.geometry("350x100")

# initialize style 
s = ttk.Style()
s.configure ("TFrame", background="lightblue")
s.configure("TCheckbutton", background="lightblue" )

varAnw = tk.BooleanVar()

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)
frame.columnconfigure(0, weight=1) # allow column 0 to expand

check = ttk.Checkbutton (frame, text="anwesend", variable=varAnw)
check.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10) # grid is responsible for placement, sticky means "stick to this side"

button_ok = ttk.Button(frame, text="ok", width=10, command=root.destroy)
button_ok.grid(row=2, column=0, sticky=tk.SE, pady=10, padx=10)

root.mainloop() # start event loop, keep window responsive
