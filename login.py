from __init__ import *
from guard_view import Ui_GuardDialog
from student_view import Ui_StudentDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi(main_ui, self)

        self.Login.clicked.connect(self.runSlot)

        self.Logo.setPixmap(QPixmap("resources/login.png"))
        self.Logo.setScaledContents(True)

        self.new_window = None
        self.Videocapture = None

    def refreshAll(self):
        """
        Set the text of lineEdit once it's valid
        """
        self.Videocapture = "1"

    @pyqtSlot()
    def runSlot(self):
        """
        Called when the user presses the Run button
        """
        print("Clicked Run")
        self.refreshAll()
        print(self.Videocapture)
        ui.hide()
        if self.LoginType.currentText() == "Guard Login":
            self.guard_view()

        if self.LoginType.currentText() == "Student Login":
            self.student_view()

    def guard_view(self):

        self.new_window = Ui_GuardDialog()
        self.new_window.show()
        self.new_window.startVideo(self.Videocapture)

    def student_view(self):
        self.new_window = Ui_StudentDialog()
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
