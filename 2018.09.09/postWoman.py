from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

def render_ui():
    root = Tk()
    root.geometry("1000x500+500+200")

    L_titile = Label(root , text = '小明专版postwoman')
    L_titile.config(font = 'Helvetica -15 bold' , fg = '#ff0000')
    L_titile.place(x = 80 , y = 10 , anchor = "center")
    L_author = Label(root , text = 'author:CodingXXM')
    L_author.config(font = 'Helvetica -10 bold')
    L_author.place(x = 900 , y = 480)

    mainloop()

if __name__ == "__main__":
    render_ui()
