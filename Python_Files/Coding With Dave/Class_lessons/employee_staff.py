"""

Say we have a class which has some attributes that some other classes do not have,
the process of assigning the class with the required attributes to the ones without the attributes is called Inheritance.
We will see examples of such below:
"""



class EmployeeStaff:
    # class attribute
    staff_attribute = "Workaholic"

    def __init__(self, name,flank, level, salary):
        # instance attributes
        self.name = name
        self.flank = flank
        self.level = level
        self.salary = salary
        
    def work_status(self):
        if self.flank == "Software":
            print(f"{self.name} is coding, right now")
        if self.flank == "Design":
            print(f"{self.name} is designing, right now")

class SoftwareEngineer(EmployeeStaff):
    def __init__(self, name,flank, level, salary, age):
        super().__init__(name,flank, level, salary,)
        self.age = age
    
    def skill(self):
        print(f"{self.name} is a Network Wizard.")
    
    def virtue(self):
        print(f"{self.name} is dedicated to his work.")

class Designer(EmployeeStaff):
    def __init__(self, name,flank, level, salary, age):
        super().__init__(name,flank, level, salary)
        self.age = age
    
    def skill(self):
        print(f"{self.name} designs the  fliers, posters and bill boards in this firm.")
    
    def virtue(self):
        print(f"{self.name} has a beautiful heart.")

"""
se = SoftwareEngineer("Genius","Senior", 7000, 21)
print(f"{se. name}, {se.level}")
se.work_status()
se.skill()
se.virtue()

d = Designer("Dexter","Senior", 5000, 22)
print(f"{d. name}, {d.level}")
d.work_status()
d.skill()
d.virtue()
"""