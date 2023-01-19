from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

t = Tk()
t.geometry("600x400")
t.resizable(0, 0)

# There is a problem that in showall page we cant see the inserted value to be updated Then we code the following
f55 = None


#         **************************************************  LOGIN **********************************************

def login():
    # second Frame

    f2 = Frame(bg="#091e42")
    f2.place(x=0, y=0, width=600, height=400)

    a = StringVar()
    b = StringVar()

    # Label and their Entry
    u1 = Label(f2, text="Enter Name", font=("Century", 11), bg="#091e42", fg="white")
    u1.place(x=200, y=50)
    e1 = Entry(f2, font=("Century", 14), textvariable=a)
    e1.place(x=325, y=50, width=130)

    u2 = Label(f2, text="Enter PassWord", font=("Century", 11), bg="#091e42", fg="white")
    u2.place(x=200, y=100)
    e2 = Entry(f2, font=("Century", 14), show="*", textvariable=b)
    e2.place(x=325, y=100, width=130)

    def login1():
        if ((a.get() == '' or b.get() == '')):

            messagebox.showinfo("Incorrect", "please enter your data")
            a.set("")
            b.set("")

        else:
            db = sqlite3.connect("adi.db")
            cr = db.cursor()
            r = cr.execute(
                "select * from registration where USERNAME='" + a.get() + "' AND USER_PASSWORD='" + b.get() + "'   ")
            for r1 in r:
                mymenu()
                # messagebox.showinfo("success", "Welcome")
                break
            else:
                messagebox.showinfo("Incorrect", "invalid username and password")

            db.commit()
            db.close()
            # message alert

            # To set the Values empty
            a.set("")
            b.set("")

    # Buttons
    b1 = Button(f2, text="LogIn", bg="#091e42", fg="red", font=("Century", 15), command=login1)
    b1.place(x=260, y=160, width=100, height=40)

    b2 = Button(f2, text="Home", bg="#091e42", fg="red", font=("Century", 15), command=home)
    b2.place(x=5, y=360, width=100, height=40)

    b3 = Button(f2, text="RegIs", bg="#091e42", fg="red", font=("Century", 15), command=regis)
    b3.place(x=495, y=360, width=100, height=40)


#         **************************************************  LOGIN END **********************************************


#         **************************************************  REGISTRATION **********************************************


def regis():
    # third Frame
    f3 = Frame(bg="#091e42")
    f3.place(x=0, y=0, width=600, height=400)

    r1 = StringVar()
    r2 = StringVar()
    r3 = StringVar()

    u1 = Label(f3, text="Enter Name", font=("Century", 11), bg="#091e42", fg="white")
    u1.place(x=150, y=50)
    e1 = Entry(f3, font=("Century", 14), textvariable=r1)
    e1.place(x=350, y=50, width=130)

    u2 = Label(f3, text="Enter Password", font=("Century", 11), bg="#091e42", fg="white")
    u2.place(x=150, y=100)
    e2 = Entry(f3, font=("Century", 14), show="*", textvariable=r2)
    e2.place(x=350, y=100, width=130)

    u3 = Label(f3, text="Enter Contact Number", font=("Century", 11), bg="#091e42", fg="white")
    u3.place(x=150, y=150)
    e3 = Entry(f3, font=("Century", 14), textvariable=r3)
    e3.place(x=350, y=150, width=130)

    def regis1():
        if ((r1.get() == '' or r2.get() == '' or r3.get() == '')):

            messagebox.showinfo("Incorrect", "please enter your data")
            r1.set("")
            r2.set("")
            r3.set("")
        else:
            db = sqlite3.connect("adi.db")
            cr = db.cursor()

            cr.execute("insert into registration values('" + r1.get() + "','" + r2.get() + "','" + r3.get() + "')")
            db.commit()
            db.close()
            # message alert

            messagebox.showinfo("success", "You are successfully registered")

            # To set the Values empty
            r1.set("")
            r2.set("")
            r3.set("")

    b1 = Button(f3, text="Registered", bg="#091e42", fg="red", font=("Century", 15), command=regis1)
    b1.place(x=260, y=200, width=110, height=40)

    b2 = Button(f3, text="Home", bg="#091e42", fg="red", font=("Century", 15), command=home)
    b2.place(x=5, y=360, width=100, height=40)

    b3 = Button(f3, text="Login", bg="#091e42", fg="red", font=("Century", 15), command=login)
    b3.place(x=495, y=360, width=100, height=40)


#         **************************************************END REGISTRATION **********************************************


#         ******************************************************   MENU  **********************************************
def mymenu():
    n = ttk.Notebook()
    n.place(x=0, y=0, width=600, height=400)

    def demo(a):
        if (n.index("current") == 5):
            messagebox.showinfo("LOGOUT", "logout")
            home()

    n.bind("<<NotebookTabChanged>>", demo)
    insertdata(n)
    showall(n)
    searchdata(n)
    updatedata(n)
    deletedata(n)
    logout(n)


def insertdata(n):
    f4 = Frame(bg="#091e42")
    n.add(f4, text="Insert")
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()

    # Label and their Entry
    u1 = Label(f4, text="ENTER RollNO", font=("Century", 11), bg="#091e42", fg="white")
    u1.place(x=120, y=50)
    e1 = Entry(f4, font=("Century", 14), textvariable=s1)
    e1.place(x=325, y=50, width=130)

    u2 = Label(f4, text="ENTER NAME", font=("Century", 11), bg="#091e42", fg="white")
    u2.place(x=120, y=100)
    e2 = Entry(f4, font=("Century", 14), textvariable=s2)
    e2.place(x=325, y=100, width=130)

    u3 = Label(f4, text="ENTER PHYSICS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u3.place(x=120, y=150)
    e3 = Entry(f4, font=("Century", 14), textvariable=s3)
    e3.place(x=325, y=150, width=130)

    u4 = Label(f4, text="ENTER CHEMIS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u4.place(x=120, y=200)
    e4 = Entry(f4, font=("Century", 14), textvariable=s4)
    e4.place(x=325, y=200, width=130)

    u5 = Label(f4, text="ENTER MATHS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u5.place(x=120, y=250)
    e5 = Entry(f4, font=("Century", 14), textvariable=s5)
    e5.place(x=325, y=250, width=130)

    def insertdemo1():
        if ((s1.get() == '' or s2.get() == '' or s3.get() == '' or s4.get() == '' or s5.get() == '')):

            messagebox.showinfo("Incorrect", "please enter your data")

            s2.set("")
            s3.set("")
            s4.set("")
            s5.set("")

        else:
            db = sqlite3.connect("adi.db")
            cr = db.cursor()

            cr.execute(
                "insert into ins values('" + s1.get() + "','" + s2.get() + "','" + s3.get() + "','" + s4.get() + "','" + s5.get() + "')")
            db.commit()
            db.close()
            # message alert

            messagebox.showinfo("success", "You are successfully inserted")

            # To set the Values empty
            s1.set("")
            s2.set("")
            s3.set("")
            s4.set("")
            s5.set("")

            showalldata1(f55)

    # show all data1 takes one argument then we crweate f55 to none and in showall function we assign

    b1 = Button(f4, text="INSERT", bg="#091e42", fg="red", font=("Century", 15), command=insertdemo1)
    b1.place(x=260, y=300, width=100, height=40)


def showall(n):
    f5 = Frame(bg="#091e42")
    n.add(f5, text="ShowAll")

    global f55
    f55 = f5
    showalldata1(f5)


def showalldata1(f5):
    for w in f5.winfo_children():
        w.destroy()
    u1 = Label(f5, text="RollNO", font=("Century", 11), bg="#091e42", fg="white")
    u1.place(x=25, y=10)

    u2 = Label(f5, text="NAME", font=("Century", 11), bg="#091e42", fg="white")
    u2.place(x=100, y=10)

    u3 = Label(f5, text="PHYSICS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u3.place(x=180, y=10)

    u4 = Label(f5, text="CHEMIS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u4.place(x=325, y=10)

    u5 = Label(f5, text="MATHS_MARKS", font=("Century", 11), bg="#091e42", fg="white")
    u5.place(x=465, y=10)

    db = sqlite3.connect("adi.db")
    cr = db.cursor()
    r = cr.execute("select * from ins ")

    x = 0
    y = 50

    for r1 in r:
        Label(f5, text=r1[0], font=("Century", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 75

        Label(f5, text=r1[1], font=("Century", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 110

        Label(f5, text=r1[2], font=("Century", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 140

        Label(f5, text=r1[3], font=("Century", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        x += 140

        Label(f5, text=r1[4], font=("Century", 11), bg="#091e42", fg="white").place(x=x, y=y, width=120)
        y += 40
        x = 0
    db.commit()
    db.close()


def searchdata(n):
    f6 = Frame(bg="#091e42")
    n.add(f6, text="Search")

    s1 = StringVar()

    u1 = Label(f6, text="ENTER RoLLNO.", font=("Century", 12), bg="#091e42", fg="white")
    u1.place(x=120, y=50)
    e1 = Entry(f6, font=("Century", 11), textvariable=s1)
    e1.place(x=270, y=50)

    def searchdata1():
        db = sqlite3.connect("adi.db")
        cr = db.cursor()
        r = cr.execute("select * from ins where RollNo='" + s1.get() + "' ")
        for r1 in r:
            u1 = Label(f6, text="****DETAILS****", font=("Century", 11), bg="#091e42", fg="#ffcc00")
            u1.place(x=200, y=140)

            u9 = Label(f6, text="NAME", font=("Century", 11), bg="#091e42", fg="white")
            u9.place(x=170, y=170)

            u2 = Label(f6, text=r1[1], font=("Century", 11), bg="#091e42", fg="cyan")
            u2.place(x=320, y=170)

            u3 = Label(f6, text="PHY_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u3.place(x=170, y=200)

            u4 = Label(f6, text=r1[2], font=("Century", 11), bg="#091e42", fg="cyan")
            u4.place(x=320, y=200)

            u5 = Label(f6, text="CHE_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u5.place(x=170, y=230)

            u6 = Label(f6, text=r1[3], font=("Century", 11), bg="#091e42", fg="cyan")
            u6.place(x=320, y=230)
            u7 = Label(f6, text="MATH_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u7.place(x=170, y=260)

            u8 = Label(f6, text=r1[4], font=("Century", 11), bg="#091e42", fg="cyan")
            u8.place(x=320, y=260)
            break
        else:
            messagebox.showinfo("Title", "invaild Roll No")
            u1 = Label(f6, text="                                    ", font=("Century", 11), bg="#091e42",
                       fg="#ffcc00")
            u1.place(x=200, y=140)
            u10 = Label(f6, text="                                    ", font=("Century", 11), bg="#091e42", fg="white")
            u10.place(x=170, y=170)

            u11 = Label(f6, text="                                    ", font=("Century", 11), bg="#091e42", fg="cyan")
            u11.place(x=320, y=170)

            u13 = Label(f6, text="                                    ", font=("Century", 11), bg="#091e42", fg="white")
            u13.place(x=170, y=200)

            u14 = Label(f6, text="                                     ", font=("Century", 11), bg="#091e42", fg="cyan")
            u14.place(x=320, y=200)

            u15 = Label(f6, text="                                      ", font=("Century", 11), bg="#091e42",
                        fg="white")
            u15.place(x=170, y=230)

            u16 = Label(f6, text="                                     ", font=("Century", 11), bg="#091e42", fg="cyan")
            u16.place(x=320, y=230)
            u17 = Label(f6, text="                                     ", font=("Century", 11), bg="#091e42",
                        fg="white")
            u17.place(x=170, y=260)

            u18 = Label(f6, text="                                     ", font=("Century", 11), bg="#091e42", fg="cyan")
            u18.place(x=320, y=260)

        db.commit()
        db.close()

    b1 = Button(f6, text="Search", bg="#091e42", fg="red", font=("Century", 15), command=searchdata1)
    b1.place(x=220, y=90, width=100, height=40)


def updatedata(n):
    f7 = Frame(bg="#091e42")
    s1 = StringVar()
    n.add(f7, text="Update")

    u1 = Label(f7, text="RoLLNO.", font=("Century", 12), bg="#091e42", fg="white")
    u1.place(x=170, y=50)
    e1 = Entry(f7, font=("Century", 11), textvariable=s1)
    e1.place(x=250, y=50, width=130)

    def updatedata1():
        db = sqlite3.connect("adi.db")
        cr = db.cursor()
        r = cr.execute("select * from ins where RollNo='" + s1.get() + "' ")
        for r1 in r:
            s2 = StringVar()
            s3 = StringVar()
            s4 = StringVar()
            s5 = StringVar()

            u = Label(f7, text="****DETAILS****", font=("Century", 11), bg="#091e42", fg="#ffcc00")
            u.place(x=230, y=100)

            u1 = Label(f7, text="NAME", font=("Century", 11), bg="#091e42", fg="white")
            u1.place(x=170, y=140)

            e1 = Entry(f7, font=("Century", 11), bg="#091e42", fg="white", textvariable=s2)
            e1.insert(0, r1[1])
            e1.place(x=320, y=140)

            u2 = Label(f7, text="PHY_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u2.place(x=170, y=180)

            e2 = Entry(f7, font=("Century", 11), bg="#091e42", fg="white", textvariable=s3)
            e2.insert(0, r1[2])
            e2.place(x=320, y=180)

            u3 = Label(f7, text="CHE_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u3.place(x=170, y=220)

            e3 = Entry(f7, font=("Century", 11), bg="#091e42", fg="white", textvariable=s4)
            e3.insert(0, r1[3])
            e3.place(x=320, y=220)

            u5 = Label(f7, text="MATH_MARKS", font=("Century", 11), bg="#091e42", fg="white")
            u5.place(x=170, y=260)
            e5 = Entry(f7, font=("Century", 11), bg="#091e42", fg="white", textvariable=s5)
            e5.insert(0, r1[4])
            e5.place(x=320, y=260)

            def updatedata2():
                if ((s2.get() == '' or s3.get() == '' or s4.get() == '' or s5.get() == '')):

                    messagebox.showinfo("Incorrect", "please enter your data")

                    s2.set("")
                    s3.set("")
                    s4.set("")
                    s5.set("")

                else:
                    db = sqlite3.connect("adi.db")
                    cr = db.cursor()

                    cr.execute(
                        "update ins set NAME='" + s2.get() + "',PHY_Marks='" + s3.get() + "',CHE_Marks='" + s4.get() + "',Maths_Marks ='" + s5.get() + "' where RollNo='" + s1.get() + "' ")
                    db.commit()
                    db.close()
                    # message alert
                    showalldata1(f55)

                    messagebox.showinfo("success", "You are successfully update")

                    # To set the Values empty

                    s2.set("")
                    s3.set("")
                    s4.set("")
                    s5.set("")

            b78 = Button(f7, text="UPDATE", bg="#091e42", fg="red", font=("Century", 12), command=updatedata2)
            b78.place(x=270, y=310, width=80)
            break

        else:
            messagebox.showinfo("Title", "invaild Roll No")

        db.commit()
        db.close()

    b1 = Button(f7, text="Search", bg="#091e42", fg="red", font=("Century", 12), command=updatedata1)
    b1.place(x=400, y=45, width=100)


def deletedata(n):
    f8 = Frame(bg="#091e42")
    n.add(f8, text="Delete")
    s1 = StringVar()

    u1 = Label(f8, text="RoLLNO.", font=("Century", 12), bg="#091e42", fg="white")

    u1 = Label(f8, text="RoLLNO.", font=("Century", 12), bg="#091e42", fg="white")
    u1.place(x=170, y=50)
    e1 = Entry(f8, font=("Century", 11), textvariable=s1)
    e1.place(x=250, y=50, width=130)

    def deletedata1():
        if ((s1.get() == '')):

            messagebox.showinfo("Incorrect", "please enter your data")

            s1.set("")


        else:
            db = sqlite3.connect("adi.db")
            cr = db.cursor()

            cr.execute(" delete from ins where RollNo='" + s1.get() + "' ")
            db.commit()
            db.close()
            # message alert
            showalldata1(f55)

            messagebox.showinfo("success", "Your data is successfully delete")

            # To set the Values empty

            s1.set("")

    b1 = Button(f8, text="Delete", bg="#091e42", fg="red", font=("Century", 12), command=deletedata1)
    b1.place(x=400, y=45, width=100)


def logout(n):
    f9 = Frame(bg="#091e42")
    n.add(f9, text="LOGOUT")


#         **********************************************************  MENU END **********************************************


def home():
    f1 = Frame(background="#091e42")
    f1.place(x=0, y=0, width=600, height=400)

    u = Label(f1, text="Welcome To DataBase", font=("Century", 20), bg="#091e42", fg="white")
    u.place(x=160, y=20)

    b1 = Button(f1, text="LogIn", command=login, bg="#091e42", fg="red", font=("Century", 15))
    b1.place(x=220, y=100, width=80, height=40)

    b2 = Button(f1, text="RegIs", command=regis, bg="#091e42", fg="red", font=("Century", 15))
    b2.place(x=310, y=100, width=80, height=40)


#         ***********************************************************  calling Home  ++***********************************
home()

t.mainloop()
