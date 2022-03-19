from main.login import Ui_Dialog
from __init__ import *

app = QApplication(sys.argv)
ui = Ui_Dialog()

apply_stylesheet(app, theme='dark_blue.xml')

ui.show()
sys.exit(app.exec_())
