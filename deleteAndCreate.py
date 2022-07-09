from tkinter import *
from enterQue import *




def deleteAndCrt():
    def enterval():
        createtable()
        input()

    root = Tk()
    root.geometry("644x344")
    root.title('delete and create ')
    #Text for our form
    que = Label(root, text="delete and create new test ", font="comicsansms 13 bold", pady=30)
    #Pack text for our form
    que.grid(row=1, column=2)
    #Button & packing it and assigning it a command
    Button(root,text="-->",width=10,height=2,command=enterval).grid(row=9, column=7)
    
    root.mainloop()


# deleteAndCreate()