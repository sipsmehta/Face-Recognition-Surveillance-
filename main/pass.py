from __init__ import *
from Student import Student


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
            f"{dt.date.today().year+1}-{dt.date.today().month}-{dt.date.today().day+1} 19:00", format)

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
    def __init__(self, student: Student, _out_time: str, _place: str, pass_type: str = "dayout") -> None:

        name = student.name
        UID = student.UID
        hostel = student.hostel
        room = student.room
        place = _place
        out_time = _out_time

        self.outpass = None

        if pass_type == "dayout":
            self.outpass = __DayoutPass__(
                name, out_time, place, hostel, room, UID)
        elif pass_type == "nightout":
            self.outpass = __NightoutPass__(
                name, out_time, place, hostel, room, UID)
        elif pass_type == "leave":
            self.outpass = __LeavePass__(
                name, out_time, hostel, room, UID, place)
        else:
            print("Wrong type")

    def issue(self,) -> None:
        self.outpass.issued = True

    def check_in(self, time: dt.datetime) -> None:
        self.outpass.checked_in_time = time

    def check_out(self, time: dt.datetime) -> None:
        self.outpass.checked_out_time = time


if __name__ == "__main__":
    stu1 = Student("Amulya", "21BCS2287", "1111111111", "xyz",
                   "2222222222", hostel="Zakir", room=666)
    time = dt.datetime.now().strftime(format)
    op1 = OutPass(stu1, time, "kharar")
