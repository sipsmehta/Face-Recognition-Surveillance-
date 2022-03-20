import mysql.connector as sq
from datetime import datetime as dt
# from __init__ import *

format = '%Y-%m-%d %H:%M:%S'
'''Connecting to the database'''
# cn = sq.connect(username="admin", password="sih",host="localhost", database='sih_main')
cn = sq.connect(username="root", password="SIH",host="localhost", database='sih')
if cn.is_connected() == False:
    print("not connected")
else:
    print("Connection successful")
mc = cn.cursor()


'''Student details table creating function'''


def createdetailtbl():
    qry = "CREATE TABLE IF NOT EXISTS student_details(UID varchar(40) PRIMARY KEY UNIQUE,Name varchar(60),Branch varchar(20),Hostel_name Varchar(20),Room_no int,Mobile varchar(14),Father_Name char(60),Father_Mobile varchar(14),Student_Status VARCHAR(20))"
    mc.execute(qry)


'''Main Log Table'''


def logintbl():
    qry = "CREATE TABLE IF NOT EXISTS global_log(PID bigint auto_increment PRIMARY KEY,UID varchar(40),Name char(60),Place_of_visit VARCHAR(50),Checkin_time DATETIME,Checkout_time DATETIME,Permit_time DATETIME,Branch varchar(20),Pass_Type VARCHAR(20))"
    mc.execute(qry)


''' Creating Student Individual tables'''


def StudentPersonalTable(uid):
    mc.execute("CREATE TABLE IF NOT EXISTS {}(PID bigint PRIMARY KEY,Place_of_visit VARCHAR(50),Checkin_time DATETIME,Checkout_time DATETIME,Permit_time DATETIME,Pass_Status VARCHAR(20))".format(uid))
    print("Table Structure Created Successfully")


def New_Student(uid, name, branch, mobile, father_name, father_mobile, hostel='NA', room_no=0):
    mc.execute("INSERT INTO student_details(uid,name,branch,hostel_name,room_no,mobile,father_name,father_mobile,Student_Status) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        uid, name, branch, hostel, room_no, mobile, father_name, father_mobile, "Inside"))
    cn.commit()
    StudentPersonalTable(uid)


def pass_creation(pid, uid, place, permit):
    permit = dt.strptime(permit, format)
    mc.execute("INSERT INTO {}(pid,place_of_visit,permit_time) VALUES ('{}','{}','{}')".format(
        uid, pid, place, permit))
    cn.commit()


def checkout(uid, checkout, pid=9999):
    checkout = dt.strptime(checkout, format)
    mc.execute('SELECT name,branch FROM student_details WHERE uid="{}"'.format(uid))
    data=mc.fetchall()[0]
    mc.execute("Select place_of_visit,permit_time from {}".format(uid)) #where pass_status="Granted"
    data+=mc.fetchall()[-1]
    mc.execute(
        "INSERT INTO global_log(pid,uid,name,branch,place_of_visit,permit_time,checkout_time) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(pid,uid,data[0],data[1],data[2],data[3],checkout))
    cn.commit()
    mc.execute("UPDATE {} SET checkout_time='{}' where pid={}".format(
        uid, checkout, pid))
    cn.commit()
    mc.execute("UPDATE student_details SET student_status='{}' WHERE uid='{}'".format(
        "Outside", uid))
    cn.commit()


def checkin(uid, checkin, pid=9999):
    checkin = dt.strptime(checkin, format)
    mc.execute(
        "UPDATE global_log SET checkin_time='{}' WHERE pid={}".format(checkin, pid))
    cn.commit()
    mc.execute("UPDATE {} SET checkin_time='{}' where pid={}".format(
        uid, checkin, pid))
    cn.commit()
    mc.execute("UPDATE student_details SET student_status='{}' WHERE uid='{}'".format(
        "Inside", uid))
    cn.commit()


def getdetails(uid):
    mc.execute(
        'SELECT name,Student_status,Branch from student_details where uid="{}"'.format(uid))
    a = mc.fetchall()[0]
    mc.execute(
        'SELECT pass_type,checkout_time,checkin_time from global_log where uid="{}"'.format(uid))

    try:
        b = mc.fetchall()[-1]
    except Exception:
        b = ()
    return a+b


if __name__ == "__main__":
    pid = 1

    createdetailtbl()
    logintbl()

    # New_Student("21BCS2324", "Shivam Kumar", "CSE",
    #             "7017908137", "Shubham Kumar", "9836473647")

    # # _dt = dt.datetime.strptime("2022-11-11 11:11:11", format)

    # New_Student("21BCS2952", "Sarthak Puri", "CSE", "8284829383",
    #             "Pramod Puri", "8383938293", "Zakir-A", 903)

    # New_Student("21BCS2287", "Amulya Paritosh", "CSE", "999999999",
    #             "Father", "7777777777", "Zakir-A", 417)

    # pass_creation(125, "21BCS2287",
    #               "Kharar", "2022-11-11 11:11:11")

    checkout("21BCS2287","2022-11-11 09:11:11",125)
    checkin("21BCS2287","2022-11-11 10:11:11",125)
    
    pass_creation(2, "21BCS2287",
                  "Kharar", "2022-11-11 15:11:11")

    checkout("21BCS2287","2022-11-11 13:11:11",2)
    checkin("21BCS2287","2022-11-11 14:11:11",2)
    
    pass_creation(3, "21BCS2287",
                  "Kharar", "2022-03-11 11:11:11")

    checkout("21BCS2287","2022-03-11 09:11:11",3)
    checkin("21BCS2287","2022-03-11 10:11:11",3)
    
    pass_creation(4, "21BCS2287",
                  "Kharar", "2022-03-21 11:11:11")

    checkout("21BCS2287","2022-03-21 09:11:11",4)
    checkin("21BCS2287","2022-03-21 10:11:11",4)
    
    pass_creation(5, "21BCS2287",
                  "Kharar", "2022-03-22 11:11:11")

    checkout("21BCS2287","2022-03-22 09:11:11",5)
    checkin("21BCS2287","2022-03-22 10:11:11",5)