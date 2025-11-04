
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit


class Lesson2(QWidget):
    count = 0

    def __init__(self):
        super().__init__()

        self.label1 = None
        self.pushbutton = None
        self.featuresUI()

    def featuresUI(self):
        self.setWindowTitle("Lesson 2")
        # to set a window to open in the top left corner of the screen: (x,y) -> (0,0)
        # the following parameters are the width and height respectively
        self.setGeometry(500, 150, 400, 300)

        # QLabel Widget
        label = QLabel(self)
        label.setText("Hi, I am learning PyQt6\n"
                      "Besides this is the Second Lesson\n")
        label.setFont(QFont("Arial", 14))
        label.move(0, 0)

        self.label1 = QLabel(self)
        self.label1.setText("Hi, I'm gonna change")
        self.label1.move(0, 70)

        pushbutton = QPushButton(self)
        pushbutton.setText("Change Text")
        pushbutton.move(0, 200)

        pushbutton.clicked.connect(self.changeText)

        name_label = QLabel(self)
        name_label.setText("Give Me Your Name:")
        name_label.setFont(QFont("Times New Roman", 16))
        name_label.move(50, 100)

        name_input = QLineEdit(self)

        name_input.resize(200, 30)
        print(name_input.size())
        name_input.move(50, 130)

    def changeText(self):
        self.count +=1
        self.label1.setText(f"It changed {self.count} times")
        self.label1.adjustSize()

