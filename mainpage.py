from tkinter import *
from tkinter import ttk
from enterQue import *
# from deleteAndCreate import deleteAndCrt
from deleteAndCreate import *
from credential import *
from Result import *



import tkinter
root = Tk()

def teacher():
    # pass
    # frame.quit
    deleteAndCrt()
    # tecr()

def credential():
    # pass
    credentialInput()

def res():
    # pass
    result()

def showmain():

    root.title('Main Window ')

    root.geometry("500x500")

    f0 = Frame(root,bg="grey", borderwidth=2, relief=SUNKEN)
    f0.pack(side=TOP,fill="x")
    f1 = Frame(root,bg="White", borderwidth=7, relief=SUNKEN)
    f1.pack(side=RIGHT, fill="y")
    value=StringVar()



    lbl = ttk.Label(root, text="Select Your Identity ", font="comicsansms 13 bold", padding='10')
    lbl.pack()

    b2=tkinter.Button(text="Teacher",command=teacher)
    b3=tkinter.Button(text="Student",command=credential)
    b1=tkinter.Button(text="Check Result",command=res)
    b2.pack()
    b3.pack()
    b1.pack()

    root.mainloop()

showmain()