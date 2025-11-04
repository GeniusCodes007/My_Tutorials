from ui_free_style_2 import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout

class Edit(QMainWindow, Ui_MainWindow):
    
    v = [1, 3, 5, 7, 9, 11]
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #self.vLayout = QVBoxLayout(self.frame_2)
        
        #self.pushButton.clicked.connect(self.addButton)
        
        for x in range(0, len(self.v)):
            new = QPushButton(self.frame_2)
            new.setObjectName(f"button_{x}")
            new.setText(f"New Button {self.v[x]}")
            #print(x)
            self.gridLayout.addWidget(new, x, 0, 1, 1)