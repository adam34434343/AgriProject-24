import tkinter as tk
from tkinter import *
import mysql.connector
import sys
import os

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor = mydb.cursor()

def Clear():
	t1.delete("0","end")
	t2.delete("0","end")
	t3.delete("0","end")
def Check():
	d1=t1.get()
	d2=t2.get()
	d3=t3.get()
	val=(d1,d2,d3)
	sql="select *from consumer where uid=%s and psw=%s and mid=%s"
	mycursor.execute(sql,val)
	resultset=mycursor.fetchall()
	for x in resultset:
		s3=x[5]
		s1=x[10]
		s2=x[11]
		if d1==s1 and d2==s2 and d3==s3:
			os.system("python QueryProcess.py")
		else:
			print("invalid")
root = tk.Tk()
w=600
h=600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Consumer Login")
root.config(bg='lightblue')

hlab = tk.Label(root, text ="CONSUMER LOGIN", )
hlab.place(x = 135, y = 10) 
hlab.config(fg='blue',bg='lightblue',font=('Helvetica bold', 30))

l1 = tk.Label(root, text ="Login - Id" )
l1.place(x = 180, y = 130)
l1.config(fg='red', bg='lightblue',font=('Arial', 16))
 
t1 = tk.Entry(root, width = 35)
t1.place(x = 180, y = 180, width = 200)
  
l2 = tk.Label(root, text ="Password")
l2.place(x = 180, y = 230)
l2.config(fg='red',bg='lightblue',font=('Arial', 16))
 
t2 = tk.Entry(root, width = 35)
t2.place(x = 180, y = 280, width = 200)

l3 = tk.Label(root, text ="Mail-Id")
l3.place(x = 180, y = 330)
l3.config(fg='red',bg='lightblue',font=('Arial', 16))
 
t3 = tk.Entry(root, width = 35)
t3.place(x = 180, y = 380, width = 200)

b1 = tk.Button(root, text ="Clear", bg ='grey',command=Clear)
b1.place(x = 180, y = 460, width = 80)
b1.config(font=('Helvetica bold', 13))

b2 = tk.Button(root, text ="Login", bg ='grey',command=Check)
b2.place(x = 270, y = 460, width = 80)
b2.config(font=('Helvetica bold', 13))

b3 = tk.Button(root, text ="Quit", bg ='grey',command='exit')
b3.place(x = 360, y = 460, width = 80)
b3.config(font=('Helvetica bold', 13))

root.mainloop()