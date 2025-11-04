from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from qt_table_content import Ui_Form

class Run(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = Run()
window.show()

sys.exit(app.exec())