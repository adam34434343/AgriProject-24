import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()
sql="create table agriln(lid varchar(100) primary key,loc varchar(100),vlg varchar(100),tlk varchar(100),dst varchar(100),sta varchar(100),pln varchar(100),aar varchar(100),yer varchar(20),amt varchar(100),lna varchar(100),apl varchar(100),dux varchar(100),dun varchar(100),rmk varchar(1500))"
mycursor.execute(sql)