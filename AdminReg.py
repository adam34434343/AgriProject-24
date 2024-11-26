import tkinter as tk
import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor = mydb.cursor()

def Clear():
	t1.delete("0","end")
	t2.delete("0","end")
	t3.delete("0","end")
	t4.delete("0","end")
	t5.delete("0","end")
	t6.delete("0","end")
	t7.delete("0","end")
	t8.delete("0","end")

def Insert():
	d1=int(t1.get())
	d2=t2.get()
	d3= t3.get()
	d4=t4.get()
	d5=t5.get()
	d6=t6.get()
	d7= t7.get()
	d8=t8.get()
	val=(d1,d2,d3,d4,d5,d6,d7,d8)
	sql="insert into adminreg values(%s,%s,%s,%s,%s,%s,%s,%s)"
	mycursor.execute(sql,val)
	mydb.commit()
def View():
	d1=int(t1.get())
	val=(d1,)
	sql="select *from adminreg where aid=%s"
	mycursor.execute(sql,val)	
	myresult = mycursor.fetchall()
	for x in myresult:
		t2.insert(0,x[1])
		t3.insert(0,x[2])
		t4.insert(0,x[3])
		t5.insert(0,x[4])
		t6.insert(0,x[5])
		t7.insert(0,x[6])
		t8.insert(0,x[7])

def Update():
	d1=int(t1.get())
	d2=t2.get()
	d3=t3.get()
	d4=t4.get()
	d5=t5.get()
	d6=t6.get()
	d7=t7.get()
	d8=t8.get()
	val=(d2,d3,d4,d5,d6,d7,d8,d1)
	sql=("update adminreg set ana=%s,dep=%s,deg=%s,mob=%s,mid=%s,lid=%s,psw=%s where aid=%s")
	mycursor.execute(sql,val)
	mydb.commit()
def Delete():
	d1=int(t1.get())
	val=(d1,)
	sql="delete from adminreg where aid=%s"
	mycursor.execute(sql,val)
	mydb.commit()
def Close():
	root.destroy()
 
root=tk.Tk()
w=400
h=600
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2) - (w/2)
y=(screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Admin Registration')
root.config(bg='lightblue')

hlab = tk.Label(root, text ="ADMIN REGISTRATION", )
hlab.place(x = 50, y = 30) 
hlab.config(bg='lightblue',font=('Helvetica bold', 20))
 
l1 = tk.Label(root, text ="Admin - Id" )
l1.place(x = 30, y = 100)
l1.config(bg='lightblue',font=('Helvetica bold', 13))
 
t1 = tk.Entry(root, width = 35)
t1.place(x = 150, y = 100, width = 200)
  
l2 = tk.Label(root, text ="Name")
l2.place(x = 30, y = 150)
l2.config(bg='lightblue',font=('Helvetica bold', 13))
 
t2 = tk.Entry(root, width = 35)
t2.place(x = 150, y = 150, width = 200)
 
l3 = tk.Label(root, text ="Department")
l3.place(x = 30, y = 200)
l3.config(bg='lightblue',font=('Helvetica bold', 13))
 
t3 = tk.Entry(root, width = 35)
t3.place(x = 150, y = 200, width = 200)
  
l4 = tk.Label(root, text ="Designation")
l4.place(x = 30, y = 250)
l4.config(bg='lightblue',font=('Helvetica bold', 13))
 
t4 = tk.Entry(root, width = 35)
t4.place(x = 150, y = 250, width = 200)

l5 = tk.Label(root, text ="Mobile No")
l5.place(x = 30, y = 300)
l5.config(bg='lightblue',font=('Helvetica bold', 13))
 
t5 = tk.Entry(root, width = 35)
t5.place(x = 150, y = 300, width = 200) 

l6 = tk.Label(root, text ="Mail - Id")
l6.place(x = 30, y = 350)
l6.config(bg='lightblue',font=('Helvetica bold', 13))
 
t6 = tk.Entry(root, width = 35)
t6.place(x = 150, y = 350, width = 200) 

l7 = tk.Label(root, text ="Login-Id")
l7.place(x = 30, y = 400)
l7.config(bg='lightblue',font=('Helvetica bold', 13))
 
t7 = tk.Entry(root, width = 35)
t7.place(x = 150, y = 400, width = 200) 

l8 = tk.Label(root, text ="Password")
l8.place(x = 30, y = 450)
l8.config(bg='lightblue',font=('Helvetica bold', 13))
 
t8 = tk.Entry(root, width = 35)
t8.place(x = 150, y = 450, width = 200) 

b1 = tk.Button(root, text ="Clear", bg ='grey',command=Clear)
b1.place(x = 75, y = 500, width = 80)
b1.config(font=('Helvetica bold', 13))

b2 = tk.Button(root, text ="Commit", bg ='grey',command=Insert)
b2.place(x = 157, y = 500, width = 80)
b2.config(font=('Helvetica bold', 13))

b3 = tk.Button(root, text ="View", bg ='grey',command=View)
b3.place(x = 239, y = 500, width = 80)
b3.config(font=('Helvetica bold', 13))

b4 = tk.Button(root, text ="Update", bg ='grey',command=Update)
b4.place(x = 75, y = 550, width = 80)
b4.config(font=('Helvetica bold', 13))

b5 = tk.Button(root, text ="Delete", bg ='grey',command=Delete)
b5.place(x = 157, y = 550, width = 80)
b5.config(font=('Helvetica bold', 13))

b6 = tk.Button(root, text ="Exit", bg ='grey',command=Close)
b6.place(x = 239, y = 550, width = 80)
b6.config(font=('Helvetica bold', 13))

root.mainloop()