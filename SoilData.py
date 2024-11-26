import tkinter as tk
import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()

def Clear():
	t1.delete(0,'end')
	t2.delete(0,'end')
	t3.delete(0,'end')
	t4.delete(0,'end')
	t5.delete(0,'end')
	t6.delete(0,'end')
	t7.delete(0,'end')
	t8.delete(0,'end')
	t9.delete(0,'end')
	t10.delete(0,'end')
	t11.delete(0,'end')
	t12.delete(0,'end')
	t13.delete(1.0,'end')
def Commit():
	d1=t1.get()
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
	d13=t13.get(1.0,'end')
	val=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13)
	sql="insert into soildata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	mycursor.execute(sql,val)
	mydb.commit()

def View():
	lid=t1.get()
	val=(lid,)
	sql="select *from soildata where lid=%s"
	mycursor.execute(sql,val)
	resultset=mycursor.fetchall()
	for x in resultset:
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
		t13.insert(1.0,x[12])
def Edit():
	d1=t1.get()
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
	d13=t13.get(1.0,'end')
	val=(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d1)
	sql="update soildata set loc=%s,vlg=%s,tlk=%s,dst=%s,sta=%s,pln=%s,aar=%s,sar=%s,stp=%s,sut=%s,yld=%s,sct=%s where lid=%s"
	mycursor.execute(sql,val)
	mydb.commit()

def Delete():
	lid=t1.get()
	val=(lid,)
	sql="delete from soildata where lid=%s"
	mycursor.execute(sql,val)
	mydb.commit()

root=tk.Tk()

w=800
h=600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Soil - Information")
root.config(bg='lightblue')

hlab = tk.Label(root, text ="AREA SOIL INFORMATION")
hlab.place(x = 70, y = 10) 
hlab.config(fg='blue',bg='lightblue',font=('Helvetica bold', 30))

w=650
h=560
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Consumer Login")
root.config(bg='lightblue')

lab = tk.Label(root, text ="Locality / Soil Information")
lab.place(x=20, y=70) 
lab.config(fg='black',bg='lightblue',font=('Helvetica bold', 15,'bold'))

l1 = tk.Label(root, text ="Location - Id" )
l1.place(x=20, y =120)
l1.config(fg='black', bg='lightblue',font=('Arial', 13))
t1 = tk.Entry(root)
t1.place(x=150, y =120,width=150)

l2 = tk.Label(root, text ="Location Name" )
l2.place(x=340, y =120)
l2.config(fg='black', bg='lightblue',font=('Arial', 13))
t2 = tk.Entry(root)
t2.place(x=470, y =120,width=150)

l3 = tk.Label(root, text ="Village" )
l3.place(x=20, y =170)
l3.config(fg='black', bg='lightblue',font=('Arial', 13))
t3 = tk.Entry(root)
t3.place(x=150, y =170,width=150)

l4 = tk.Label(root, text ="Taluk" )
l4.place(x=340, y =170)
l4.config(fg='black', bg='lightblue',font=('Arial', 13))
t4 = tk.Entry(root)
t4.place(x=470, y =170,width=150)

l5 = tk.Label(root, text ="District" )
l5.place(x=20, y =220)
l5.config(fg='black', bg='lightblue',font=('Arial', 13))
t5 = tk.Entry(root)
t5.place(x=150, y =220,width=150)

l6 = tk.Label(root, text ="State" )
l6.place(x=340, y =220)
l6.config(fg='black', bg='lightblue',font=('Arial', 13))
t6 = tk.Entry(root)
t6.place(x=470, y =220,width=150)

l7 = tk.Label(root, text ="Population" )
l7.place(x=20, y =270)
l7.config(fg='black', bg='lightblue',font=('Arial', 13))
t7 = tk.Entry(root)
t7.place(x=150, y =270,width=150)

l8 = tk.Label(root, text ="Total Agri Area" )
l8.place(x=340, y =270)
l8.config(fg='black', bg='lightblue',font=('Arial', 13))
t8 = tk.Entry(root)
t8.place(x=470, y =270,width=150)

l9 = tk.Label(root, text ="Survey Area" )
l9.place(x=20, y =320)
l9.config(fg='black', bg='lightblue',font=('Arial', 13))
t9 = tk.Entry(root)
t9.place(x=150, y =320,width=150)

l10 = tk.Label(root, text ="Soil Type" )
l10.place(x=340, y =320)
l10.config(fg='black', bg='lightblue',font=('Arial', 13))
t10 = tk.Entry(root)
t10.place(x=470, y =320,width=150)

l11 = tk.Label(root, text ="Suitable for" )
l11.place(x=20, y =370)
l11.config(fg='black', bg='lightblue',font=('Arial', 13))
t11 = tk.Entry(root)
t11.place(x=150, y =370,width=150)

l12=tk.Label(root, text ="Yield" )
l12.place(x=340, y =370)
l12.config(fg='black', bg='lightblue',font=('Arial', 13))
t12=tk.Entry(root)
t12.place(x=470, y =370,width=150)

l13 = tk.Label(root, text ="Soil Contents")
l13.place(x=20, y =420)
l13.config(fg='black', bg='lightblue',font=('Arial', 13))
t13 = tk.Text(root)
t13.place(x=150, y =420,width=470,height=70)

b1=tk.Button(root,text="Clear",command=Clear)
b1.place(x=20,y=510,width=100)

b2=tk.Button(root,text="Commit",command=Commit)
b2.place(x=120,y=510,width=100)

b3=tk.Button(root,text="View",command=View)
b3.place(x=220,y=510,width=100)

b4=tk.Button(root,text="Edit",command=Edit)
b4.place(x=320,y=510,width=100)

b5=tk.Button(root,text="Delete",command=Delete)
b5.place(x=420,y=510,width=100)

b6=tk.Button(root,text="Exit",command=exit)
b6.place(x=520,y=510,width=100)

root.mainloop()