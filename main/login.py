from __init__ import *
from main.guard_view import Ui_GuardDialog
from main.student_view import Ui_StudentDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi(main_ui, self)

        self.Login.clicked.connect(self.runSlot)

        self.Logo.setPixmap(QPixmap("resources/login.png"))
        self.Logo.setScaledContents(True)

        self.new_window = None
        self.Videocapture = camera

    @pyqtSlot()
    def runSlot(self):

        print(self.Videocapture)
        self.hide()
        if self.LoginType.currentText() == "Guard Login":
            self.guard_view()

        if self.LoginType.currentText() == "Student Login":
            self.student_view()

    def guard_view(self):

        self.new_window = Ui_GuardDialog()
        self.new_window.startVideo(self.Videocapture)
        self.new_window.show()

    def student_view(self):
        self.new_window = Ui_StudentDialog()
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
