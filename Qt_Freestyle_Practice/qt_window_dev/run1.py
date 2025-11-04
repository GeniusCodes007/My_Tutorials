import sys
from PyQt6.QtWidgets import *
from lesson1 import Lesson1


app = QApplication(sys.argv)
window = Lesson1()
window.show()

sys.exit(app.exec())