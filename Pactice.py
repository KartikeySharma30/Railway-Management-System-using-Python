import mysql.connector
UserLog=mysql.connector.connect(host="localhost",user="root",passwd="Kartikey30",database="ProjectRailway")
C1=UserLog.cursor()
From_Chk="Select Station_Name From station"
C1.execute(From_Chk)
F1=C1.fetchall()
b=[]
for Frm in F1:
    a=list(Frm)
    b.append(a)
b=tuple(b)
print(b)
