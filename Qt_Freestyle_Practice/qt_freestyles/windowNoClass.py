import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Butt")

        button = QPushButton("Press Me")

        self.setCentralWidget(button)

app = QApplication(sys.argv)
win = ButtonHolder()
win.show()
sys.exit(app.exec())