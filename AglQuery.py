import sys
import os
import tkinter as tk
from tkinter import *

def AgriLoan():
	os.system("python Yearvsamt.py")

def DistLoan():
	os.system("python Distvsamt.py")	

def TypeLoan():
	os.system("python Typevsamt.py")	

def AglRep():
	os.system("python AglRep.py")

root = tk.Tk()
w=650
h=400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Agri - Query Process")
root.config(bg='lightblue')

hlab1 = tk.Label(root, text ='AGRI LOAN QUERY PROCESS' )
hlab1.place(x = 45, y = 20) 
hlab1.config(bg='lightblue',fg='blue',font=('Bookman Old Style',25,'bold'))

b1 = tk.Button(root, text='Year vs Amount', bg='blue', fg='lightblue',command=AgriLoan)
b1.place(x=10, y=100, width=210, height=125)
b1.config(font=('Helvetica bold', 16))

b2 = tk.Button(root, text='District vs Amount', bg='blue', fg='lightblue',command=DistLoan)
b2.place(x=220, y=125, width=210, height=125)
b2.config(font=('Helvetica bold', 16))

b3 = tk.Button(root, text='Loan Type vs Amount', bg='blue', fg='lightblue',command=TypeLoan)
b3.place(x=430, y=145, width=210, height=125)
b3.config(font=('Helvetica bold', 16))

b4 = tk.Button(root, text='Overall Entity', bg='blue', fg='lightblue',command=AglRep)
b4.place(x=225, y=300, width=210, height=75)
b4.config(font=('Helvetica bold', 16))

root.bind("<Escape>", 'exit')

root.mainloop()