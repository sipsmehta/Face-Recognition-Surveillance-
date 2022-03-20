from __init__ import *


class Ui_WardenDialog(QDialog):
    def __init__(self):
        super(Ui_WardenDialog, self).__init__()
        loadUi(warden_ui, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    new_window = Ui_WardenDialog()
    new_window.show()
    sys.exit(app.exec_())
