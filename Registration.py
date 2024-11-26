import sys
import os
import tkinter as tk
from tkinter import *

def Admin():
	os.system('python AdminReg.py')

def Consumer():
	os.system('python ConsumerReg.py')

root = tk.Tk()
w=1100
h=600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("New Registration")
root.config(bg='lightblue')

hlab1 = tk.Label(root, text ='NEW REGISTRATION' )
hlab1.place(x = 45, y = 30) 
hlab1.config(bg='lightblue',fg='blue',font=('Bookman Old Style', 40))

b1 = tk.Button(root, text='Admin', bg='blue', fg='lightblue',command=Admin)
b1.place(x=220, y=250, width=200, height=200)
b1.config(font=('Helvetica bold', 20))

b2 = tk.Button(root, text='Consumer', bg='blue', fg='lightblue',command=Consumer)
b2.place(x=440, y=250, width=200, height=200)
b2.config(font=('Helvetica bold', 20))

b3 = tk.Button(root, text='Back', bg='blue', fg='lightblue',command='exit')
b3.place(x=660, y=250, width=200, height=200)
b3.config(font=('Helvetica bold', 20))
root.mainloop()