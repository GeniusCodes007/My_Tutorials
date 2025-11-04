from ui_qt_charts import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import Qt, QIcon, QColor
from PySide6 import QtCharts

class ActionEdit( Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.sliceHTML = None
        self.sliceCsh = None
        self.slicePHP = None
        self.sliceKotlin = None
        self.sliceJavaScript = None
        self.sliceJAVA = None
        self.sliceCPP = None
        self.slicePython = None
        self.pie_series = None
        self.pie_chart = None
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.setWindowTitle("My Charts App")
        self.setWindowIcon(QIcon(":/chart_icons/line_graph_1.png"))

        #Connect the buttons
        self.pieChartPushButton.clicked.connect(self.showPieChart)
        self.lineGraphPushButton.clicked.connect(self.showLineGraph)
        self.barChartPushButton.clicked.connect(self.showBarChart)

        self.updatePushButton.clicked.connect(self.updatePieChart)
        self.updatePieChart()
        self.updateLineGraph()
        self.updateBarChart()

    def showPieChart(self):
        self.stackedWidget.setCurrentIndex(0)

    def showLineGraph(self):
        self.stackedWidget.setCurrentIndex(1)

    def showBarChart(self):
        self.stackedWidget.setCurrentIndex(2)


    #Manage Pie Chart
    def updatePieChart(self):
        #self.chart_view
        self.pie_chart = QtCharts.QChart()

        #Initialise pie series
        self.pie_series = QtCharts.QPieSeries()
        self.pie_series.setLabelsVisible(True)
        self.pie_series.setLabelsPosition(QtCharts.QPieSlice.LabelPosition.LabelOutside)

        #Add slices for programming languages
        self.slicePython = QtCharts.QPieSlice("Python", float(self.pythonLineEdit.text()))
        self.slicePython.setColor("red")
        self.sliceCPP = QtCharts.QPieSlice("C++", float(self.cppLineEdit.text()))
        self.sliceJAVA = QtCharts.QPieSlice("JAVA", float(self.javaLineEdit.text()))
        self.sliceJavaScript = QtCharts.QPieSlice("Java Script", float(self.javaScriptLineEdit.text()))
        self.sliceKotlin = QtCharts.QPieSlice("Kotlin", float(self.kotlinLineEdit.text()))
        self.slicePHP = QtCharts.QPieSlice("PHP", float(self.phpLineEdit.text()))
        self.sliceCsh = QtCharts.QPieSlice("C#", float(self.cshLineEdit.text()))
        self.sliceHTML = QtCharts.QPieSlice("HTML", float(self.htmlLineEdit.text()))

        #Append language slices to Pie Series
        self.pie_series.append(self.slicePython)
        self.pie_series.append(self.sliceCPP)
        self.pie_series.append(self.sliceJAVA)
        self.pie_series.append(self.sliceJavaScript)
        self.pie_series.append(self.sliceKotlin)
        self.pie_series.append(self.slicePHP)
        self.pie_series.append(self.sliceCsh)
        self.pie_series.append(self.sliceHTML)

        #Add Pie Series to Chart
        self.pie_chart.addSeries(self.pie_series)
        self.pie_chart.setTitle("Programming Language Popularity")
        self.pie_chart.legend().setVisible(True)
        self.pie_chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.pieChartGraphicsView.setChart(self.pie_chart)

        try:
            numPython = float(self.pythonLineEdit.text())
            numCPP = float(self.cppLineEdit.text())
            numJava = float(self.javaLineEdit.text())
            numJavaScript = float(self.javaScriptLineEdit.text())
            numKotlin = float(self.kotlinLineEdit.text())
            numPHP = float(self.phpLineEdit.text())
            numCsh = float(self.cshLineEdit.text())
            numHTML = float(self.htmlLineEdit.text())

            #Update Slice Values
            total = numPython + numCPP + numJava + numJavaScript + numKotlin + numPHP + numCsh + numHTML

            if total > 0:
                self.slicePython.setValue((numPython/total)*100)
                self.sliceCPP.setValue((numCPP / total) * 100)
                self.sliceJAVA.setValue((numJava / total) * 100)
                self.sliceJavaScript.setValue((numJavaScript / total) * 100)
                self.sliceKotlin.setValue((numKotlin / total) * 100)
                self.slicePHP.setValue((numPHP / total) * 100)
                self.sliceCsh.setValue((numCsh / total) * 100)
                self.sliceHTML.setValue((numHTML / total) * 100)
        
        except ValueError:
            pass

    def updateLineGraph(self):
        chart = QtCharts.QChart()
        chart.setTitle("Programming Language Popularity Over Time")

        years = ["2020", "2021", "2022", "2023", "2024"]

        python_data = [10, 80, 30, 90, 35]
        cpp_data = [21, 24, 6, 30, 54]
        java_data = [23, 43, 12, 98, 45]
        javascript_data = [15, 25, 20, 30, 40]
        kotlin_data = [89, 75, 4, 27, 90]
        php_data = [12, 6, 7, 4, 3]
        csh_data = [12, 9, 4, 5, 6]
        html_data = [32, 45, 65, 7, 3]

        #Create series for each programming language

        python_series = QtCharts.QLineSeries()
        python_series.setName("Python")
        for i in range(len(years)):
            python_series.append(i, python_data[i])
        chart.addSeries(python_series)

        cpp_series = QtCharts.QLineSeries()
        cpp_series.setName("C++")
        for i in range(len(years)):
            cpp_series.append(i, cpp_data[i])
        chart.addSeries(cpp_series)

        java_series = QtCharts.QLineSeries()
        java_series.setName("Java")
        for i in range(len(years)):
            java_series.append(i, java_data[i])
        chart.addSeries(java_series)

        javascript_series = QtCharts.QLineSeries()
        javascript_series.setName("JavaScript")
        for i in range(len(years)):
            javascript_series.append(i, javascript_data[i])
        chart.addSeries(javascript_series)

        kotlin_series = QtCharts.QLineSeries()
        kotlin_series.setName("Kotlin")
        for i in range(len(years)):
            kotlin_series.append(i, kotlin_data[i])
        chart.addSeries(kotlin_series)

        php_series = QtCharts.QLineSeries()
        php_series.setName("PHP")
        for i in range(len(years)):
            php_series.append(i, php_data[i])
        chart.addSeries(php_series)

        csh_series = QtCharts.QLineSeries()
        csh_series.setName("C#")
        for i in range(len(years)):
            csh_series.append(i, csh_data[i])
        chart.addSeries(csh_series)

        html_series = QtCharts.QLineSeries()
        html_series.setName("HTML")
        for i in range(len(years)):
            html_series.append(i, html_data[i])
        chart.addSeries(html_series)

        #Add axis and set alignment
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(years)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        #Set minimum and maximum for the y-axis
        min_y = min(min(python_data), min(cpp_data), min(java_data), min(javascript_data), min(kotlin_data),
                    min(php_data), min(csh_data),
                    min(html_data))
        max_y = max(max(python_data), max(cpp_data), max(java_data), max(javascript_data), max(kotlin_data),
                    max(php_data), max(csh_data),
                    max(html_data))

        axis_y.setRange(min_y,max_y)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        #Attach axes to series
        python_series.attachAxis(axis_x)
        python_series.attachAxis(axis_y)

        cpp_series.attachAxis(axis_x)
        cpp_series.attachAxis(axis_y)

        java_series.attachAxis(axis_x)
        java_series.attachAxis(axis_y)

        javascript_series.attachAxis(axis_x)
        javascript_series.attachAxis(axis_y)

        kotlin_series.attachAxis(axis_x)
        kotlin_series.attachAxis(axis_y)

        php_series.attachAxis(axis_x)
        php_series.attachAxis(axis_y)

        csh_series.attachAxis(axis_x)
        csh_series.attachAxis(axis_y)

        html_series.attachAxis(axis_x)
        html_series.attachAxis(axis_y)

        self.lineGraphGraphicsView.setChart(chart)

    def updateBarChart(self):
        series = QtCharts.QBarSeries()
        series.setName("Programming Language Popularity Over Time")


        years = ["2020", "2021", "2022", "2023", "2024"]

        python_data = [10, 80, 30, 90, 35]
        cpp_data = [21, 24, 6, 30, 54]
        java_data = [23, 43, 12, 98, 45]
        javascript_data = [15, 25, 20, 30, 40]
        kotlin_data = [89, 75, 4, 27, 90]
        php_data = [12, 6, 7, 4, 3]
        csh_data = [12, 9, 4, 5, 6]
        html_data = [32, 45, 65, 7, 3]

        bar_set_python = QtCharts.QBarSet("Python")
        bar_set_cpp = QtCharts.QBarSet("C++")
        bar_set_java = QtCharts.QBarSet("Java")
        bar_set_java_script = QtCharts.QBarSet("Java Script")
        bar_set_kotlin = QtCharts.QBarSet("Kotlin")
        bar_set_php = QtCharts.QBarSet("PHP")
        bar_set_csh = QtCharts.QBarSet("C#")
        bar_set_html = QtCharts.QBarSet("HTML")

        for i in range(len(years)):
            bar_set_python.append(python_data[i])
            bar_set_cpp.append(cpp_data[i])
            bar_set_java.append(java_data[i])
            bar_set_java_script.append(javascript_data[i])
            bar_set_kotlin.append(kotlin_data[i])
            bar_set_php.append(php_data[i])
            bar_set_csh.append(csh_data[i])
            bar_set_html.append(html_data[i])

        series.append(bar_set_python)
        series.append(bar_set_cpp)
        series.append(bar_set_java)
        series.append(bar_set_java_script)
        series.append(bar_set_kotlin)
        series.append(bar_set_php)
        series.append(bar_set_csh)
        series.append(bar_set_html)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Programming Language Popularity Over Time")
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(years)
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        self.barChartGraphicsView.setChart(chart)