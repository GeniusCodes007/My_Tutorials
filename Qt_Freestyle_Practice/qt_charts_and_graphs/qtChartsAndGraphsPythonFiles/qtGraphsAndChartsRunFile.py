from PySide6.QtWidgets import QApplication
from qtChartAndGraphActionEdit import QtChartAndGraphActionEdit
import sys
#ui_qtChartWindow

class Run(QtChartAndGraphActionEdit):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = Run()
window.show()

sys.exit(app.exec())
