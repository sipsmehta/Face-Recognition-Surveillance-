from __init__ import *
from Database import databaseFunctions as dbf
from main.Outpass import createoutpass


class Ui_StudentDialog(QDialog):
    def __init__(self, uid):
        super(Ui_StudentDialog, self).__init__()
        loadUi(student_ui, self)

        self.UID = uid

        self.ApplyPass.clicked.connect(self.apply_pass)

    def apply_pass(self):

        pass_type = self.PassType.currentText()
        place = self.PlaceOfVisit.text()
        out_time = QDateTime(self.OutDate.selectedDate(),
                             self.OutTime.time()).toPyDateTime()

        pid = createoutpass(self.UID, out_time, place, pass_type)

        dbf.pass_creation(pid, self.UID, place)
        # print(self.OutTime.time())
        # print(self.OutDate.selectedDate())

        # print()

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    new_window = Ui_StudentDialog("22")
    new_window.show()
    sys.exit(app.exec_())
