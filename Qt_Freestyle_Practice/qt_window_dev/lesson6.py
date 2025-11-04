from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QLayout


class Lesson6(QWidget):
    def __init__(self):
        super().__init__()

        self.featuresUI()

    def featuresUI(self):
        self.setWindowTitle("Lesson 5")
        #self.setGeometry(150,400, 200, 250)

        label1 = QLabel("Label 1")
        name = QLineEdit()
        button = QPushButton("Add")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(name)
        layout.addWidget(button)

        self.setLayout(layout)



        layout.addWidget(label1,0)
        layout.addWidget(name,1)
        layout.addWidget(button,2)



        self.setLayout(layout)