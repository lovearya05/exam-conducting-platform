import mysql.connector as ct

# setup file to create table used in various interfaces..

db = ct.connect(host="localhost", user="root", passwd="8900")
mcursor = db.cursor()

mcursor.execute("create database hello;")
db.commit()


mydb = ct.connect(host="localhost", user="root", passwd="8900", database="hello")
mycursor = mydb.cursor()
# mycursor.execute("drop table test;")


mycursor.execute(f"create table test (queno int primary key AUTO_INCREMENT, question varchar(300), \
optionA varchar(100), optionB varchar(100), optionC varchar(100), \
optionD varchar(100), ans varchar(10) );")

mydb.commit()

mycursor.execute(f'''insert into test values(null,"what is your name","Astha","Lovepreet","Ritika","Hardik","Gurpreet");''')

mydb.commit()

mycursor.execute("create table student(name varchar(20), rno int(10), department varchar(20), marks int(5));")

mydb.commit()

mycursor.execute('''insert into student values("ankit",1,"mca",99);''')


mydb.commit()

mycursor.execute("select * from student")
# mycursor.execute("describe table student;")
for i in mycursor:
    print(i)
# mycursor.execute("drop table student;")
# mydb.commit()
# mycursor.execute("drop table test;")
# mydb.commit()

mycursor.execute("select * from test")
for i in mycursor:
    print(i)



