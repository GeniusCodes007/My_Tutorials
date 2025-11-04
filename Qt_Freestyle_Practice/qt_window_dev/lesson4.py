from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QMessageBox, QMainWindow, QLabel, QPushButton


class Lesson4(QMainWindow):
    def __init__(self):
        super().__init__()

        self.featuresUI()

    def featuresUI(self):
        self.setWindowTitle("Lesson 4")

        window_info = QLabel(self)
        window_info.resize(300, 40)
        window_info.setText("About QMessageBox In PyQt")
        window_info.setFont(QFont("Times New Roman", 14))
        window_info.move(10, 40)

        button = QPushButton("Show Message Box",self)
        button.adjustSize()
        #button.setGeometry(20, 100, 120, 30)
        button.move(10, 70)
        button.clicked.connect(self.show_warning)

    def show_warning(self):
        warn = QMessageBox()
        warn.setWindowTitle("My Warning")
        warn.setText("I Saw You!!!, Do You Accept My Challenge")
        #warn.setIcon(QMessageBox.Icon.Information)
        warn.setIcon(QMessageBox.Icon.Warning)
        warn.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Cancel)
        warn.setDefaultButton(QMessageBox.StandardButton.Ok)
        display = warn.exec()
        #warn.exec()

        if display == QMessageBox.StandardButton.Ok:
            print("You Agreed!!!, That's Great")
        elif display == QMessageBox.StandardButton.Cancel:
            print("Hahaha!!!, You Quit")
        else:
            print("Oh Dear!!!, You Shouldn't Have Avoided The Challenge")
