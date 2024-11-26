import sys
import os
import tkinter as tk
from tkinter import *

def AgArSlTy():
	os.system("python AgArSlTy.py")

def SrArSlTy():
	os.system("python SrArSlTy.py")	

def SolRep():
	os.system("python SolRep.py")

root = tk.Tk()
w=550
h=300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Seed/Plant - Query Process")
root.config(bg='lightblue')

hlab1 = tk.Label(root, text ='SOIL QUERY PROCESS' )
hlab1.place(x = 75, y = 20) 
hlab1.config(bg='lightblue',fg='blue',font=('Bookman Old Style',25,'bold'))

b1 = tk.Button(root, text='Agri-Area vs Soil-Type', bg='blue', fg='lightblue',command=AgArSlTy)
b1.place(x=50, y=100, width=225, height=100)
b1.config(font=('Helvetica bold', 16))

b2 = tk.Button(root, text='Yield vs Soil-Type', bg='blue', fg='lightblue',command=SrArSlTy)
b2.place(x=275, y=100, width=225, height=100)
b2.config(font=('Helvetica bold', 16))

b3 = tk.Button(root, text='Overall Entity', bg='blue', fg='lightblue',command=SolRep)
b3.place(x=170, y=200, width=210, height=75)
b3.config(font=('Helvetica bold', 16))

root.bind("<Escape>", 'exit')

root.mainloop()