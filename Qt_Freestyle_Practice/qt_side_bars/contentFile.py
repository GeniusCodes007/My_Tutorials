# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_side_bars_and_drop_downsbfHRZH.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_DropAndSideMainWindow(object):
    def setupUi(self, DropAndSideMainWindow):
        if not DropAndSideMainWindow.objectName():
            DropAndSideMainWindow.setObjectName(u"DropAndSideMainWindow")
        DropAndSideMainWindow.resize(1064, 588)
        icon = QIcon()
        icon.addFile(u"resource_folder_test/WIN_20250404_18_49_12_Pro.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        DropAndSideMainWindow.setWindowIcon(icon)
        DropAndSideMainWindow.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.centralwidget = QWidget(DropAndSideMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 1046, 564))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icons_widget = QWidget(self.layoutWidget)
        self.icons_widget.setObjectName(u"icons_widget")
        self.icons_widget.setMinimumSize(QSize(71, 562))
        self.icons_widget.setMaximumSize(QSize(71, 562))
        self.icons_widget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.layoutWidget1 = QWidget(self.icons_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 11, 47, 547))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.school_logo_1 = QLabel(self.layoutWidget1)
        self.school_logo_1.setObjectName(u"school_logo_1")
        self.school_logo_1.setMinimumSize(QSize(20, 41))
        self.school_logo_1.setMaximumSize(QSize(45, 41))
        self.school_logo_1.setPixmap(QPixmap(u"resource_folder_test/settings.png"))
        self.school_logo_1.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.school_logo_1)

        self.dashboard_icon = QPushButton(self.layoutWidget1)
        self.dashboard_icon.setObjectName(u"dashboard_icon")
        icon1 = QIcon()
        icon1.addFile(u"resource_folder_test/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"resource_folder_test/home2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon1.addFile(u"resource_folder_test/home2.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.dashboard_icon.setIcon(icon1)
        self.dashboard_icon.setCheckable(True)
        self.dashboard_icon.setChecked(False)
        self.dashboard_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_icon)

        self.institution_icon = QPushButton(self.layoutWidget1)
        self.institution_icon.setObjectName(u"institution_icon")
        icon2 = QIcon()
        icon2.addFile(u"resource_folder_test/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u"resource_folder_test/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_icon.setIcon(icon2)
        self.institution_icon.setCheckable(True)
        self.institution_icon.setChecked(False)
        self.institution_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.institution_icon)

        self.student_icon = QPushButton(self.layoutWidget1)
        self.student_icon.setObjectName(u"student_icon")
        self.student_icon.setIcon(icon2)
        self.student_icon.setCheckable(True)
        self.student_icon.setChecked(False)
        self.student_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.student_icon)

        self.teachers_icon = QPushButton(self.layoutWidget1)
        self.teachers_icon.setObjectName(u"teachers_icon")
        self.teachers_icon.setIcon(icon2)
        self.teachers_icon.setCheckable(True)
        self.teachers_icon.setChecked(False)
        self.teachers_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.teachers_icon)

        self.finances_icon = QPushButton(self.layoutWidget1)
        self.finances_icon.setObjectName(u"finances_icon")
        self.finances_icon.setIcon(icon2)
        self.finances_icon.setCheckable(True)
        self.finances_icon.setChecked(False)
        self.finances_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.finances_icon)

        self.verticalSpacer = QSpacerItem(17, 288, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.settings_icon = QPushButton(self.layoutWidget1)
        self.settings_icon.setObjectName(u"settings_icon")
        icon3 = QIcon()
        icon3.addFile(u"resource_folder_test/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_icon.setIcon(icon3)
        self.settings_icon.setCheckable(True)
        self.settings_icon.setChecked(False)
        self.settings_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.settings_icon)

        self.sign_out_icon = QPushButton(self.layoutWidget1)
        self.sign_out_icon.setObjectName(u"sign_out_icon")
        icon4 = QIcon()
        icon4.addFile(u"resource_folder_test/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sign_out_icon.setIcon(icon4)
        self.sign_out_icon.setCheckable(True)
        self.sign_out_icon.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.sign_out_icon)


        self.horizontalLayout.addWidget(self.icons_widget)

        self.text_widget = QWidget(self.layoutWidget)
        self.text_widget.setObjectName(u"text_widget")
        self.text_widget.setMinimumSize(QSize(160, 0))
        self.text_widget.setMaximumSize(QSize(160, 16777215))
        self.text_widget.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"QPshButton\n"
"{\n"
"height: 30px;\n"
"border: none\n"
"}")
        self.layoutWidget2 = QWidget(self.text_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 135, 549))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.school_logo_2 = QLabel(self.layoutWidget2)
        self.school_logo_2.setObjectName(u"school_logo_2")
        self.school_logo_2.setMaximumSize(QSize(49, 41))
        self.school_logo_2.setPixmap(QPixmap(u"resource_folder_test/settings.png"))
        self.school_logo_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.school_logo_2)

        self.school_name_label = QLabel(self.layoutWidget2)
        self.school_name_label.setObjectName(u"school_name_label")
        self.school_name_label.setMaximumSize(QSize(124, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.school_name_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.school_name_label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.dashboard_pushbutton = QPushButton(self.layoutWidget2)
        self.dashboard_pushbutton.setObjectName(u"dashboard_pushbutton")
        self.dashboard_pushbutton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"resource_folder_test/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u"resource_folder_test/home2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_pushbutton.setIcon(icon5)
        self.dashboard_pushbutton.setCheckable(True)
        self.dashboard_pushbutton.setChecked(False)
        self.dashboard_pushbutton.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_pushbutton)

        self.institution_pushButton = QPushButton(self.layoutWidget2)
        self.institution_pushButton.setObjectName(u"institution_pushButton")
        self.institution_pushButton.setIcon(icon2)
        self.institution_pushButton.setCheckable(True)
        self.institution_pushButton.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institution_pushButton)

        self.students_big_frame = QFrame(self.layoutWidget2)
        self.students_big_frame.setObjectName(u"students_big_frame")
        self.students_big_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.students_big_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.students_big_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.studentFrame = QPushButton(self.students_big_frame)
        self.studentFrame.setObjectName(u"studentFrame")
        self.studentFrame.setIcon(icon2)
        self.studentFrame.setCheckable(True)
        self.studentFrame.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.studentFrame)

        self.student_drop_down_frame = QFrame(self.students_big_frame)
        self.student_drop_down_frame.setObjectName(u"student_drop_down_frame")
        self.student_drop_down_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.student_drop_down_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.student_drop_down_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.studentInfo = QPushButton(self.student_drop_down_frame)
        self.studentInfo.setObjectName(u"studentInfo")
        self.studentInfo.setCheckable(True)
        self.studentInfo.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.studentInfo)

        self.studentResult = QPushButton(self.student_drop_down_frame)
        self.studentResult.setObjectName(u"studentResult")
        self.studentResult.setCheckable(True)
        self.studentResult.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.studentResult)

        self.studentPayments = QPushButton(self.student_drop_down_frame)
        self.studentPayments.setObjectName(u"studentPayments")
        self.studentPayments.setCheckable(True)
        self.studentPayments.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.studentPayments)


        self.verticalLayout_5.addWidget(self.student_drop_down_frame)


        self.verticalLayout_7.addWidget(self.students_big_frame)

        self.teachers_big_frame = QFrame(self.layoutWidget2)
        self.teachers_big_frame.setObjectName(u"teachers_big_frame")
        self.teachers_big_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.teachers_big_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.teachers_big_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.teacherFrame = QPushButton(self.teachers_big_frame)
        self.teacherFrame.setObjectName(u"teacherFrame")
        self.teacherFrame.setIcon(icon2)
        self.teacherFrame.setCheckable(True)
        self.teacherFrame.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.teacherFrame)

        self.teacher_drop_down_frame = QFrame(self.teachers_big_frame)
        self.teacher_drop_down_frame.setObjectName(u"teacher_drop_down_frame")
        self.teacher_drop_down_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.teacher_drop_down_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.teacher_drop_down_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.teacherInfo = QPushButton(self.teacher_drop_down_frame)
        self.teacherInfo.setObjectName(u"teacherInfo")
        self.teacherInfo.setCheckable(True)
        self.teacherInfo.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.teacherInfo)

        self.teacherAllowances = QPushButton(self.teacher_drop_down_frame)
        self.teacherAllowances.setObjectName(u"teacherAllowances")
        self.teacherAllowances.setCheckable(True)
        self.teacherAllowances.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.teacherAllowances)

        self.teacherPayments = QPushButton(self.teacher_drop_down_frame)
        self.teacherPayments.setObjectName(u"teacherPayments")
        self.teacherPayments.setCheckable(True)
        self.teacherPayments.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.teacherPayments)


        self.verticalLayout_4.addWidget(self.teacher_drop_down_frame)


        self.verticalLayout_7.addWidget(self.teachers_big_frame)

        self.finanaces_big_frame = QFrame(self.layoutWidget2)
        self.finanaces_big_frame.setObjectName(u"finanaces_big_frame")
        self.finanaces_big_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.finanaces_big_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finanaces_big_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.financesFrame = QPushButton(self.finanaces_big_frame)
        self.financesFrame.setObjectName(u"financesFrame")
        self.financesFrame.setIcon(icon2)
        self.financesFrame.setCheckable(True)
        self.financesFrame.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.financesFrame)

        self.finanace_drop_down_frame = QFrame(self.finanaces_big_frame)
        self.finanace_drop_down_frame.setObjectName(u"finanace_drop_down_frame")
        self.finanace_drop_down_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.finanace_drop_down_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.finanace_drop_down_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.budgets = QPushButton(self.finanace_drop_down_frame)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setCheckable(True)
        self.budgets.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.budgets)

        self.expenses = QPushButton(self.finanace_drop_down_frame)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setCheckable(True)
        self.expenses.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.expenses)

        self.income = QPushButton(self.finanace_drop_down_frame)
        self.income.setObjectName(u"income")
        self.income.setCheckable(True)
        self.income.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.income)


        self.verticalLayout_6.addWidget(self.finanace_drop_down_frame)


        self.verticalLayout_7.addWidget(self.finanaces_big_frame)

        self.settings = QPushButton(self.layoutWidget2)
        self.settings.setObjectName(u"settings")
        self.settings.setIcon(icon3)
        self.settings.setCheckable(True)
        self.settings.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.settings)

        self.sign_out_2 = QPushButton(self.layoutWidget2)
        self.sign_out_2.setObjectName(u"sign_out_2")
        self.sign_out_2.setIcon(icon4)
        self.sign_out_2.setCheckable(True)
        self.sign_out_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.sign_out_2)


        self.horizontalLayout.addWidget(self.text_widget)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMaximumSize(QSize(16777215, 72))
        self.header_widget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(46, 51))
        icon6 = QIcon()
        icon6.addFile(u"resource_folder_test/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(34, 100))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Shape.WinPanel)

        self.verticalLayout_12.addWidget(self.label)

        self.label_2 = QLabel(self.header_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.WinPanel)

        self.verticalLayout_12.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(241, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(241, 31))
        self.lineEdit.setMaximumSize(QSize(270, 31))
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.header_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(71, 41))
        self.label_3.setMaximumSize(QSize(71, 41))
        self.label_3.setPixmap(QPixmap(u"resource_folder_test/WIN_20250916_23_49_46_Pro.jpg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_13.addWidget(self.header_widget)

        self.main_display_widget = QWidget(self.layoutWidget)
        self.main_display_widget.setObjectName(u"main_display_widget")
        self.main_display_widget.setMinimumSize(QSize(0, 0))
        self.main_display_widget.setMaximumSize(QSize(16777215, 16777215))
        self.main_display_widget.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.verticalLayout_14 = QVBoxLayout(self.main_display_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget = QStackedWidget(self.main_display_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(773, 463))
        font2 = QFont()
        font2.setPointSize(25)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setFrameShape(QFrame.Shape.WinPanel)
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_4 = QLabel(self.dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 110, 181, 111))
        self.label_4.setFont(font2)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.institution_page = QWidget()
        self.institution_page.setObjectName(u"institution_page")
        self.label_5 = QLabel(self.institution_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 170, 181, 111))
        self.label_5.setFont(font2)
        self.stackedWidget.addWidget(self.institution_page)
        self.studentInfo_page = QWidget()
        self.studentInfo_page.setObjectName(u"studentInfo_page")
        self.label_6 = QLabel(self.studentInfo_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 170, 181, 111))
        self.label_6.setFont(font2)
        self.stackedWidget.addWidget(self.studentInfo_page)
        self.studentInfo_page1 = QWidget()
        self.studentInfo_page1.setObjectName(u"studentInfo_page1")
        self.label_7 = QLabel(self.studentInfo_page1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 220, 261, 111))
        self.label_7.setFont(font2)
        self.stackedWidget.addWidget(self.studentInfo_page1)
        self.studentPayments_page = QWidget()
        self.studentPayments_page.setObjectName(u"studentPayments_page")
        self.label_8 = QLabel(self.studentPayments_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, 170, 291, 111))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.studentPayments_page)
        self.teacherInfo_page = QWidget()
        self.teacherInfo_page.setObjectName(u"teacherInfo_page")
        self.label_9 = QLabel(self.teacherInfo_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 160, 181, 111))
        self.label_9.setFont(font2)
        self.stackedWidget.addWidget(self.teacherInfo_page)
        self.teacherAllowances_page = QWidget()
        self.teacherAllowances_page.setObjectName(u"teacherAllowances_page")
        self.label_10 = QLabel(self.teacherAllowances_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(210, 160, 351, 121))
        self.label_10.setFont(font2)
        self.stackedWidget.addWidget(self.teacherAllowances_page)
        self.teacherPayments_page = QWidget()
        self.teacherPayments_page.setObjectName(u"teacherPayments_page")
        self.label_11 = QLabel(self.teacherPayments_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 160, 291, 111))
        self.label_11.setFont(font2)
        self.stackedWidget.addWidget(self.teacherPayments_page)
        self.budgets_page = QWidget()
        self.budgets_page.setObjectName(u"budgets_page")
        self.label_12 = QLabel(self.budgets_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(290, 180, 271, 111))
        self.label_12.setFont(font2)
        self.stackedWidget.addWidget(self.budgets_page)
        self.expenses_page = QWidget()
        self.expenses_page.setObjectName(u"expenses_page")
        self.label_13 = QLabel(self.expenses_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(310, 120, 181, 111))
        self.label_13.setFont(font2)
        self.stackedWidget.addWidget(self.expenses_page)
        self.income_page = QWidget()
        self.income_page.setObjectName(u"income_page")
        self.label_14 = QLabel(self.income_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 150, 181, 111))
        self.label_14.setFont(font2)
        self.stackedWidget.addWidget(self.income_page)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_15 = QLabel(self.page_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(360, 140, 181, 111))
        self.label_15.setMinimumSize(QSize(181, 111))
        self.label_15.setFont(font2)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_13.addWidget(self.main_display_widget)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        DropAndSideMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DropAndSideMainWindow)
        self.studentFrame.toggled.connect(self.student_drop_down_frame.setHidden)
        self.pushButton.toggled.connect(self.text_widget.hide)
        self.sign_out_2.toggled.connect(self.sign_out_icon.setChecked)
        self.teacherFrame.toggled.connect(self.teachers_icon.setChecked)
        self.sign_out_2.toggled.connect(DropAndSideMainWindow.close)
        self.settings.toggled.connect(self.settings_icon.setChecked)
        self.financesFrame.toggled.connect(self.finanace_drop_down_frame.setHidden)
        self.sign_out_icon.toggled.connect(DropAndSideMainWindow.close)
        self.financesFrame.toggled.connect(self.finances_icon.setChecked)
        self.institution_pushButton.toggled.connect(self.institution_icon.setChecked)
        self.pushButton.toggled.connect(self.text_widget.setVisible)
        self.teacherFrame.toggled.connect(self.teacher_drop_down_frame.setHidden)
        self.studentFrame.toggled.connect(self.student_icon.setChecked)
        self.dashboard_pushbutton.toggled.connect(self.dashboard_icon.setChecked)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(DropAndSideMainWindow)
    # setupUi

    def retranslateUi(self, DropAndSideMainWindow):
        DropAndSideMainWindow.setWindowTitle(QCoreApplication.translate("DropAndSideMainWindow", u"MainWindow", None))
        self.school_logo_1.setText("")
        self.dashboard_icon.setText("")
        self.institution_icon.setText("")
        self.student_icon.setText("")
        self.teachers_icon.setText("")
        self.finances_icon.setText("")
        self.settings_icon.setText("")
        self.sign_out_icon.setText("")
        self.school_logo_2.setText("")
        self.school_name_label.setText(QCoreApplication.translate("DropAndSideMainWindow", u"SCHOOL", None))
        self.dashboard_pushbutton.setText(QCoreApplication.translate("DropAndSideMainWindow", u"   DASHBOARD", None))
        self.institution_pushButton.setText(QCoreApplication.translate("DropAndSideMainWindow", u"   INSTITUTION", None))
        self.studentFrame.setText(QCoreApplication.translate("DropAndSideMainWindow", u"   STUDENTS", None))
        self.studentInfo.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Info", None))
        self.studentResult.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Result", None))
        self.studentPayments.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Payments", None))
        self.teacherFrame.setText(QCoreApplication.translate("DropAndSideMainWindow", u"  TEACHERS", None))
        self.teacherInfo.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Info", None))
        self.teacherAllowances.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Allowances", None))
        self.teacherPayments.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Payments", None))
        self.financesFrame.setText(QCoreApplication.translate("DropAndSideMainWindow", u"  FINANCES", None))
        self.budgets.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Expenses", None))
        self.income.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Income", None))
        self.settings.setText(QCoreApplication.translate("DropAndSideMainWindow", u"  SETTINGS", None))
        self.sign_out_2.setText(QCoreApplication.translate("DropAndSideMainWindow", u"  SIGN OUT", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Welcome Student", None))
        self.label_2.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DropAndSideMainWindow", u"Search...", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Institution", None))
        self.label_6.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Info", None))
        self.label_7.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Result", None))
        self.label_8.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Student Payments", None))
        self.label_9.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Info", None))
        self.label_10.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Allowances", None))
        self.label_11.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Teacher Payments", None))
        self.label_12.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Budgets", None))
        self.label_13.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Expenses", None))
        self.label_14.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Income", None))
        self.label_15.setText(QCoreApplication.translate("DropAndSideMainWindow", u"Settings", None))
    # retranslateUi

