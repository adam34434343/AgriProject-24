import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()
sql="create table seedplant(sid varchar(100) primary key,loc varchar(100),vlg varchar(100),tlk varchar(100),dst varchar(100),sta varchar(100),pln varchar(100),aar varchar(100),yer varchar(20),alt varchar(100),sna varchar(100),yld varchar(100),abt varchar(100))"
mycursor.execute(sql)