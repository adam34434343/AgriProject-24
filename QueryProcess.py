import sys
import os
import tkinter as tk
from tkinter import *

def AgriLoan():
	os.system("python AglQuery.py")
def Fertilizer():
	os.system("python FerQuery.py")
def Plantation():
	os.system("python SedQuery.py")
def SoilData():
	os.system("python SolQuery.py")
def Rainfall():
	os.system("python RanQuery.py")
root = tk.Tk()
w=1100
h=600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Query Process")
root.config(bg='lightblue')

hlab1 = tk.Label(root, text ='QUERY PROCESS CENTER' )
hlab1.place(x = 45, y = 30) 
hlab1.config(bg='lightblue',fg='blue',font=('Bookman Old Style',40,'bold'))

b1 = tk.Button(root, text='Agri Loan', bg='blue', fg='lightblue',command=AgriLoan)
b1.place(x=45, y=230, width=200, height=150)
b1.config(font=('Helvetica bold', 16))

b2 = tk.Button(root, text='Fertilizer', bg='blue', fg='lightblue',command=Fertilizer)
b2.place(x=247, y=230, width=200, height=150)
b2.config(font=('Helvetica bold', 16))

b3 = tk.Button(root, text='Plantation&Seeds', bg='blue', fg='lightblue',command=Plantation)
b3.place(x=449, y=230, width=200, height=150)
b3.config(font=('Helvetica bold', 16))

b4 = tk.Button(root, text='Soil Data', bg='blue', fg='lightblue',command=SoilData)
b4.place(x=651, y=230, width=200, height=150)
b4.config(font=('Helvetica bold', 16))

b5 = tk.Button(root, text='Rain Fall', bg='blue', fg='lightblue',command=Rainfall)
b5.place(x=853, y=230, width=200, height=150)
b5.config(font=('Helvetica bold', 16))

b6 = tk.Button(root, text='Exit', bg='blue', fg='lightblue',command='exit')
b6.place(x=449, y=400, width=200, height=150)
b6.config(font=('Helvetica bold', 16))

root.mainloop()