import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor = mydb.cursor()

sql="select *from agriln"
mycursor.execute(sql)
resultset=mycursor.fetchall()
dhd=[]
dvl=[]
for x in resultset:
	dhd.append(x[8])
	dvl.append(int(x[9]))
print(dhd)
print(dvl)

x = np.array(dhd)
y = np.array(dvl)

plt.bar(x, y, width = 0.1)
plt.title("Year VS Amount Alloacted")
plt.xlabel("Year")
plt.ylabel("Amount Allocated")
plt.show()