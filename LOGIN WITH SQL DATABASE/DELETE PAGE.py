from tkinter import *
from tkinter import messagebox
import sqlite3

t = Tk()
t.geometry("600x400")
t.configure(background="#091e42")
a = StringVar()



def show():
    db = sqlite3.connect('adi.db')
    cr = db.cursor()
    cr.execute("delete from registration where USERNAME='" + a.get() + "'")
    messagebox.showinfo("Delete", "Data delete")
    db.commit()
    db.close()
    a.set("")


u = Label(text="Delete Page", fg="white", font=("Century", 15), bg="#091e42")
u.place(x=200, y=20)

u1 = Label(text="Enter Username", font=("Century", 15), bg="#091e42", fg="white")
u1.place(x=70, y=80)
e1 = Entry(font=("", 15), width=15, textvariable=a)
e1.place(x=270, y=85)


b3 = Button(text="LogIn", font=("Century", 15), fg='white', command=show, bg="red")
b3.place(x=225, y=140, width=80, height=40)

t.mainloop()
