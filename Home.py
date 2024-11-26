import sys
import os
import tkinter as tk
from tkinter import *

def next():
	os.system('python AdminControl.py')

root=tk.Tk()
w=1100
h=600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x=(screen_width/2) - (w/2)
y=(screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Home Page")
root.config(bg='black')

hlab1 = tk.Label(root, text ='Application of ' )
hlab1.place(x=40,y=30) 
hlab1.config(bg='black',fg='gold',font=('Bookman Old Style',48,'bold'))

hlab2 = tk.Label(root, text ='Digital Technologies for ' )
hlab2.place(x=100,y=130) 
hlab2.config(bg='black',fg='gold',font=('Bookman Old Style',40,'bold'))

hlab3 = tk.Label(root, text ='Ensuring Agricultural Productivity' )
hlab3.place(x=160,y=230) 
hlab3.config(bg='black',fg='gold',font=('Bookman Old Style',30,'bold'))

hlab4 = tk.Label(root, text ="Machine Learning Principle" )
hlab4.place(x = 500, y = 430) 
hlab4.config(bg='black',fg='gold',font=('Bookman Old Style', 30))

b1 = tk.Button(root, text ='Next', bg ='black', fg='gold',command=next)
b1.place(x = 500, y = 550, width = 80)
b1.config(font=('Helvetica bold', 13))

root.bind("<Escape>", 'exit')

root.mainloop()