import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        self.button = QPushButton("Add QLineEdit")
        self.button.clicked.connect(self.addLineEdit)
        self.gridLayout.addWidget(self.button, 0, 0)

        self.row = 1

    def addLineEdit(self):
        lineEdit = QLineEdit()
        self.gridLayout.addWidget(lineEdit, self.row, 0)
        self.row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())