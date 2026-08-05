import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main_window():

    root = tk.Tk()
    varAnw = tk.IntVar()

    root.title("Anwesendheitkontrolle")
    root.minsize(350, 125)

    # initialize style 
    style = ttk.Style()
    style.configure ("TFrame", background="lightblue")
    style.configure("TCheckbutton", background="lightblue" )

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill="both", expand=True)
    frame.columnconfigure(0, weight=1) # allow column 0 to expand 
    frame.rowconfigure(1, weight=1) # allow row 1 to expand

    check = ttk.Checkbutton (frame, text="anwesend", variable=varAnw)
    check.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10) # grid is responsible for placement, sticky means "stick to this side"

    button_ok = ttk.Button(frame, text="ok", width=10, command=root.quit)
    button_ok.grid(row=1, column=0, sticky=tk.SE, pady=10, padx=10)

    root.mainloop() # start event loop, keep window responsive
    present = varAnw.get()
    return present

def confirm_non_workday():
    answer = messagebox.askokcancel(
        "Warnung",
        "Heute ist kein normaler Arbeitstag.\n Möchten Sie trotzdem fortfahren?"
    )
    return answer
        