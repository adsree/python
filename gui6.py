from tkinter import *
master = Tk()


label1=Label.grid(sticky=E)
label2=Label.grid(sticky=E) 

e1=Entry.grid(row=0, column=1)
e2=Entry.grid(row=1, column=1)

Checkbutton.grid(columnspan=2,sticky=W)

Image.grid(row=0,column=2,columnspan=2,rowspan=2,sticky=W+E+N+S, padx=5, pady=5)


Button.grid(row=2, column=2)
Button.grid(row=2, column=3)

mainloop()