from PySide6.QtWidgets import QApplication
from windowProperties import WindowProperties
import sys


app = QApplication(sys.argv)
window = WindowProperties()
window.show()
sys.exit(app.exec())
