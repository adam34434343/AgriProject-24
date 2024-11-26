import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor = mydb.cursor()

sql="select *from fertilizer"
mycursor.execute(sql)
resultset=mycursor.fetchall()
dhd=[]
dvl=[]
yvl=[]
for x in resultset:
	dhd.append(x[8]+"\n"+x[10])
	dvl.append(int(x[9]))

print(dhd)
print(dvl)

y=np.array(dhd)
x=np.array(dvl)
plt.barh(range(len(x)), x)
plt.yticks(range(len(x)), y)

plt.title("Agri-Product VS Allotment")
plt.xlabel("Agri Product")
plt.ylabel("Total Allotment")
plt.show()