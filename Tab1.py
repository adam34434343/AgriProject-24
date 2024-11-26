import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()
sql="create table adminreg(aid int primary key,ana varchar(100),dep varchar(100),deg varchar(100),mob varchar(30),mid varchar(100),lid varchar(100),psw varchar(100))"
mycursor.execute(sql)