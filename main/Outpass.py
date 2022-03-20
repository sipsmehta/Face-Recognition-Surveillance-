from __init__ import *
# from main.Student import Student


class __DayoutPass__:
    def __init__(self, name: str, out_time: str, place: str, hostel: str, room: int, UID: str) -> None:
        self.name = name
        self.out_time = dt.datetime.strptime(out_time, format)
        self.cheked_out_time = None
        self.in_time = None
        self.checked_in_time = None
        self.allowed_time = dt.datetime.strptime(
            f"{str(dt.date.today())} 19:00", format)
        self.place = place
        self.hostel = hostel
        self.room = room
        self.UID = UID

        self.issued = False


class __NightoutPass__:
    def __init__(self, name: str, out_time: str, place: str, hostel: str, room: int, UID: str) -> None:
        self.name = name

        self.out_time = dt.datetime.strptime(out_time, format)
        self.cheked_out_time = None
        self.in_time = None
        self.checked_in_time = None

        self.allowed_time = dt.datetime.strptime(
            f"{dt.date.today().year + 1}-{dt.date.today().month}-{dt.date.today().day + 1} 19:00", format)

        self.place = place
        self.hostel = hostel
        self.room = room
        self.UID = UID

        self.issued = False


class __LeavePass__:
    def __init__(self, name: str, out_time: str, hostel: str, room: int, UID: str, place: str = 'home') -> None:
        self.name = name

        self.out_time = dt.datetime.strptime(out_time, format)
        self.cheked_out_time = None
        self.in_time = None
        self.checked_in_time = None

        self.place = place
        self.hostel = hostel
        self.room = room
        self.UID = UID

        self.issued = False


class OutPass:

    try:
        data = int(os.listdir("passes")[-1][:-4])+1
    except Exception:
        data = 2000

    @staticmethod
    def incre():
        OutPass.data += 1

    def __init__(self, uid: str, _out_time, _place: str, pass_type: str = "dayout") -> None:

        self.UID = uid

        self.name, self.hostel, self.room = self.details()

        self.place = _place
        self.out_time = dt.datetime.strftime(_out_time, format)

        self.pid = OutPass.data
        OutPass.incre()

        self.outpass = None

        if pass_type == "Dayout Pass":
            self.outpass = __DayoutPass__(
                self.name, self.out_time, self.place, self.hostel, self.room, self.UID)
        elif pass_type == "Nightout Pass":
            self.outpass = __NightoutPass__(
                self.name, self.out_time, self.place, self.hostel, self.room, self.UID)
        elif pass_type == "Leave Pass":
            self.outpass = __LeavePass__(
                self.name, self.out_time, self.hostel, self.room, self.UID, self.place)
        else:
            print("Wrong type")

    def details(self):
        mc.execute(
            'SELECT name,hostel_name,room_no from student_details where uid="{}"'.format(self.UID))
        c = mc.fetchall()[0]
        return c

    def issue(self, ) -> None:
        self.outpass.issued = True

    def check_in(self, time: dt.datetime) -> None:
        self.outpass.checked_in_time = time

    def check_out(self, time: dt.datetime) -> None:
        self.outpass.checked_out_time = time


def createoutpass(uid, out_time, place, pass_type):

    pass_obj = OutPass(uid, out_time, place, pass_type)

    with open(f'passes/{pass_obj.pid}.pkl', 'wb') as f:
        pickle.dump(pass_obj, f)

    return pass_obj.pid
