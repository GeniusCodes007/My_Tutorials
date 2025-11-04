import sys
from PyQt6.QtWidgets import QApplication
from lesson5 import Lesson5
from lesson6 import Lesson6


app = QApplication(sys.argv)

#window = Lesson5()
#window.show()

window2 = Lesson6()
window2.show()

sys.exit(app.exec())