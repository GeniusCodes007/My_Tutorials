#from chartsAndGraphsQtFiles
import os
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCharts import QChart
from random import randrange
from functools import partial
import csv
import datetime

#to install Custom_Widgets
#Run: pip install QT-PyQt-PySide-Custom-Widgets
#from Custom_Widgets.Widgets import *

#frame3 = projectNameFrame
#frame5 = supportFrame
#frame8 = mainDisplayFrame

from chartsAndGraphsQtFiles.qtChartWindow_ui import Ui_QtChartWindow
from PySide6.QtWidgets import QMainWindow


shadowElements = {"leftMenuWidget",
                  "projectNameFrame",
                  "supportFrame",
                  "mainDisplayFrame",
                  "headerFrame"}


class QtChartAndGraphActionEdit(QMainWindow, Ui_QtChartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setMinimumSize(850, 600)

        now = datetime.datetime.now()
        time_ = f"Time: {now.strftime('%H:%M:%S')}"
        date_ = f"Date: {now.strftime('%Y-%m-%d')}"

        self.dateLabel.setText(f"{date_}")
        self.timeLabel.setText(f"{time_}")

        for x in shadowElements:
            #effect = QtWidgets.QGraphicsDropShadowEffect(self)
            #effect.setBlurRadius(18)
            #effect.setXOffset(0)
            #effect.setYOffset(0)
            #effect.setColor(QColor(0,0,0,255))
            #getattr(self.ui,x).setGraphicsEffect(effect)
            pass

