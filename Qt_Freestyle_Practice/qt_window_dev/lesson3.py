from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QCheckBox, QLabel

class Lesson3(QWidget):

    cost_coffee = 33.5
    cost_sugar = 12.5
    cost_milk = 25.0
    total_coffee_cost = cost_coffee

    def __init__(self):
        super().__init__()
        self.total_cost = None
        self.featuresUI()

    def featuresUI(self):
        self.setWindowTitle("Lesson 3")

        window_info = QLabel(self)
        window_info.setText("About QCheckBox IN PyQt")
        window_info.setFont(QFont("Times New Roman", 15))
        window_info.move(10, 40)

    #Coffee Making App

        app_info = QLabel(self)
        app_info.setText("Coffee Making App")
        app_info.setFont(QFont("Times New Roman", 14))
        app_info.move(10, 90)

        #QCheckBox For Sugar
        checkBoxSugar = QCheckBox(self)
        checkBoxSugar.setText("Sugar")
        checkBoxSugar.move(10, 110)
        checkBoxSugar.clicked.connect(self.sugar_present)
        #checkBox.toggled.connect(self.sugar_present)

        #QCheckBox For Milk
        checkBoxMilk = QCheckBox(self)
        checkBoxMilk.setText("Milk")
        checkBoxMilk.move(10, 130)
        checkBoxMilk.clicked.connect(self.milk_present)
        #checkBoxMilk.toggled.connect(self.milk_present)

        #QLabel For Cost Of Coffee
        self.total_cost = QLabel(self)
        self.total_cost.setText(f"Total Cost Of Coffee: {self.total_coffee_cost}")
        self.total_cost.adjustSize()
        self.total_cost.move(10, 150)

    def sugar_present(self, checked):
        val = float(self.total_cost.text()[22:])
        if checked:
            print("Sugar present")
            self.total_cost.setText(f"Total Cost Of Coffee: {val + self.cost_sugar}")
        else:
            print("Sugar Absent")
            self.total_cost.setText(f"Total Cost Of Coffee: {val - self.cost_sugar}")

    def milk_present(self, checked):
        val = float(self.total_cost.text()[22:])
        if checked:
            print("Milk present")
            self.total_cost.setText(f"Total Cost Of Coffee: {val + self.cost_milk}")
        else:
            print("Milk Absent")
            self.total_cost.setText(f"Total Cost Of Coffee: {val - self.cost_milk}")