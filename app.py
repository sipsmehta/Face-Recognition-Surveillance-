from main.login import Ui_Dialog
from __init__ import *
import qdarkstyle

app = QApplication(sys.argv)
ui = Ui_Dialog()

app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

ui.show()
sys.exit(app.exec_())
