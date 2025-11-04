


class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = None
        self._num_bugs_solved = 0
    
    def code(self):
        self._num_bugs_solved += 1
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,base_value):
        self.__salary = self._calc_salary(base_value)
        return self.__salary
    
    def _calc_salary(self, base_value):
        if self._num_bugs_solved <10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se = SoftwareEngineer("Genius", "24")

for i in range(70):
    se.code()



#

print(se.name, se.age)
se.set_salary(4000)
print(se.get_salary())

