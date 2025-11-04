import sys
from PyQt6.QtWidgets import QApplication
from lesson3 import Lesson3


app = QApplication(sys.argv)
window = Lesson3()
window.setMinimumWidth(400)
window.setMinimumHeight(100)
window.show()
sys.exit(app.exec())