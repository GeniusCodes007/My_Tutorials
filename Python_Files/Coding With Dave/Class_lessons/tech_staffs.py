"""
The 4 Principles of Object-Oriented Programming:
Inheritance
Polymorphism
Encapsulation
Abstraction

"""
# position, name, age, level, salary
#se1 = ["Software Engineer", "Max", 20, "Senior", 5000]
#se2 = ["Software Analyst", "Lisa", 20, "Junior", 3000]
#tailor = ["Fashion Designer", "Mike"]


class TechStaffs:
    #class attribute
    staff_attribute = "Network Wizard"
    
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    def code(self):
        print(f"{self.name} is busy right now")
        
    def code_in_language(self, language):
        print(f"{self.name} is a {language} Programmer")
    """
    def information(self):
       data = f"Name: {self.name} \nAge: {self.age}\nLevel: {self.level} \nSalary: {self.salary}"
       print(data)
        """
    def __str__(self):
        data = f"Name: {self.name}; Age: {self.age}; Level: {self.level}; Salary: {self.salary}"
        return data
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.name
    
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 7000
        else:
            return 9000
        


# instance
se1 = TechStaffs("Max", 20, "Senior", 5000)
print(se1.name, se1.age, se1.level, se1.salary)
print(TechStaffs.staff_attribute)
se2 = TechStaffs("Lisa", 20, "Junior", 3000)
print(se2.name, se2.age, se2.level, se2.salary)
print(se2.staff_attribute)
"""
class attributes are variable values assigned to all instances (or any instance) of a class
instance attributes are peculiar to each instance
"""
se1.code()
se2.code()

se1.code_in_language("Python")
se2.code_in_language("JAVA")

#se1.information()
#se2.information()
print(se2.entry_salary(45))
print(TechStaffs.entry_salary(29))
