from tkinter import *
from tkinter import ttk


def hello():
    print("Bonjour")
def main():

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Hello", command=hello).grid(column=1, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()


if __name__ == '__main__':
    main()
