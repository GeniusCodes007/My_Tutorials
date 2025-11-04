"""
Encapsulation is the concealing of data implementation. This means that instance variables and methods can be made to be accessed from one side. 

"""


class TechStaffs:
    #class attribute
    staff_attribute = "Network Wizard"
    
    def __init__(self, name, age, level):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.__salary = 5000
        self._num_bugs_solved = 0
        
se = TechStaffs("Max",25, "Senior")
print(se.age, se.name, se.__salary)