# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtChartWindowDTdJfp.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
from chartsAndGraphsQtFiles import qtChartIcons_rc

class Ui_QtChartWindow(object):
    def setupUi(self, QtChartWindow):
        if not QtChartWindow.objectName():
            QtChartWindow.setObjectName(u"QtChartWindow")
        QtChartWindow.resize(959, 514)
        QtChartWindow.setStyleSheet(u"background-color: rgb(0, 141, 201);")
        self.chartAndGraphsCentralWidget = QWidget(QtChartWindow)
        self.chartAndGraphsCentralWidget.setObjectName(u"chartAndGraphsCentralWidget")
        self.horizontalLayout = QHBoxLayout(self.chartAndGraphsCentralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuWidget = QWidget(self.chartAndGraphsCentralWidget)
        self.leftMenuWidget.setObjectName(u"leftMenuWidget")
        self.verticalLayout = QVBoxLayout(self.leftMenuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectNameFrame = QFrame(self.leftMenuWidget)
        self.projectNameFrame.setObjectName(u"projectNameFrame")
        self.projectNameFrame.setMaximumSize(QSize(16777215, 68))
        self.projectNameFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.projectNameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.projectNameFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.projectIconLabel = QLabel(self.projectNameFrame)
        self.projectIconLabel.setObjectName(u"projectIconLabel")
        self.projectIconLabel.setMaximumSize(QSize(39, 39))
        self.projectIconLabel.setStyleSheet(u"background-color: rgb(103, 103, 103);")
        self.projectIconLabel.setPixmap(QPixmap(u":/newPrefix/chartsAndGraphs/qt_chart.png"))
        self.projectIconLabel.setScaledContents(True)
        self.projectIconLabel.setMargin(3)
        self.projectIconLabel.setIndent(-1)

        self.horizontalLayout_2.addWidget(self.projectIconLabel)

        self.projectNameLabel = QLabel(self.projectNameFrame)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        self.projectNameLabel.setMinimumSize(QSize(121, 39))
        self.projectNameLabel.setMaximumSize(QSize(121, 39))
        font = QFont()
        font.setBold(True)
        self.projectNameLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.projectNameLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.projectNameFrame)

        self.pushButtonsFrame = QFrame(self.leftMenuWidget)
        self.pushButtonsFrame.setObjectName(u"pushButtonsFrame")
        self.pushButtonsFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.pushButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.pushButtonsFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.percentageBarPushButton = QPushButton(self.pushButtonsFrame)
        self.percentageBarPushButton.setObjectName(u"percentageBarPushButton")
        self.percentageBarPushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/chartsAndGraphs/percentage_bar_chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.percentageBarPushButton.setIcon(icon)
        self.percentageBarPushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.percentageBarPushButton)

        self.temperaturePushButton = QPushButton(self.pushButtonsFrame)
        self.temperaturePushButton.setObjectName(u"temperaturePushButton")
        self.temperaturePushButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/chartsAndGraphs/temperature.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperaturePushButton.setIcon(icon1)
        self.temperaturePushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.temperaturePushButton)

        self.nestedDonutsPushButton = QPushButton(self.pushButtonsFrame)
        self.nestedDonutsPushButton.setObjectName(u"nestedDonutsPushButton")
        self.nestedDonutsPushButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/chartsAndGraphs/nested_donut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nestedDonutsPushButton.setIcon(icon2)
        self.nestedDonutsPushButton.setIconSize(QSize(23, 23))

        self.verticalLayout_2.addWidget(self.nestedDonutsPushButton)

        self.lineChartsPushButton = QPushButton(self.pushButtonsFrame)
        self.lineChartsPushButton.setObjectName(u"lineChartsPushButton")
        self.lineChartsPushButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/chartsAndGraphs/line_chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lineChartsPushButton.setIcon(icon3)
        self.lineChartsPushButton.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.lineChartsPushButton)

        self.barChartPushButton = QPushButton(self.pushButtonsFrame)
        self.barChartPushButton.setObjectName(u"barChartPushButton")
        self.barChartPushButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/chartsAndGraphs/bar_charts.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.barChartPushButton.setIcon(icon4)
        self.barChartPushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.barChartPushButton)


        self.verticalLayout.addWidget(self.pushButtonsFrame)

        self.supportFrame = QFrame(self.leftMenuWidget)
        self.supportFrame.setObjectName(u"supportFrame")
        self.supportFrame.setMaximumSize(QSize(16777215, 70))
        self.supportFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.supportFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.supportFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.supportIconLabel = QLabel(self.supportFrame)
        self.supportIconLabel.setObjectName(u"supportIconLabel")
        self.supportIconLabel.setMaximumSize(QSize(35, 35))
        self.supportIconLabel.setPixmap(QPixmap(u":/newPrefix/chartsAndGraphs/support.png"))
        self.supportIconLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.supportIconLabel)

        self.supportLabel = QLabel(self.supportFrame)
        self.supportLabel.setObjectName(u"supportLabel")
        self.supportLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.supportLabel)


        self.verticalLayout.addWidget(self.supportFrame)

        self.additionalFrame = QFrame(self.leftMenuWidget)
        self.additionalFrame.setObjectName(u"additionalFrame")
        self.additionalFrame.setMaximumSize(QSize(16777215, 150))
        self.additionalFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.additionalFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.additionalFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.patreonIconLabel = QLabel(self.additionalFrame)
        self.patreonIconLabel.setObjectName(u"patreonIconLabel")
        self.patreonIconLabel.setMaximumSize(QSize(40, 35))
        self.patreonIconLabel.setPixmap(QPixmap(u":/newPrefix/chartsAndGraphs/patreon.png"))
        self.patreonIconLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.patreonIconLabel, 0, 0, 1, 1)

        self.subscribeIconLabel = QLabel(self.additionalFrame)
        self.subscribeIconLabel.setObjectName(u"subscribeIconLabel")
        self.subscribeIconLabel.setMaximumSize(QSize(40, 35))
        self.subscribeIconLabel.setPixmap(QPixmap(u":/newPrefix/chartsAndGraphs/subcribe.png"))
        self.subscribeIconLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.subscribeIconLabel, 1, 0, 1, 1)

        self.payPalIconLabel = QLabel(self.additionalFrame)
        self.payPalIconLabel.setObjectName(u"payPalIconLabel")
        self.payPalIconLabel.setMaximumSize(QSize(40, 35))
        self.payPalIconLabel.setPixmap(QPixmap(u":/newPrefix/chartsAndGraphs/images.png"))
        self.payPalIconLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.payPalIconLabel, 2, 0, 1, 1)

        self.patreonPushButton = QPushButton(self.additionalFrame)
        self.patreonPushButton.setObjectName(u"patreonPushButton")
        self.patreonPushButton.setFont(font)

        self.gridLayout.addWidget(self.patreonPushButton, 0, 1, 1, 1)

        self.subcribePushButton = QPushButton(self.additionalFrame)
        self.subcribePushButton.setObjectName(u"subcribePushButton")
        self.subcribePushButton.setFont(font)

        self.gridLayout.addWidget(self.subcribePushButton, 1, 1, 1, 1)

        self.payPalPushButton = QPushButton(self.additionalFrame)
        self.payPalPushButton.setObjectName(u"payPalPushButton")
        self.payPalPushButton.setFont(font)

        self.gridLayout.addWidget(self.payPalPushButton, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.additionalFrame)


        self.horizontalLayout.addWidget(self.leftMenuWidget)

        self.displayFrame = QFrame(self.chartAndGraphsCentralWidget)
        self.displayFrame.setObjectName(u"displayFrame")
        self.displayFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.displayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.displayFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.headerFrame = QFrame(self.displayFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(734, 68))
        self.headerFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuFrame = QFrame(self.headerFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.menuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menuFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.menuIconPushButton = QPushButton(self.menuFrame)
        self.menuIconPushButton.setObjectName(u"menuIconPushButton")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/chartsAndGraphs/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuIconPushButton.setIcon(icon5)
        self.menuIconPushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.menuIconPushButton)

        self.menuLabel = QLabel(self.menuFrame)
        self.menuLabel.setObjectName(u"menuLabel")
        self.menuLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.menuLabel)


        self.horizontalLayout_4.addWidget(self.menuFrame)

        self.dashBoardFrame = QFrame(self.headerFrame)
        self.dashBoardFrame.setObjectName(u"dashBoardFrame")
        self.dashBoardFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.dashBoardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dashBoardFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dashBoardLabel = QLabel(self.dashBoardFrame)
        self.dashBoardLabel.setObjectName(u"dashBoardLabel")
        self.dashBoardLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.dashBoardLabel)


        self.horizontalLayout_4.addWidget(self.dashBoardFrame)

        self.windowActionFrame = QFrame(self.headerFrame)
        self.windowActionFrame.setObjectName(u"windowActionFrame")
        self.windowActionFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.windowActionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.windowActionFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.minimiseIconPushButton = QPushButton(self.windowActionFrame)
        self.minimiseIconPushButton.setObjectName(u"minimiseIconPushButton")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/chartsAndGraphs/minimise.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimiseIconPushButton.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.minimiseIconPushButton)

        self.restoreIconPushButton = QPushButton(self.windowActionFrame)
        self.restoreIconPushButton.setObjectName(u"restoreIconPushButton")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/chartsAndGraphs/maximise.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreIconPushButton.setIcon(icon7)

        self.horizontalLayout_6.addWidget(self.restoreIconPushButton)

        self.closeIconPushButton = QPushButton(self.windowActionFrame)
        self.closeIconPushButton.setObjectName(u"closeIconPushButton")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/chartsAndGraphs/close_or_cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeIconPushButton.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.closeIconPushButton)


        self.horizontalLayout_4.addWidget(self.windowActionFrame)


        self.verticalLayout_4.addWidget(self.headerFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.mainDisplayFrame = QFrame(self.displayFrame)
        self.mainDisplayFrame.setObjectName(u"mainDisplayFrame")
        self.mainDisplayFrame.setStyleSheet(u"")
        self.mainDisplayFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.mainDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainDisplayFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.mainDisplayFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Shape.WinPanel)
        self.stackedWidget.setLineWidth(0)
        self.percentageBarChartPage = QWidget()
        self.percentageBarChartPage.setObjectName(u"percentageBarChartPage")
        self.verticalLayout_9 = QVBoxLayout(self.percentageBarChartPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.percentageBarFrame = QFrame(self.percentageBarChartPage)
        self.percentageBarFrame.setObjectName(u"percentageBarFrame")
        self.percentageBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.percentageBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.percentageBarFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.percentageBarLabel = QLabel(self.percentageBarFrame)
        self.percentageBarLabel.setObjectName(u"percentageBarLabel")
        self.percentageBarLabel.setFont(font)
        self.percentageBarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.percentageBarLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.percentageBarFrame)

        self.percentageBarDisplayFrame = QFrame(self.percentageBarChartPage)
        self.percentageBarDisplayFrame.setObjectName(u"percentageBarDisplayFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentageBarDisplayFrame.sizePolicy().hasHeightForWidth())
        self.percentageBarDisplayFrame.setSizePolicy(sizePolicy)
        self.percentageBarDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.percentageBarDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.percentageBarDisplayFrame)

        self.stackedWidget.addWidget(self.percentageBarChartPage)
        self.temperatureChartPage = QWidget()
        self.temperatureChartPage.setObjectName(u"temperatureChartPage")
        self.verticalLayout_11 = QVBoxLayout(self.temperatureChartPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.temperatureChartFrame = QFrame(self.temperatureChartPage)
        self.temperatureChartFrame.setObjectName(u"temperatureChartFrame")
        self.temperatureChartFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.temperatureChartFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.temperatureChartFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.temperatureChartLabel = QLabel(self.temperatureChartFrame)
        self.temperatureChartLabel.setObjectName(u"temperatureChartLabel")
        self.temperatureChartLabel.setFont(font)
        self.temperatureChartLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.temperatureChartLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_11.addWidget(self.temperatureChartFrame)

        self.temperatureDisplayFrame = QFrame(self.temperatureChartPage)
        self.temperatureDisplayFrame.setObjectName(u"temperatureDisplayFrame")
        sizePolicy.setHeightForWidth(self.temperatureDisplayFrame.sizePolicy().hasHeightForWidth())
        self.temperatureDisplayFrame.setSizePolicy(sizePolicy)
        self.temperatureDisplayFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.temperatureDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.temperatureDisplayFrame)

        self.stackedWidget.addWidget(self.temperatureChartPage)
        self.barChartPage = QWidget()
        self.barChartPage.setObjectName(u"barChartPage")
        self.verticalLayout_17 = QVBoxLayout(self.barChartPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_23 = QFrame(self.barChartPage)
        self.frame_23.setObjectName(u"frame_23")
        font1 = QFont()
        font1.setBold(False)
        self.frame_23.setFont(font1)
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_23)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.barChartPage)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_17.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.barChartPage)
        self.nestedDonutsPage = QWidget()
        self.nestedDonutsPage.setObjectName(u"nestedDonutsPage")
        self.verticalLayout_13 = QVBoxLayout(self.nestedDonutsPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.nestedDonutsFrame = QFrame(self.nestedDonutsPage)
        self.nestedDonutsFrame.setObjectName(u"nestedDonutsFrame")
        self.nestedDonutsFrame.setFont(font1)
        self.nestedDonutsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.nestedDonutsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.nestedDonutsFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.nestedDonutsLabel = QLabel(self.nestedDonutsFrame)
        self.nestedDonutsLabel.setObjectName(u"nestedDonutsLabel")
        self.nestedDonutsLabel.setFont(font)
        self.nestedDonutsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.nestedDonutsLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_13.addWidget(self.nestedDonutsFrame)

        self.nestedDonutsDisplayFrame = QFrame(self.nestedDonutsPage)
        self.nestedDonutsDisplayFrame.setObjectName(u"nestedDonutsDisplayFrame")
        sizePolicy.setHeightForWidth(self.nestedDonutsDisplayFrame.sizePolicy().hasHeightForWidth())
        self.nestedDonutsDisplayFrame.setSizePolicy(sizePolicy)
        self.nestedDonutsDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.nestedDonutsDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_13.addWidget(self.nestedDonutsDisplayFrame)

        self.stackedWidget.addWidget(self.nestedDonutsPage)
        self.lineChartPage = QWidget()
        self.lineChartPage.setObjectName(u"lineChartPage")
        self.verticalLayout_15 = QVBoxLayout(self.lineChartPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineChartFrame = QFrame(self.lineChartPage)
        self.lineChartFrame.setObjectName(u"lineChartFrame")
        self.lineChartFrame.setFont(font1)
        self.lineChartFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lineChartFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.lineChartFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lineChartLabel = QLabel(self.lineChartFrame)
        self.lineChartLabel.setObjectName(u"lineChartLabel")
        self.lineChartLabel.setFont(font)
        self.lineChartLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.lineChartLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_15.addWidget(self.lineChartFrame)

        self.lineChartDisplayFrame = QFrame(self.lineChartPage)
        self.lineChartDisplayFrame.setObjectName(u"lineChartDisplayFrame")
        sizePolicy.setHeightForWidth(self.lineChartDisplayFrame.sizePolicy().hasHeightForWidth())
        self.lineChartDisplayFrame.setSizePolicy(sizePolicy)
        self.lineChartDisplayFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.lineChartDisplayFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_15.addWidget(self.lineChartDisplayFrame)

        self.stackedWidget.addWidget(self.lineChartPage)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.mainDisplayFrame)

        self.copyRightFrame = QFrame(self.displayFrame)
        self.copyRightFrame.setObjectName(u"copyRightFrame")
        self.copyRightFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.copyRightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.copyRightFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.geniusCodesFrame = QFrame(self.copyRightFrame)
        self.geniusCodesFrame.setObjectName(u"geniusCodesFrame")
        self.geniusCodesFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.geniusCodesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.geniusCodesFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.copyRightLabel = QLabel(self.geniusCodesFrame)
        self.copyRightLabel.setObjectName(u"copyRightLabel")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.copyRightLabel.setFont(font2)
        self.copyRightLabel.setIndent(30)

        self.verticalLayout_6.addWidget(self.copyRightLabel)


        self.horizontalLayout_7.addWidget(self.geniusCodesFrame)

        self.dateAndTimeFrame = QFrame(self.copyRightFrame)
        self.dateAndTimeFrame.setObjectName(u"dateAndTimeFrame")
        self.dateAndTimeFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.dateAndTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.dateAndTimeFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.dateLabel = QLabel(self.dateAndTimeFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.dateLabel)

        self.timeLabel = QLabel(self.dateAndTimeFrame)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.timeLabel)


        self.horizontalLayout_7.addWidget(self.dateAndTimeFrame)


        self.verticalLayout_4.addWidget(self.copyRightFrame)


        self.horizontalLayout.addWidget(self.displayFrame)

        QtChartWindow.setCentralWidget(self.chartAndGraphsCentralWidget)

        self.retranslateUi(QtChartWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(QtChartWindow)
    # setupUi

    def retranslateUi(self, QtChartWindow):
        QtChartWindow.setWindowTitle(QCoreApplication.translate("QtChartWindow", u"MainWindow", None))
        self.projectIconLabel.setText("")
        self.projectNameLabel.setText(QCoreApplication.translate("QtChartWindow", u"QT CHARTS", None))
        self.percentageBarPushButton.setText(QCoreApplication.translate("QtChartWindow", u"Percentage Bar Chart", None))
        self.temperaturePushButton.setText(QCoreApplication.translate("QtChartWindow", u"Temperature Records", None))
        self.nestedDonutsPushButton.setText(QCoreApplication.translate("QtChartWindow", u"Nested Donuts", None))
        self.lineChartsPushButton.setText(QCoreApplication.translate("QtChartWindow", u"Line Charts", None))
        self.barChartPushButton.setText(QCoreApplication.translate("QtChartWindow", u"Bar Charts", None))
        self.supportIconLabel.setText("")
        self.supportLabel.setText(QCoreApplication.translate("QtChartWindow", u"SUPPORT ME", None))
        self.patreonIconLabel.setText("")
        self.subscribeIconLabel.setText("")
        self.payPalIconLabel.setText("")
        self.patreonPushButton.setText(QCoreApplication.translate("QtChartWindow", u"Patreon", None))
        self.subcribePushButton.setText(QCoreApplication.translate("QtChartWindow", u"Subscribe Youtube", None))
        self.payPalPushButton.setText(QCoreApplication.translate("QtChartWindow", u"PayPal", None))
        self.menuIconPushButton.setText("")
        self.menuLabel.setText(QCoreApplication.translate("QtChartWindow", u"MENU", None))
        self.dashBoardLabel.setText(QCoreApplication.translate("QtChartWindow", u"DASHBOARD", None))
        self.minimiseIconPushButton.setText("")
        self.restoreIconPushButton.setText("")
        self.closeIconPushButton.setText("")
        self.percentageBarLabel.setText(QCoreApplication.translate("QtChartWindow", u"PERCENTAGE BAR CHART", None))
        self.temperatureChartLabel.setText(QCoreApplication.translate("QtChartWindow", u"TEMPERATURE RECORDS CHART", None))
        self.label_13.setText(QCoreApplication.translate("QtChartWindow", u"BAR CHART", None))
        self.nestedDonutsLabel.setText(QCoreApplication.translate("QtChartWindow", u"NESTED DONUTS CHART", None))
        self.lineChartLabel.setText(QCoreApplication.translate("QtChartWindow", u"LINE CHART", None))
        self.copyRightLabel.setText(QCoreApplication.translate("QtChartWindow", u"GeniusCodes Copyright", None))
        self.dateLabel.setText("")
        self.timeLabel.setText("")
    # retranslateUi

