import tkinter as tk
from tkinter import *

def test_fun():
    root = tk.Tk()
    root.title('Form')
    root.geometry("250x160")


    #variable
    var = IntVar()
    #label
    l1 = Label(root,text="Radio Buttons working",font=("verdana",10,"bold"))
    l1.grid(sticky="w",padx=60)

    #radiobuttons
    r1 = Radiobutton(root,text="R1", value=1,variable=var)
    r1.grid(sticky="w",row=1,pady=10)

    #label
    l2 = Label(root,text="Check Buttons",font=("verdana",10,"bold"))
    l2.grid(sticky="w",padx=60)

    #checkbuttons
    c1 = Checkbutton(root,text="C1")
    c1.grid(row=3,sticky="w",pady=10)


    root.mainloop()


test_fun()