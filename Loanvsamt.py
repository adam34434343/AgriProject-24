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
yvl=[]
for x in resultset:
	dhd.append(x[10])
	yvl.append(x[8])
	dvl.append(int(x[9]))

print(dhd)
print(dvl)
print(yvl)

y=np.array(dhd)
x=np.array(dvl)
z=np.array(yvl)
plt.barh(range(len(x)), x)
plt.yticks(range(len(x)), y)
plt.yticks(range(len(x)), z)


plt.title("Loan-Type VS Amount Alloacted")
plt.xlabel("Amount Allocated")
plt.ylabel("Loan Type")
plt.show()