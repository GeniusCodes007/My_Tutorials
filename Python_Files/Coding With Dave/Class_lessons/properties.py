


class SoftwareEngineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, base_value):
        self._salary = base_value
    
    @salary.deleter
    def salary(self, base_value):
        del self.salary

    



se = SoftwareEngineer()
se.salary = 5000

#se.set_salary(4000)
print(se.salary)
#del se.salary
print(se.salary)