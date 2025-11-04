from PySide6.QtWidgets import QApplication
import sys
from edit import Edit


app = QApplication(sys.argv)
window = Edit()
window.show()
sys.exit(app.exec())