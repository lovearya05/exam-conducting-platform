from tkinter import *
import mysql.connector as ct


mydb = ct.connect(host="localhost", user="root", passwd="8900",database="hello")
mycursor = mydb.cursor()

def myconnect():
    mydb = ct.connect(host="localhost", user="root", passwd="8900",database="hello")
    return mydb


def createtable():
    mycursor = mydb.cursor()
    # pass
    mycursor.execute(f"DELETE FROM test;")
    mydb.commit()

def input():
    # input.count=2
    mycursor = mydb.cursor()
    def delete(): 
        mycursor.execute(f'''insert into test values(null,"{nameentry.get()}","{A.get()}","{B.get()}","{C.get()}","{D.get()}","{answer.get()}");''')
        print("myques:",nameentry.get())
        print("Question added sucessfull ")
        mydb.commit()
        clear()

    def clear():
        A.delete(0, END)
        B.delete(0, END)
        C.delete(0, END)
        D.delete(0, END)
        answer.delete(0, END)
        nameentry.delete(0, END)


    root = Tk()
    frame = Frame(root)
    
    root.geometry("644x344")

    root.title('Create a Quiz')

    # Q = Label(frame, text=f"Q{input.count}")
    Q = Label(frame, text=f"Q")
    que = Label(root, text="Enter Question", font="comicsansms 13 bold", pady=30)
    opA = Label(root, text="Option A")
    opB = Label(root, text="Option B")
    opC = Label(root, text="Option C")
    opD = Label(root, text="Option D")
    ansOp = Label(root, text="Choose the correct option like(A, B, C, D)")

    #Pack text for our form
    frame.grid(row=1, column=1)
    Q.grid(row=1, column=1)
    que.grid(row=1, column=2)
    opA.grid(row=2, column=2)
    opB.grid(row=3, column=2)
    opC.grid(row=4, column=2)
    opD.grid(row=5, column=2)
    ansOp.grid(row=3, column=7)

    # Tkinter variable for storing entries
    question = StringVar()
    optionA = StringVar()
    optionB = StringVar()
    optionC = StringVar()
    optionD = StringVar()
    ans = StringVar()


    #Entries for our form
    nameentry = Entry(root, textvariable=question)
    A = Entry(root, textvariable=optionA)
    B = Entry(root, textvariable=optionB)
    C = Entry(root, textvariable=optionC)
    D = Entry(root, textvariable=optionD)
    answer = Entry(root, textvariable=ans)

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    A.grid(row=2, column=3)
    B.grid(row=3, column=3)
    C.grid(row=4, column=3)
    D.grid(row=5, column=3)
    answer.grid(row=4, column=7)


    #Button & packing it and assigning it a command
    Button(root, text="Save Enter new Question", command=delete).grid(row=9, column=7)
    # Button(root, text="Quit", command=frame.quit).grid(row=9, column=8)
    
    root.mainloop()



# drop()
# createtable()
# input()


