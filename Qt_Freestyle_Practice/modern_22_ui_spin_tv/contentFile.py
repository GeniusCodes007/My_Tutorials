# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spin_tv_sFLRHt.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SpinTVMainWindow(object):
    def setupUi(self, SpinTVMainWindow):
        if not SpinTVMainWindow.objectName():
            SpinTVMainWindow.setObjectName(u"SpinTVMainWindow")
        SpinTVMainWindow.resize(1026, 500)
        SpinTVMainWindow.setStyleSheet(u"\n"
"background-color: rgb(103, 103, 103);")
        self.centralwidget = QWidget(SpinTVMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftMenuSub = QWidget(self.leftMenuContainer)
        self.leftMenuSub.setObjectName(u"leftMenuSub")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSub)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftMenuSub)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.menu_button = QPushButton(self.frame)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon = QIcon()
        icon.addFile(u"resource_folder_test/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon)

        self.verticalLayout_3.addWidget(self.menu_button)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSub)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.home_button = QPushButton(self.frame_2)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon1 = QIcon()
        icon1.addFile(u"resource_folder_test/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_button.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.home_button)

        self.analysis_button = QPushButton(self.frame_2)
        self.analysis_button.setObjectName(u"analysis_button")
        self.analysis_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon2 = QIcon()
        icon2.addFile(u"resource_folder_test/data_analysis.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analysis_button.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.analysis_button)

        self.reports_button = QPushButton(self.frame_2)
        self.reports_button.setObjectName(u"reports_button")
        self.reports_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon3 = QIcon()
        icon3.addFile(u"resource_folder_test/reports.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reports_button.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.reports_button)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSub)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.settings_button = QPushButton(self.frame_3)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon4 = QIcon()
        icon4.addFile(u"resource_folder_test/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.settings_button)

        self.info_button = QPushButton(self.frame_3)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon5 = QIcon()
        icon5.addFile(u"resource_folder_test/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.info_button)

        self.help_button = QPushButton(self.frame_3)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        icon6 = QIcon()
        icon6.addFile(u"resource_folder_test/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_button.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.help_button)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSub, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignmentFlag.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        self.mainBodyContainer.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.centerMenuContainer = QWidget(self.mainBodyContainer)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setGeometry(QRect(100, 160, 120, 80))
        self.centerMenuContainer.setStyleSheet(u"background-color: rgb(103, 103, 103);")

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        SpinTVMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpinTVMainWindow)

        QMetaObject.connectSlotsByName(SpinTVMainWindow)
    # setupUi

    def retranslateUi(self, SpinTVMainWindow):
        SpinTVMainWindow.setWindowTitle(QCoreApplication.translate("SpinTVMainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"MENU", None))
#if QT_CONFIG(tooltip)
        self.home_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"HOME", None))
#if QT_CONFIG(tooltip)
        self.analysis_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.analysis_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"DATA ANALYSIS", None))
#if QT_CONFIG(tooltip)
        self.reports_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reports_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"REPORTS", None))
#if QT_CONFIG(tooltip)
        self.settings_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"SETTINGS", None))
#if QT_CONFIG(tooltip)
        self.info_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Info", None))
#endif // QT_CONFIG(tooltip)
        self.info_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"INFO", None))
#if QT_CONFIG(tooltip)
        self.help_button.setToolTip(QCoreApplication.translate("SpinTVMainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.help_button.setText(QCoreApplication.translate("SpinTVMainWindow", u"HELP", None))
    # retranslateUi

