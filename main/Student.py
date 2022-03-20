from __init__ import *


class Student:

    def __init__(self, name: str, uid: str, phonenum: str, father: str, fathernum: int, status: str = "hosteler", hostel: str = None, room: int = None, wardenpermit: bool = None):
        self.name = name
        self.UID = uid
        self.phonenum = phonenum
        self.father = father
        self.fathernum = fathernum
        self.status = status
        self.hostel = hostel
        self.room = room
        self.wardenpermit = wardenpermit

    def IdCardImg(self, img):
        self.idimage = Image.open(img)
        self.idimage = np.asarray(self.idimage)

    def TrainingImages(self, n):
        self.TestImgArr = np.array()
        for i in range(n):
            testing = Image.open(input())
            testing = np.asarray(testing)
            self.TestImgArr.append(testing)

    def Logout(self, outtime, permittime):
        self.outtime = dt.strptime(outtime, format)
        self.permittime = dt.strptime(permittime, format)
        self.intime = False

    def Login(self, intime):
        self.intime = dt.strptime(intime, format)

    def LateNotify(self):
        self.currenttime = (dt.datetime.utcnow(
        ) + dt.timedelta(hours=5, minutes=30)).dt.strptime(format)
        if self.intime == False and self.currenttime > self.permittime:
            print('Notify')
