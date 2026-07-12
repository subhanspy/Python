#SMART SCHOOL MANAGMENT

class User:
    
    @staticmethod
    def school_timing():
        return f"School hours are from 8:00 am to 2:00 pm "
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_role(self):
        return f"I am the general user of the school"
    
class Teacher(User):
    def __init__(self,name,age,salary):
        super().__init__(name,age)

        self.__salary=salary
    
    def show_role(self):
        return f"I am a Teacher, teaching at this school."
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,new_salary):
        if new_salary <=0:
            print("Invalid Request")
        else:
            self.__salary=new_salary
        
user1=User("Ali","15")
print(user1.show_role())


Teacher1=Teacher("Shahzad",30,30,000)
print(Teacher1.show_role())

print(Teacher1.salary)
Teacher1.salary=-6000
print(Teacher1.salary)
print(User.school_timing())