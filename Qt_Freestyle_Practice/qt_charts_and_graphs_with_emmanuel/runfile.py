from PySide6.QtWidgets import QApplication
import sys
from actionEditFile import ActionEdit


app= QApplication(sys.argv)

window = ActionEdit()
window.show()
#waka_389bced0-9d6d-4a78-8436-49d2088693d0

sys.exit(app.exec())