from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from contentFile import Ui_DropAndSideMainWindow


class DropAndSideMainWindow(QMainWindow, Ui_DropAndSideMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Side Bar")

        # Hiding Widget Menu
        self.text_widget.setHidden(True)

        # Hide Drop-Downs
        self.student_drop_down_frame.setHidden(True)
        self.teacher_drop_down_frame.setHidden(True)
        self.finanace_drop_down_frame.setHidden(True)

        # Connect widget buttons to Stack Widget Pages
        self.dashboard_icon.clicked.connect(self.showDashBoard)
        self.dashboard_pushbutton.clicked.connect(self.showDashBoard)

        self.institution_icon.clicked.connect(self.showInstitution)
        self.institution_pushButton.clicked.connect(self.showInstitution)

        self.studentInfo.clicked.connect(self.showStudentInfo)
        self.studentResult.clicked.connect(self.showStudentResult)
        self.studentPayments.clicked.connect(self.showStudentPayments)

        self.teacherInfo.clicked.connect(self.showTeacherInfo)
        self.teacherAllowances.clicked.connect(self.showTeacherAllowance)
        self.teacherPayments.clicked.connect(self.showTeacherPayments)

        self.budgets.clicked.connect(self.showBudgets)
        self.expenses.clicked.connect(self.showExpenses)
        self.income.clicked.connect(self.showIncome)

        self.settings_icon.clicked.connect(self.showSettings)
        self.settings.clicked.connect(self.showSettings)

        self.student_icon.clicked.connect(self.studentsContextMenu)
        self.teachers_icon.clicked.connect(self.teachersContextMenu)
        self.finances_icon.clicked.connect(self.financeContextMenu)

    # Methods for displaying each page

    def showDashBoard(self):
        self.stackedWidget.setCurrentIndex(0)

    def showInstitution(self):
        self.stackedWidget.setCurrentIndex(1)

    def showStudentInfo(self):
        self.stackedWidget.setCurrentIndex(2)

    def showStudentResult(self):
        self.stackedWidget.setCurrentIndex(3)

    def showStudentPayments(self):
        self.stackedWidget.setCurrentIndex(4)

    def showTeacherInfo(self):
        self.stackedWidget.setCurrentIndex(5)

    def showTeacherAllowance(self):
        self.stackedWidget.setCurrentIndex(6)

    def showTeacherPayments(self):
        self.stackedWidget.setCurrentIndex(7)

    def showBudgets(self):
        self.stackedWidget.setCurrentIndex(8)

    def showExpenses(self):
        self.stackedWidget.setCurrentIndex(9)

    def showIncome(self):
        self.stackedWidget.setCurrentIndex(10)

    def showSettings(self):
        self.stackedWidget.setCurrentIndex(11)

    #Showing Context Menus for STUDENT

    def studentsContextMenu(self):
        self.showCustomContextMenu(self.student_icon, ["Student Info", "Student Result", "Student Payments"])
    
    def teachersContextMenu(self):
        self.showCustomContextMenu(self.teachers_icon, ["Teacher Info", "Teacher Allowances", "Teacher Payments"])
    
    def financeContextMenu(self):
        self.showCustomContextMenu(self.finances_icon, ["Budgets", "Expenses", "Income"])

    def showCustomContextMenu(self, button, menuItems):

        menu = QMenu(self)

        #Style Sheet
        menu.setStyleSheet(
            """
            QMenu{
            background-color: black;
            color: white;
            }
            
            QMenu:selected{
            background-color: white;
            color: #128298;
            }
            """)

        #Action
        for item in menuItems:
            action = QAction(item, self)
            action.triggered.connect(self.handleMenuItems)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handleMenuItems(self):

        text = self.sender().text_widget

        if text == "Student Info":
            self.showStudentInfo()
        elif text == "Student Payments":
            self.showStudentPayments()
        elif text == "Student Result":
            self.showStudentResult()
