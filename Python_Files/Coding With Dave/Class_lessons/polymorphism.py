"""
Polymorphism is similar to but not same as Inheritance
Polymorphism allows the use of a child class as though it were the parent class, yet the child class keeps its own methods.
"""
from employee_staff import EmployeeStaff, SoftwareEngineer, Designer

se = SoftwareEngineer("Max", "Software", "Senior", 6000, 34)
d = Designer("Philipp", "Design","Senior", 4000, 23)

employees =[SoftwareEngineer("Genius",  "Software","Senior", 6000, 34),
            SoftwareEngineer("Max", "Software","Junior", 4000, 34),
            Designer("Philipp", "Design","Senior", 4000, 23),
            SoftwareEngineer("Anna", "Software","Senior", 6000, 24),
            Designer("Monalisa", "Design","Junior", 3000, 34)]







def check_on(employees):
    for employee in employees:
        employee.work_status()

check_on(employees)