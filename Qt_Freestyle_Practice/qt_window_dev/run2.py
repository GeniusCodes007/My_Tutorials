import sys
from PyQt6.QtWidgets import *
from lesson2 import Lesson2

app = QApplication(sys.argv)
window = Lesson2()
window.show()
sys.exit(app.exec())