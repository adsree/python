from tkinter import *
w=Tk()
l1=Label(text="UserName")
l1.grid(row=0, column=0)
e1=Entry()
e1.grid(row=0, column=1)
l2=Label(text="Password")
l2.grid(row=1, column=0)
e2=Entry()
e2.grid(row=1, column=1)

l3=Button(text="Register")
l3.grid(row=2,column=1)
w.mainloop()