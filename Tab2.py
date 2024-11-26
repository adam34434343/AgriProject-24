import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="",database="agritech")
mycursor=mydb.cursor()
sql="create table consumer(sid int primary key,dna varchar(100),fna varchar(100),plc varchar(100),mob varchar(30),mid varchar(100),dep varchar(100),brn varchar(100),yer varchar(50),acy varchar(50),uid varchar(50),psw varchar(50))"
mycursor.execute(sql)