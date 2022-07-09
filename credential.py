from tkinter import *
from ExamWindow import *

import mysql.connector as ct
mydb = ct.connect(host="localhost", user="root", passwd="8900",database="hello")
mycursor = mydb.cursor()

global rno
rno = 0


def credentialInput():

    def attempt():
        global rno
        rno = B.get()
        # rno = rn.get()
        mycursor.execute(f'''insert into student values("{A.get()}","{rno}","{C.get()}",0);''')
        mydb.commit()
        # print(f"{rno}")
        clear()
        # mycursor.execute
        # exam(B.get())

        exam(rno)

        # pass
    
    def clear():
        A.delete(0, END)
        B.delete(0, END)
        C.delete(0, END)

    root = Tk()


    Framee = Frame(root)

    Framee.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    Framee.configure(relief=GROOVE)
    Framee.configure(borderwidth="2")
    Framee.configure(border="2")
    Framee.configure(relief=GROOVE)
    Framee.configure(background="#d9d9d9")
    Framee.configure(highlightbackground="#d9d9d9")
    Framee.configure(highlightcolor="black")
    Framee.configure(width=925)


    root.title('Student Details')
    root.geometry("644x344")    


    #Text for our form
    ee = Label(root, text="Enter Credentials", font="comicsansms 13 bold underline", pady=0, justify = CENTER, background="#d9d9d9")
    name = Label(root, text=" NAME                      :", pady=20, justify = CENTER,  background="#d9d9d9")
    rollno = Label(root, text=" ROLL NO                 :", pady=20, justify = CENTER,  background="#d9d9d9")
    dept = Label(root, text=" DEPARTMENT          :", pady=20, justify = CENTER,  background="#d9d9d9")
    #ansOp = Label(root, text="Choose the correct option like(A, B, C)")    

    #Pack text for our form
    ee.grid(row=2, columnspan=3)
    ee.place(relx=0.04, rely=0.037, height=50, width=150)
    name.grid(row=3, column=3)
    name.place(relx=0.3, rely=0.1, height=50, width=150)
    rollno.grid(row=4, column=3)
    rollno.place(relx=0.3, rely=0.2, height=50, width=150)
    dept.grid(row=5, column=3)
    dept.place(relx=0.3, rely=0.3, height=50, width=150)    

    # Tkinter variable for storing entries
    #question = StringVar()
    name = StringVar()
    rn = IntVar()
    dept = StringVar()  

    #Entries for our form
    #nameentry = Entry(root, textvariable=question)
    A = Entry(root, textvariable=name, justify="center",)
    # global rn
    # rn = 0
    B = Entry(root, textvariable=rn)
    C = Entry(root, textvariable=dept)  
    bb = Button(root,text="SUBMIT & ATTEMPT TEST",command=attempt)


    # Packing the Entries
    A.grid(row=3, column=5)
    A.place(relx=0.6, rely=0.15, height=20, width=100)
    B.grid(row=4, column=5)
    B.place(relx=0.6, rely=0.25, height=20, width=100)
    C.grid(row=5, column=5)
    C.place(relx=0.6, rely=0.35, height=20, width=100)  


    bb.grid( row = 33, column= 5 )
    bb.place(relx=0.40, rely=0.65, height=50, width=150)    
    #Button & packing it and assigning it a command

    root.mainloop()


# credentialInput()