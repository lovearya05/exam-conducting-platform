from tkinter import *
import mysql.connector as ct
mydb = ct.connect(host="localhost", user="root", passwd="8900",database="hello")

global rno
rno = 0

def result():

    root = Tk()
    root.title('Exam Window ')
    
    root.geometry("500x400")

    
    def showresult():

        def button():
            global rno
            rno = box.get()
            # pass
            l1.destroy()
            bt1.destroy()
            box.destroy()

            # print(rno)
            mycursor = mydb.cursor()
            mycursor.execute(f'''select * from student where rno={rno}''')
            j = mycursor.fetchone()
            # print(j)

            # for i in mycursor:
                # print(i)
            a1 = Label(root, text="Name ... ", font="comicsansms 10 bold")
            a2 = Label(root, text="Roll-No ... ", font="comicsansms 10 bold")
            a3 = Label(root, text="Department... ", font="comicsansms 10 bold")
            a4 = Label(root, text="Marks ... ", font="comicsansms 10 bold")
            a1.place(x=100,y=100)
            a2.place(x=100,y=140)
            a3.place(x=100,y=180) # use Grid here
            a4.place(x=100,y=220)
            
            b1 = Label(root, text=f"{j[0]}", font="comicsansms 10 bold")
            b2 = Label(root, text=f"{j[1]}", font="comicsansms 10 bold")
            b3 = Label(root, text=f"{j[2]}", font="comicsansms 10 bold")
            b4 = Label(root, text=f"{j[3]}", font="comicsansms 10 bold")
            b1.place(x=220,y=100)
            b2.place(x=220,y=140)#   use grid here
            b3.place(x=220,y=180)
            b4.place(x=220,y=220)



        ab = Label(root,text="\n\n\n\n\n\n\n")
        ab.grid(row=1, column=1)
        ab1 = Label(root,text="\t\t\t")
        ab1.grid(row=2, column=1)
        l1 = Label(root, text="Enter roll Number to check Result ", font="comicsansms 10 bold")
        l1.place(x=100,y=80)
        # l1.pack()
        rn = IntVar()
        box = Entry(root, textvariable=rn)
        box.grid(row=2, column=2)

        #Button & packing it and assigning it a command
        bt1=Button(root,text="Check ",command=button)
        bt1.grid(row=2, column=4)
    
    
    showresult()
     
    
    root.mainloop()



# result()