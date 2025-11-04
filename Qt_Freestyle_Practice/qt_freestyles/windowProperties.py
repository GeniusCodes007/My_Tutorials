from PySide6.QtCore import QSize
from PySide6.QtWidgets import QFrame, QLineEdit

from freestyle import Ui_FreestyleUI
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

class WindowProperties(QWidget, Ui_FreestyleUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.itemsNumber_pushbutton.clicked.connect(self.numberOfItems)
        self.addLabel_pushbutton.clicked.connect(self.addLine)
        self.rowCount_pushButton.clicked.connect(self.rowCount)
        self.columnCount_pushButton.clicked.connect(self.columnCount)


        self.font = QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)

        self.minSize = QSize(80, 35)
        self.maxSize = QSize(1000, 35)



    def addLine(self):
        position = self.tableValuesGridLayout.rowCount()

        print(f"the row count here is: {self.tableValuesGridLayout.rowCount()}")

        sn_label = QLabel()
        sn_label.setText(f"{position}")
        sn_label.setFont(self.font)
        sn_label.setMaximumSize(40, 78)
        sn_label.setMinimumSize(30, 35)
        sn_label.setFrameShape(QFrame.Shape.WinPanel)
        sn_label.setFrameShadow(QFrame.Shadow.Plain)

        if position < 10:
            sn_label.setIndent(10)
        elif position > 9:
            sn_label.setIndent(5)
        self.tableValuesGridLayout.addWidget(sn_label, position, 0,1,1)

        surnameLine = QLineEdit()
        surnameLine.setObjectName(f"surnameRecordLineEdit_{position}")
        surnameLine.setFont(self.font)
        surnameLine.setMaximumSize(self.maxSize)
        surnameLine.setMinimumSize(self.minSize)
        self.tableValuesGridLayout.addWidget(surnameLine, position, 1,1,1)

        firstnameLine = QLineEdit()
        firstnameLine.setObjectName(f"firstnameRecordLineEdit_{position}")
        firstnameLine.setFont(self.font)
        firstnameLine.setMaximumSize(self.maxSize)
        firstnameLine.setMinimumSize(self.minSize)
        self.tableValuesGridLayout.addWidget(firstnameLine, position, 2,1,1)

        middleNameLine = QLineEdit()
        middleNameLine.setObjectName(f"midNameRecordLineEdit_{position}")
        middleNameLine.setFont(self.font)
        middleNameLine.setMaximumSize(self.maxSize)
        middleNameLine.setMinimumSize(self.minSize)
        self.tableValuesGridLayout.addWidget(middleNameLine, position, 3,1,1)

        regNoLine = QLineEdit()
        regNoLine.setObjectName(f"regNoRecordLineEdit_{position}")
        regNoLine.setFont(self.font)
        regNoLine.setMaximumSize(120, 35)
        regNoLine.setMinimumSize(105, 35)
        self.tableValuesGridLayout.addWidget(regNoLine, position, 4,1,1)

    def numberOfItems(self):
        print(self.tableValuesGridLayout.count())
        if self.tableKeysGridLaout.count() % 2 == 0:
            print(f"{self.tableValuesGridLayout.count()} \n We are even")
        else:
            print(f"We are gonna make up")
    
    def rowCount(self):
        print(self.tableValuesGridLayout.rowCount() -1)
    
    def columnCount(self):
        print(self.tableValuesGridLayout.columnCount()-1)

"""
class Actions:
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.row 
    def setLabelText(self, rows):
        for label in range(rows):
"""