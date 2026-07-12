#Class:
class Car:

    total_car=0

    #Constructor:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
        Car.total_car+=1

    #Function or method for full name
    def full_name(self):
        return f"The car name is {self.brand} {self.model} "
    
    def fuel_type(self):
        return f"Petrol or diesel"
     
class Electric(Car):
    def __init__(self,brand,model,electric_battery):
        super().__init__(brand,model)
        
        #Private the electric battery
        self.__electric_battery=electric_battery
    

    #get function to access private variable
    def get_battery(self):
        return self.__electric_battery
    

    #Function for full name
    def full_name(self):
        
        return f"The car name is {self.brand} {self.model} and its battery capacity is {self.__electric_battery}"
    
    #setter to update private value
    def set_battery(self,new_battery):
        self.__electric_battery=new_battery
    
    def fuel_type(self):
        return f"Electric fuel"
    
#Objects:
my_car=Car("Toyota","Corolla")
new_car=Car("Honda","Civic")
elec_car=Electric("Tesla","S 2","80kwh")
elec_car.set_battery("100kwh")

#calling objects
#print(my_car.brand)
#print(my_car.model)
#print(new_car.brand)
#print(new_car.model)

#Calling function
print(new_car.full_name())
print(my_car.full_name())
print(elec_car.full_name())
#print(elec_car.get_battery())
print(elec_car.fuel_type())
print(new_car.fuel_type())
print(Car.total_car)