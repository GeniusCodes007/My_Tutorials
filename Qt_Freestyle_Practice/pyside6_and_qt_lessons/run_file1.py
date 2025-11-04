import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Creating App With QMainWindow class")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
sys.exit(app.exec())


#When creating an app in a QMainWindow class, we can set a central widget