#Car Attributes
class Car:
    def __init__(self,brand,model):
        
        self.__brand=brand
        self.model=model

    

#Car method full name
    def full_name(self):
     return f"The car name is {self.brand} {self.model}"
    
    def get_brand(self):
       return self.__brand + "!"

#INHERITANCE
class Electric_Car(Car):
   def __init__(self,__brand,model,battery_size):
      super().__init__(__brand,model)
      self.battery_size=battery_size

second_car=Electric_Car("Tesla","S 2","830kwh")
#print(second_car.__brand)
print(second_car.model)
print(second_car.full_name())   

#this_car=Car("Toyota","Corolla")
#print(this_car.brand)
#print(this_car.model)

#Calling function full name:
#print(this_car.full_name())

#Adding another car:
New_car=Car("Tesla","super")
print(New_car.full_name())
print(second_car.get_brand())
