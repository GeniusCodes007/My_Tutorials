import sys
from PyQt6.QtWidgets import QApplication
from lesson4 import Lesson4


app = QApplication(sys.argv)
window = Lesson4()
window.show()
sys.exit(app.exec())