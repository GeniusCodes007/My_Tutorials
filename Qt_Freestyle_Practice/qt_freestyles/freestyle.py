# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'freestyleUIdbcoOX.ui'
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
        FreestyleUI.resize(707, 466)
        self.horizontalLayout = QHBoxLayout(FreestyleUI)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMainFrame = QFrame(FreestyleUI)
        self.leftMainFrame.setObjectName(u"leftMainFrame")
        self.leftMainFrame.setMinimumSize(QSize(235, 0))
        self.leftMainFrame.setMaximumSize(QSize(235, 16777215))
        self.leftMainFrame.setStyleSheet(u"background-color: rgb(156, 156, 116);")
        self.leftMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMainFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.leftMainWidget = QWidget(self.leftMainFrame)
        self.leftMainWidget.setObjectName(u"leftMainWidget")
        self.verticalLayout_7 = QVBoxLayout(self.leftMainWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.leftSubFrame = QFrame(self.leftMainWidget)
        self.leftSubFrame.setObjectName(u"leftSubFrame")
        self.leftSubFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.leftSubFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftSubFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.infoFrame = QFrame(self.leftSubFrame)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setMaximumSize(QSize(16777215, 80))
        self.infoFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.infoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.infoLabel = QLabel(self.infoFrame)
        self.infoLabel.setObjectName(u"infoLabel")

        self.verticalLayout_2.addWidget(self.infoLabel)


        self.verticalLayout_4.addWidget(self.infoFrame)

        self.addLabel_pushbutton = QPushButton(self.leftSubFrame)
        self.addLabel_pushbutton.setObjectName(u"addLabel_pushbutton")

        self.verticalLayout_4.addWidget(self.addLabel_pushbutton)

        self.itemsNumber_pushbutton = QPushButton(self.leftSubFrame)
        self.itemsNumber_pushbutton.setObjectName(u"itemsNumber_pushbutton")

        self.verticalLayout_4.addWidget(self.itemsNumber_pushbutton)

        self.rowCount_pushButton = QPushButton(self.leftSubFrame)
        self.rowCount_pushButton.setObjectName(u"rowCount_pushButton")

        self.verticalLayout_4.addWidget(self.rowCount_pushButton)

        self.columnCount_pushButton = QPushButton(self.leftSubFrame)
        self.columnCount_pushButton.setObjectName(u"columnCount_pushButton")

        self.verticalLayout_4.addWidget(self.columnCount_pushButton)


        self.verticalLayout_7.addWidget(self.leftSubFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMainWidget)


        self.horizontalLayout.addWidget(self.leftMainFrame)

        self.rightMainFrame = QFrame(FreestyleUI)
        self.rightMainFrame.setObjectName(u"rightMainFrame")
        self.rightMainFrame.setMinimumSize(QSize(447, 448))
        self.rightMainFrame.setStyleSheet(u"background-color: rgb(105, 105, 105);")
        self.rightMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.rightMainFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableKeysFrame = QFrame(self.rightMainFrame)
        self.tableKeysFrame.setObjectName(u"tableKeysFrame")
        self.tableKeysFrame.setMaximumSize(QSize(16777215, 60))
        self.tableKeysFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.tableKeysFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.tableKeysFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableKeysGridLaout = QGridLayout()
        self.tableKeysGridLaout.setObjectName(u"tableKeysGridLaout")
        self.regNoLabel = QLabel(self.tableKeysFrame)
        self.regNoLabel.setObjectName(u"regNoLabel")
        self.regNoLabel.setMinimumSize(QSize(105, 35))
        self.regNoLabel.setMaximumSize(QSize(120, 80))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.regNoLabel.setFont(font)
        self.regNoLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.regNoLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.regNoLabel.setIndent(5)

        self.tableKeysGridLaout.addWidget(self.regNoLabel, 0, 5, 1, 1)

        self.serialNoLabel = QLabel(self.tableKeysFrame)
        self.serialNoLabel.setObjectName(u"serialNoLabel")
        self.serialNoLabel.setMinimumSize(QSize(30, 35))
        self.serialNoLabel.setMaximumSize(QSize(40, 80))
        self.serialNoLabel.setFont(font)
        self.serialNoLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.serialNoLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.serialNoLabel.setIndent(2)

        self.tableKeysGridLaout.addWidget(self.serialNoLabel, 0, 0, 1, 1)

        self.firstnameLabel = QLabel(self.tableKeysFrame)
        self.firstnameLabel.setObjectName(u"firstnameLabel")
        self.firstnameLabel.setMinimumSize(QSize(80, 35))
        self.firstnameLabel.setMaximumSize(QSize(16777215, 35))
        self.firstnameLabel.setFont(font)
        self.firstnameLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.firstnameLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.firstnameLabel.setIndent(5)

        self.tableKeysGridLaout.addWidget(self.firstnameLabel, 0, 3, 1, 1)

        self.middlenameLlabel = QLabel(self.tableKeysFrame)
        self.middlenameLlabel.setObjectName(u"middlenameLlabel")
        self.middlenameLlabel.setMinimumSize(QSize(80, 35))
        self.middlenameLlabel.setMaximumSize(QSize(16777215, 35))
        self.middlenameLlabel.setFont(font)
        self.middlenameLlabel.setFrameShape(QFrame.Shape.WinPanel)
        self.middlenameLlabel.setFrameShadow(QFrame.Shadow.Raised)
        self.middlenameLlabel.setIndent(5)

        self.tableKeysGridLaout.addWidget(self.middlenameLlabel, 0, 4, 1, 1)

        self.surnameLabel = QLabel(self.tableKeysFrame)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setMinimumSize(QSize(80, 35))
        self.surnameLabel.setMaximumSize(QSize(16777215, 35))
        self.surnameLabel.setFont(font)
        self.surnameLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.surnameLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.surnameLabel.setIndent(10)

        self.tableKeysGridLaout.addWidget(self.surnameLabel, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.tableKeysGridLaout)


        self.verticalLayout_6.addWidget(self.tableKeysFrame)

        self.tableValueFrame = QFrame(self.rightMainFrame)
        self.tableValueFrame.setObjectName(u"tableValueFrame")
        self.tableValueFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.tableValueFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.tableValueFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableValuesGridLayout = QGridLayout()
        self.tableValuesGridLayout.setObjectName(u"tableValuesGridLayout")

        self.verticalLayout_5.addLayout(self.tableValuesGridLayout)


        self.verticalLayout_6.addWidget(self.tableValueFrame)


        self.horizontalLayout.addWidget(self.rightMainFrame)


        self.retranslateUi(FreestyleUI)

        QMetaObject.connectSlotsByName(FreestyleUI)
    # setupUi

    def retranslateUi(self, FreestyleUI):
        FreestyleUI.setWindowTitle(QCoreApplication.translate("FreestyleUI", u"Form", None))
        self.infoLabel.setText(QCoreApplication.translate("FreestyleUI", u"New Labels Are To Be Added", None))
        self.addLabel_pushbutton.setText(QCoreApplication.translate("FreestyleUI", u"Add New Line", None))
        self.itemsNumber_pushbutton.setText(QCoreApplication.translate("FreestyleUI", u"Number of Cells In Table", None))
        self.rowCount_pushButton.setText(QCoreApplication.translate("FreestyleUI", u"Row Count", None))
        self.columnCount_pushButton.setText(QCoreApplication.translate("FreestyleUI", u"Column Count", None))
        self.regNoLabel.setText(QCoreApplication.translate("FreestyleUI", u"Reg. Number", None))
        self.serialNoLabel.setText(QCoreApplication.translate("FreestyleUI", u"S/N", None))
        self.firstnameLabel.setText(QCoreApplication.translate("FreestyleUI", u"Firstname", None))
        self.middlenameLlabel.setText(QCoreApplication.translate("FreestyleUI", u"Middlename", None))
        self.surnameLabel.setText(QCoreApplication.translate("FreestyleUI", u"Surname", None))
    # retranslateUi

