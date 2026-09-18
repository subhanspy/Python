#Hybrid Inheritance

#EMPLOYEE MANAGMENT SYSTEM

class Employee:
    def __init__(self,name,salary,**kwargs):
        self.name=name
        self.salary=salary

    def get_details(self):
        return f"Name:{self.name},salary:{self.salary}"
    

class Manager(Employee):
    def __init__(self,name,salary,department,**kwargs):
        super().__init__(**kwargs)
        self.department=department
    
    def get_details(self):
        return f"{super().get_details()},Department:{self.department}"

class Engineer(Employee):
    def __init__(self ,name,salary,specialization,**kwargs):
        super().__init__(**kwargs)
        self.specialization=specialization
    
    def get_details(self):
        return f"{super().get_details()},Specialization:{self.specialization}"
    

class Teamlead(Manager,Engineer):

    def __init__(self,name,salary,department,specialization):
       super().__init__(name=name,salary=salary,department=department,specialization=specialization)

           
    def get_details(self):
        return f"{super().get_details()},department:{self.department}"

Lead=Teamlead("Subhan",60000,"IT","Software Development")
print(Lead.get_details())    
