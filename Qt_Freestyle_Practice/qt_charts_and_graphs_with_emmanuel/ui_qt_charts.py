# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_chartsEjlMGP.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import qtChartIcons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 600)
        icon = QIcon()
        icon.addFile(u":/myIcons/chart_icons/line_graph_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(147, 147, 147);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainInputFrame = QFrame(self.centralwidget)
        self.mainInputFrame.setObjectName(u"mainInputFrame")
        self.mainInputFrame.setMinimumSize(QSize(220, 561))
        self.mainInputFrame.setMaximumSize(QSize(250, 16777215))
        self.mainInputFrame.setStyleSheet(u"QPushButton{\n"
"background-color: #6d6d6d;\n"
"color: black;\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"background-color: #6d6d6d;\n"
"color: black;\n"
"border-radius: 30px;\n"
"}")
        self.mainInputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainInputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainInputFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacerAbove = QSpacerItem(20, 127, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacerAbove)

        self.subInputFrame = QFrame(self.mainInputFrame)
        self.subInputFrame.setObjectName(u"subInputFrame")
        self.subInputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subInputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.subInputFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inputLabelsFrame = QFrame(self.subInputFrame)
        self.inputLabelsFrame.setObjectName(u"inputLabelsFrame")
        self.inputLabelsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.inputLabelsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.inputLabelsFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pythonLabel = QLabel(self.inputLabelsFrame)
        self.pythonLabel.setObjectName(u"pythonLabel")
        font = QFont()
        font.setBold(True)
        self.pythonLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.pythonLabel)

        self.cppLabel = QLabel(self.inputLabelsFrame)
        self.cppLabel.setObjectName(u"cppLabel")
        self.cppLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.cppLabel)

        self.javaLabel = QLabel(self.inputLabelsFrame)
        self.javaLabel.setObjectName(u"javaLabel")
        self.javaLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.javaLabel)

        self.javaScriptLabel = QLabel(self.inputLabelsFrame)
        self.javaScriptLabel.setObjectName(u"javaScriptLabel")
        self.javaScriptLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.javaScriptLabel)

        self.kotlinLabel = QLabel(self.inputLabelsFrame)
        self.kotlinLabel.setObjectName(u"kotlinLabel")
        self.kotlinLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.kotlinLabel)

        self.phpLabel = QLabel(self.inputLabelsFrame)
        self.phpLabel.setObjectName(u"phpLabel")
        self.phpLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.phpLabel)

        self.cshLabel = QLabel(self.inputLabelsFrame)
        self.cshLabel.setObjectName(u"cshLabel")
        self.cshLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.cshLabel)

        self.htmlLabel = QLabel(self.inputLabelsFrame)
        self.htmlLabel.setObjectName(u"htmlLabel")
        self.htmlLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.htmlLabel)


        self.horizontalLayout_3.addWidget(self.inputLabelsFrame)

        self.inputLineEditFrame = QFrame(self.subInputFrame)
        self.inputLineEditFrame.setObjectName(u"inputLineEditFrame")
        self.inputLineEditFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.inputLineEditFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.inputLineEditFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pythonLineEdit = QLineEdit(self.inputLineEditFrame)
        self.pythonLineEdit.setObjectName(u"pythonLineEdit")
        self.pythonLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.pythonLineEdit)

        self.cppLineEdit = QLineEdit(self.inputLineEditFrame)
        self.cppLineEdit.setObjectName(u"cppLineEdit")
        self.cppLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.cppLineEdit)

        self.javaLineEdit = QLineEdit(self.inputLineEditFrame)
        self.javaLineEdit.setObjectName(u"javaLineEdit")
        self.javaLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.javaLineEdit)

        self.javaScriptLineEdit = QLineEdit(self.inputLineEditFrame)
        self.javaScriptLineEdit.setObjectName(u"javaScriptLineEdit")
        self.javaScriptLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.javaScriptLineEdit)

        self.kotlinLineEdit = QLineEdit(self.inputLineEditFrame)
        self.kotlinLineEdit.setObjectName(u"kotlinLineEdit")
        self.kotlinLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.kotlinLineEdit)

        self.phpLineEdit = QLineEdit(self.inputLineEditFrame)
        self.phpLineEdit.setObjectName(u"phpLineEdit")
        self.phpLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.phpLineEdit)

        self.cshLineEdit = QLineEdit(self.inputLineEditFrame)
        self.cshLineEdit.setObjectName(u"cshLineEdit")
        self.cshLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.cshLineEdit)

        self.htmlLineEdit = QLineEdit(self.inputLineEditFrame)
        self.htmlLineEdit.setObjectName(u"htmlLineEdit")
        self.htmlLineEdit.setMaximumSize(QSize(115, 18))

        self.verticalLayout_6.addWidget(self.htmlLineEdit)


        self.horizontalLayout_3.addWidget(self.inputLineEditFrame)


        self.verticalLayout_7.addWidget(self.subInputFrame)

        self.updatePushButton = QPushButton(self.mainInputFrame)
        self.updatePushButton.setObjectName(u"updatePushButton")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.updatePushButton.setFont(font1)
        self.updatePushButton.setStyleSheet(u"QPushButton{\n"
"background-color: #6d6d6d;\n"
"color: black;\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout_7.addWidget(self.updatePushButton)

        self.verticalSpacerBelow = QSpacerItem(20, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacerBelow)


        self.horizontalLayout.addWidget(self.mainInputFrame)

        self.mainDisplayFrame = QFrame(self.centralwidget)
        self.mainDisplayFrame.setObjectName(u"mainDisplayFrame")
        font2 = QFont()
        font2.setBold(False)
        self.mainDisplayFrame.setFont(font2)
        self.mainDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainDisplayFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.appInfoFrame = QFrame(self.mainDisplayFrame)
        self.appInfoFrame.setObjectName(u"appInfoFrame")
        self.appInfoFrame.setMinimumSize(QSize(541, 140))
        self.appInfoFrame.setMaximumSize(QSize(16777215, 140))
        self.appInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.appInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.appInfoFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.descriptionFrame = QFrame(self.appInfoFrame)
        self.descriptionFrame.setObjectName(u"descriptionFrame")
        self.descriptionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.descriptionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.descriptionFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainDescriptionLabel = QLabel(self.descriptionFrame)
        self.mainDescriptionLabel.setObjectName(u"mainDescriptionLabel")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.mainDescriptionLabel.setFont(font3)
        self.mainDescriptionLabel.setIndent(60)

        self.verticalLayout.addWidget(self.mainDescriptionLabel)

        self.subDescriptionLabel = QLabel(self.descriptionFrame)
        self.subDescriptionLabel.setObjectName(u"subDescriptionLabel")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.subDescriptionLabel.setFont(font4)
        self.subDescriptionLabel.setMargin(0)
        self.subDescriptionLabel.setIndent(11)

        self.verticalLayout.addWidget(self.subDescriptionLabel)


        self.verticalLayout_2.addWidget(self.descriptionFrame)

        self.chartSelectionFrame = QFrame(self.appInfoFrame)
        self.chartSelectionFrame.setObjectName(u"chartSelectionFrame")
        self.chartSelectionFrame.setStyleSheet(u"QPushButton{\n"
"background-color: #6d6d6d;\n"
"color: black;\n"
"border-radius: 10px;\n"
"}")
        self.chartSelectionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chartSelectionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.chartSelectionFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pieChartPushButton = QPushButton(self.chartSelectionFrame)
        self.pieChartPushButton.setObjectName(u"pieChartPushButton")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.pieChartPushButton.setFont(font5)
        icon1 = QIcon()
        icon1.addFile(u":/myIcons/chart_icons/pie_chart_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/myIcons/chart_icons/pie_chart_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pieChartPushButton.setIcon(icon1)
        self.pieChartPushButton.setIconSize(QSize(22, 25))
        self.pieChartPushButton.setCheckable(True)
        self.pieChartPushButton.setChecked(False)
        self.pieChartPushButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pieChartPushButton)

        self.lineGraphPushButton = QPushButton(self.chartSelectionFrame)
        self.lineGraphPushButton.setObjectName(u"lineGraphPushButton")
        self.lineGraphPushButton.setFont(font5)
        icon2 = QIcon()
        icon2.addFile(u":/myIcons/chart_icons/line_graph_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/myIcons/chart_icons/line_graph_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.lineGraphPushButton.setIcon(icon2)
        self.lineGraphPushButton.setIconSize(QSize(22, 25))
        self.lineGraphPushButton.setCheckable(True)
        self.lineGraphPushButton.setChecked(False)
        self.lineGraphPushButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.lineGraphPushButton)

        self.barChartPushButton = QPushButton(self.chartSelectionFrame)
        self.barChartPushButton.setObjectName(u"barChartPushButton")
        self.barChartPushButton.setFont(font5)
        icon3 = QIcon()
        icon3.addFile(u":/myIcons/chart_icons/bar_chart_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/myIcons/chart_icons/bar_chart_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.barChartPushButton.setIcon(icon3)
        self.barChartPushButton.setIconSize(QSize(22, 25))
        self.barChartPushButton.setCheckable(True)
        self.barChartPushButton.setChecked(False)
        self.barChartPushButton.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.barChartPushButton)


        self.verticalLayout_2.addWidget(self.chartSelectionFrame)


        self.verticalLayout_3.addWidget(self.appInfoFrame)

        self.chartDisplayFrame = QFrame(self.mainDisplayFrame)
        self.chartDisplayFrame.setObjectName(u"chartDisplayFrame")
        self.chartDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chartDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.chartDisplayFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.chartDisplayFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pieChartPage = QWidget()
        self.pieChartPage.setObjectName(u"pieChartPage")
        self.verticalLayout_8 = QVBoxLayout(self.pieChartPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pieChartLabel = QLabel(self.pieChartPage)
        self.pieChartLabel.setObjectName(u"pieChartLabel")
        self.pieChartLabel.setFont(font5)
        self.pieChartLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.pieChartLabel.setIndent(200)

        self.verticalLayout_8.addWidget(self.pieChartLabel)

        self.pieChartGraphicsView = QChartView(self.pieChartPage)
        self.pieChartGraphicsView.setObjectName(u"pieChartGraphicsView")
        self.pieChartGraphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.pieChartGraphicsView)

        self.stackedWidget.addWidget(self.pieChartPage)
        self.lineGraphicsPage = QWidget()
        self.lineGraphicsPage.setObjectName(u"lineGraphicsPage")
        self.verticalLayout_9 = QVBoxLayout(self.lineGraphicsPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineGraphLabel = QLabel(self.lineGraphicsPage)
        self.lineGraphLabel.setObjectName(u"lineGraphLabel")
        self.lineGraphLabel.setFont(font5)
        self.lineGraphLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.lineGraphLabel.setIndent(200)

        self.verticalLayout_9.addWidget(self.lineGraphLabel)

        self.lineGraphGraphicsView = QChartView(self.lineGraphicsPage)
        self.lineGraphGraphicsView.setObjectName(u"lineGraphGraphicsView")
        self.lineGraphGraphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.lineGraphGraphicsView)

        self.stackedWidget.addWidget(self.lineGraphicsPage)
        self.barChartPage = QWidget()
        self.barChartPage.setObjectName(u"barChartPage")
        self.verticalLayout_10 = QVBoxLayout(self.barChartPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.barChartLabel = QLabel(self.barChartPage)
        self.barChartLabel.setObjectName(u"barChartLabel")
        self.barChartLabel.setFont(font5)
        self.barChartLabel.setFrameShape(QFrame.Shape.WinPanel)
        self.barChartLabel.setIndent(200)

        self.verticalLayout_10.addWidget(self.barChartLabel)

        self.barChartGraphicsView = QChartView(self.barChartPage)
        self.barChartGraphicsView.setObjectName(u"barChartGraphicsView")
        self.barChartGraphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.barChartGraphicsView)

        self.stackedWidget.addWidget(self.barChartPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.chartDisplayFrame)


        self.horizontalLayout.addWidget(self.mainDisplayFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pythonLabel.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.cppLabel.setText(QCoreApplication.translate("MainWindow", u"C++", None))
        self.javaLabel.setText(QCoreApplication.translate("MainWindow", u"JAVA", None))
        self.javaScriptLabel.setText(QCoreApplication.translate("MainWindow", u"JAVASCRIPT", None))
        self.kotlinLabel.setText(QCoreApplication.translate("MainWindow", u"KOTLIN", None))
        self.phpLabel.setText(QCoreApplication.translate("MainWindow", u"PHP", None))
        self.cshLabel.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.htmlLabel.setText(QCoreApplication.translate("MainWindow", u"HTML", None))
        self.pythonLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cppLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.javaLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.javaScriptLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.kotlinLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.phpLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cshLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.htmlLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.updatePushButton.setText(QCoreApplication.translate("MainWindow", u"Update Chart", None))
        self.mainDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"The Most Popular Programming Languages In The World", None))
        self.subDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"A Representation of The Most Popular Programming Languages in Pie Chart, Line Graph and Bar Chart Presentations.", None))
        self.pieChartPushButton.setText(QCoreApplication.translate("MainWindow", u"Pie Chart", None))
        self.lineGraphPushButton.setText(QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.barChartPushButton.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.pieChartLabel.setText(QCoreApplication.translate("MainWindow", u"Pie Chart ", None))
        self.lineGraphLabel.setText(QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.barChartLabel.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
    # retranslateUi

