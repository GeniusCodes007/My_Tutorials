 #background-color: rgb(103, 103, 103);
import sys
from PySide6.QtWidgets import QApplication
from edittingActionsFile import DropAndSideMainWindow

app = QApplication(sys.argv)
window = DropAndSideMainWindow()
window.show()
sys.exit(app.exec())