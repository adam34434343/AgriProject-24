import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()
sql="create table soildata(lid varchar(100) primary key,loc varchar(100),vlg varchar(100),tlk varchar(100),dst varchar(100),sta varchar(100),pln varchar(100),aar varchar(100),sar varchar(20),stp varchar(100),sut varchar(100),yld varchar(100),sct varchar(100))"
mycursor.execute(sql)