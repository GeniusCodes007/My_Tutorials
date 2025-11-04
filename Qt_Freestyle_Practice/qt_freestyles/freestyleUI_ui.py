# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'freestyleUIPZEAob.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FreestyleUI(object):
    def setupUi(self, FreestyleUI):
        if not FreestyleUI.objectName():
            FreestyleUI.setObjectName(u"FreestyleUI")
        FreestyleUI.resize(599, 358)
        self.horizontalLayout = QHBoxLayout(FreestyleUI)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(FreestyleUI)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(288, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(156, 156, 116);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.addLabel_pushbutton = QPushButton(self.frame_4)
        self.addLabel_pushbutton.setObjectName(u"addLabel_pushbutton")

        self.verticalLayout_4.addWidget(self.addLabel_pushbutton)

        self.itemsNumber_pushbutton = QPushButton(self.frame_4)
        self.itemsNumber_pushbutton.setObjectName(u"itemsNumber_pushbutton")

        self.verticalLayout_4.addWidget(self.itemsNumber_pushbutton)

        self.rowCount_pushButton = QPushButton(self.frame_4)
        self.rowCount_pushButton.setObjectName(u"rowCount_pushButton")

        self.verticalLayout_4.addWidget(self.rowCount_pushButton)

        self.columnCount_pushButton = QPushButton(self.frame_4)
        self.columnCount_pushButton.setObjectName(u"columnCount_pushButton")

        self.verticalLayout_4.addWidget(self.columnCount_pushButton)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(FreestyleUI)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(105, 105, 105);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(FreestyleUI)

        QMetaObject.connectSlotsByName(FreestyleUI)
    # setupUi

    def retranslateUi(self, FreestyleUI):
        FreestyleUI.setWindowTitle(QCoreApplication.translate("FreestyleUI", u"Form", None))
        self.label.setText(QCoreApplication.translate("FreestyleUI", u"New Labels Are To Be Added", None))
        self.addLabel_pushbutton.setText(QCoreApplication.translate("FreestyleUI", u"Add A Label", None))
        self.itemsNumber_pushbutton.setText(QCoreApplication.translate("FreestyleUI", u"Number of items In GridLayout", None))
        self.rowCount_pushButton.setText(QCoreApplication.translate("FreestyleUI", u"Row Count", None))
        self.columnCount_pushButton.setText(QCoreApplication.translate("FreestyleUI", u"Column Count", None))
    # retranslateUi

