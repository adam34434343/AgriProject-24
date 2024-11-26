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
	t9.delete("0","end")
	t10.delete("0","end")
	t11.delete("0","end")
	t12.delete("0","end")

def Insert():
	d1=int(t1.get())
	d2=t2.get()
	d3= t3.get()
	d4=t4.get()
	d5=t5.get()
	d6=t6.get()
	d7= t7.get()
	d8=t8.get()
	d9= t9.get()
	d10=t10.get()
	d11= t11.get()
	d12=t12.get()
	val=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12)
	sql="insert into consumer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	mycursor.execute(sql,val)
	mydb.commit()
def View():
	d1=int(t1.get())
	val=(d1,)
	sql="select *from consumer where sid=%s"
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
		t9.insert(0,x[8])
		t10.insert(0,x[9])
		t11.insert(0,x[10])
		t12.insert(0,x[11])
def Update():
	d1=int(t1.get())
	d2=t2.get()
	d3=t3.get()
	d4=t4.get()
	d5=t5.get()
	d6=t6.get()
	d7=t7.get()
	d8=t8.get()
	d9=t9.get()
	d10=t10.get()
	d11=t11.get()
	d12=t12.get()
	val=(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d1)
	sql=("update consumer set dna=%s,fna=%s,plc=%s,mob=%s,mid=%s,dep=%s,brn=%s,yer=%s,acy=%s,uid=%s,psw=%s where sid=%s")
	mycursor.execute(sql,val)
	mydb.commit()
def Delete():
	d1=int(t1.get())
	val=(d1,)
	sql="delete from consumer where sid=%s"
	mycursor.execute(sql,val)
	mydb.commit()
def Close():
	root.destroy()
 
root = tk.Tk()
w=800
h=650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Students Registration')
root.config(bg='lightblue')

hlab = tk.Label(root, text ="CONSUMER REGISTRATION", )
hlab.place(x = 220, y = 10) 
hlab.config(bg='lightblue',font=('Helvetica bold', 20))

lab1 = tk.Label(root, text ="Personal Information", )
lab1.place(x = 30, y = 70) 
lab1.config(bg='lightblue',font=('Helvetica bold', 15))

l1 = tk.Label(root, text ="Consumer - Id" )
l1.place(x = 30, y = 130)
l1.config(bg='lightblue',font=('Helvetica bold', 13))
 
t1 = tk.Entry(root, width = 35)
t1.place(x = 180, y = 130, width = 200)
  
l2 = tk.Label(root, text ="Consumer Name")
l2.place(x = 400, y = 130)
l2.config(bg='lightblue',font=('Helvetica bold', 13))
 
t2 = tk.Entry(root, width = 35)
t2.place(x = 550, y = 130, width = 200)
 
l3 = tk.Label(root, text ="Address Field")
l3.place(x = 30, y = 190)
l3.config(bg='lightblue',font=('Helvetica bold', 13))
 
t3 = tk.Entry(root, width = 35)
t3.place(x = 180, y = 190, width = 200)
  
l4 = tk.Label(root, text ="Address Field 2")
l4.place(x = 400, y = 190)
l4.config(bg='lightblue',font=('Helvetica bold', 13))
 
t4 = tk.Entry(root, width = 35)
t4.place(x = 550, y = 190, width = 200)

l5 = tk.Label(root, text ="Mobile No")
l5.place(x = 30, y = 250)
l5.config(bg='lightblue',font=('Helvetica bold', 13))
 
t5 = tk.Entry(root, width = 35)
t5.place(x = 180, y = 250, width = 200)
  
l6 = tk.Label(root, text ="Mail - Id")
l6.place(x = 400, y = 250)
l6.config(bg='lightblue',font=('Helvetica bold', 13))
 
t6 = tk.Entry(root, width = 35)
t6.place(x = 550, y = 250, width = 200)

lab2 = tk.Label(root, text ="Academic Information", )
lab2.place(x = 30, y = 310) 
lab2.config(bg='lightblue',font=('Helvetica bold', 15))

l7 = tk.Label(root, text ="Qualification" )
l7.place(x = 30, y = 370)
l7.config(bg='lightblue',font=('Helvetica bold', 13))
 
t7 = tk.Entry(root, width = 35)
t7.place(x = 180, y = 370, width = 200)
  
l8 = tk.Label(root, text ="Branch")
l8.place(x = 400, y = 370)
l8.config(bg='lightblue',font=('Helvetica bold', 13))
 
t8 = tk.Entry(root, width = 35)
t8.place(x = 550, y = 370, width = 200)
 
l9 = tk.Label(root, text ="Year")
l9.place(x = 30, y = 430)
l9.config(bg='lightblue',font=('Helvetica bold', 13))
 
t9 = tk.Entry(root, width = 35)
t9.place(x = 180, y = 430, width = 200)
  
l10 = tk.Label(root, text ="Others")
l10.place(x = 400, y = 430)
l10.config(bg='lightblue',font=('Helvetica bold', 13))
 
t10 = tk.Entry(root, width = 35)
t10.place(x = 550, y = 430, width = 200)

lab3 = tk.Label(root, text ="Login Credentials", )
lab3.place(x = 30, y = 490) 
lab3.config(bg='lightblue',font=('Helvetica bold', 15))

l11 = tk.Label(root, text ="User - Id")
l11.place(x = 30, y = 550)
l11.config(bg='lightblue',font=('Helvetica bold', 13))
 
t11 = tk.Entry(root, width = 35)
t11.place(x = 180, y = 550, width = 200)
  
l12 = tk.Label(root, text ="Password")
l12.place(x = 400, y = 550)
l12.config(bg='lightblue',font=('Helvetica bold', 13))
 
t12 = tk.Entry(root, width = 35)
t12.place(x = 550, y = 550, width = 200)

b1 = tk.Button(root, text ="Clear", bg ='grey',command=Clear)
b1.place(x = 135, y = 600, width = 80)
b1.config(font=('Helvetica bold', 13))

b2 = tk.Button(root, text ="Commit", bg ='grey',command=Insert)
b2.place(x = 220, y = 600, width = 80)
b2.config(font=('Helvetica bold', 13))

b3 = tk.Button(root, text ="View", bg ='grey',command=View)
b3.place(x = 305, y = 600, width = 80)
b3.config(font=('Helvetica bold', 13))

b4 = tk.Button(root, text ="Update", bg ='grey',command=Update)
b4.place(x = 390, y = 600, width = 80)
b4.config(font=('Helvetica bold', 13))

b5 = tk.Button(root, text ="Delete", bg ='grey',command=Delete)
b5.place(x = 475, y = 600, width = 80)
b5.config(font=('Helvetica bold', 13))

b6 = tk.Button(root, text ="Exit", bg ='grey',command=Close)
b6.place(x = 560, y = 600, width = 80)
b6.config(font=('Helvetica bold', 13))

root.mainloop()
