from PySide6.QtWidgets import QApplication, QMainWindow
from contentFile import Ui_SpinTVMainWindow
import sys

print("for C_DEL: https://engage2.mtn.ng/nc/?time_stamp=1757678231700&uid=TVBks%2FjUKMQBZc6Iow%3D%3D")

class ContentShow(QMainWindow, Ui_SpinTVMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        print("Boy")

app = QApplication(sys.argv)
show = ContentShow()
show.show()
sys.exit(app.exec())

 