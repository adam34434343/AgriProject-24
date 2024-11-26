import mysql.connector
import tkinter  as tk 
from tkinter import * 
root= tk.Tk()
root.title("Rain Fall Report")
root.geometry("1050x400")
w=1250
h=400
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(w/2)
y=(screen_height/2)-(h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
 
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="agritech")
conn = mydb.cursor()
conn.execute("select *from raindata")
i=0 
for x in conn: 
	for j in range(len(x)):
		e = Entry(root, width=12, fg='blue') 
		e.grid(row=i, column=j) 
		e.insert(END, x[j])
	i=i+1
root.mainloop()