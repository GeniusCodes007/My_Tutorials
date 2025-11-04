from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QFont

class Lesson1(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lesson 1")
        #to set a window to open in the top left corner of the screen: (x,y) -> (0,0)
        #the following parameters are the width and height respectively
        self.setGeometry(500,150,400, 300)
        
        #QLabel Widget
        label = QLabel(self)
        label.setText("Hi, I am learning PyQt6\n"
                      "From the basics this time around\n")
        label.setFont(QFont("Times New Roman", 18))
        #posiioning the label on the window

        label.move(10,20)
        #label.move(40,0)
        #label.move(200,70)
        #label.move(150,130)#puts it in the center
        #label.move(40,200)
        #label.move(70,100)
        #label.move(500, 40)

#
        #Displaying picture in a label
        with open('UltimatePower.png'):
            image_label = QLabel(self)
            pixmap = QPixmap('UltimatePower.png')
            pixmap.setDevicePixelRatio(2.5)
            image_label.setPixmap(pixmap)
            image_label.move(90, 300)

        with open('blessed-sacrament-in-monstrance.jpg'):
            image_label2 = QLabel(self)
            pixmap2 = QPixmap('blessed-sacrament-in-monstrance.jpg')
            pixmap2.setDevicePixelRatio(3.5)
            image_label2.setPixmap(pixmap2)
            image_label2.move(300, 300)

        image_name = QLabel(self)
        image_name.setText("The Ultimate Power")
        image_name.setFont(QFont("Times New Roman", 18))
        image_name.move(50,500)

        pushbutton = QPushButton(self)
        pushbutton.setText("Press Me")
        pushbutton.setFont(QFont("Times New Roman", 14))
        pushbutton.move(40,200)
        pushbutton.clicked.connect(self.clickStatus)

    @staticmethod
    def clickStatus():
        print("You Clicked Me")

