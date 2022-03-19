import mysql.connector as sq
from datetime import datetime as dt
from psycopg2 import sql

timeformat='%Y-%m-%d %H:%M:%S'
'''Connecting to the database'''
cn=sq.connect(username="root",password="SIH",host="localhost",database='sih')
if cn.is_connected()==False:
    print("not connected")
else:
    print("Connection successful")
mc=cn.cursor()


'''Student details table creating function'''
def createdetailtbl():
    qry="CREATE TABLE IF NOT EXISTS student_details(UID varchar(40) PRIMARY KEY UNIQUE,Name varchar(60),Branch varchar(20),Hostel_name Varchar(20),Room_no int,Mobile varchar(14),Father_Name char(60),Father_Mobile varchar(14))"
    mc.execute(qry)

'''Main Log Table'''
def logintbl():
    qry="CREATE TABLE IF NOT EXISTS global_log(PID bigint auto_increment PRIMARY KEY,UID varchar(40),Name char(60),Place_of_visit VARCHAR(50),Checkin_time DATETIME,Checkout_time DATETIME,Permit_time DATETIME,Branch varchar(20))"
    mc.execute(qry)

''' Creating Student Individual tables'''
def StudentPersonalTable(uid):
    mc.execute("CREATE TABLE IF NOT EXISTS {}(PID bigint,Place_of_visit VARCHAR(50),Checkin_time DATETIME,Checkout_time DATETIME,Permit_time DATETIME)".format(uid))
    print ("Table Structure Created Successfully")


def New_Student(uid,name,branch,mobile,father_name,father_mobile,hostel='NA',room_no=0):
    mc.execute("INSERT INTO student_details(uid,name,branch,hostel_name,room_no,mobile,father_name,father_mobile) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(uid,name,branch,hostel,room_no,mobile,father_name,father_mobile))
    cn.commit()
    StudentPersonalTable(uid)

def pass_creation(pid,uid,name,place,permit,branch):
    permit=dt.strptime(permit,timeformat)
    mc.execute("INSERT INTO global_log(pid,uid,name,place_of_visit,permit_time,branch) VALUES ('{}','{}','{}','{}','{}','{}')".format(pid,uid,name,place,permit,branch))
    cn.commit()
    mc.execute("INSERT INTO {}(pid,place_of_visit,permit_time) VALUES ('{}','{}','{}')".format(uid,pid,place,permit))
    cn.commit()
    

def checkout(uid,pid,checkout):
    checkout=dt.strptime(checkout,timeformat)
    mc.execute("UPDATE global_log SET checkout_time='{}' WHERE pid={}".format(checkout,pid))
    cn.commit()
    mc.execute("UPDATE {} SET checkout_time='{}' where pid={}".format(uid,checkout,pid))
    cn.commit()


def checkin(uid,pid,checkin):
    checkin=dt.strptime(checkin,timeformat)
    mc.execute("UPDATE global_log SET checkin_time='{}' WHERE pid={}".format(checkin,pid))
    cn.commit()
    mc.execute("UPDATE {} SET checkin_time='{}' where pid={}".format(uid,checkin,pid))
    cn.commit()



createdetailtbl()
logintbl()
New_Student("21BCS2324","Shivam Kumar","CSE","7017908137","Shubham Kumar","9836473647")
pass_creation(1,"21BCS2324","Shivam Kumar","Kharar","2022-11-11 11:11:11","CSE")
checkout("21BCS2324",1,'2022-11-11 09:11:11')
checkin("21BCS2324",1,'2022-11-11 10:11:11')
New_Student("21BCS2952","Sarthak Puri","CSE","8284829383","Pramod Puri","8383938293","Zakir-A",903)
