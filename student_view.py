from __init__ import *


class Ui_StudentDialog(QDialog):
    def __init__(self):
        super(Ui_StudentDialog, self).__init__()
        loadUi(student_ui, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    new_window = Ui_StudentDialog()
    new_window.show()
    sys.exit(app.exec_())
