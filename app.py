from main.login import Ui_Dialog
from __init__ import *

app = QApplication(sys.argv)
ui = Ui_Dialog()
ui.show()
sys.exit(app.exec_())
