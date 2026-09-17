#Print your age, name, height
Name = "Subhan"
age = 22
height = 5.10
print(f"My name is:{Name},I'm {age} year old, My total height is:{height:.2f} feet")

#Input

Name= input("my name is :")
print(f"Hello, {Name}!")

#Arthimatic Operators

a = 2
b = 4
print("Addition:",a+b)
print("Multiplication:",a*b)
print("Subtraction:",a-b)
print("Divison:",a/b)

#Strings
first = "Subhan"
Second = "Rashid"
full = first + " " + Second
print("Full Name:",full)
print("Full Name in uppercase:",full.upper())
print("First Letter:",full[0])
print("Last Letter:",full[-1])

#Boolean
is_sunny = False 
is_raining = True

if is_sunny and not is_raining:
    print("It's a sunny day!")

if is_sunny or is_raining:
    print("Weather condition met.")

# Lists: Add, Remove, No. of fruits, print all
fruits = ["apple", "banana", "cherry", "orange", "grape"]
fruits.append("Mango")
print(fruits)
fruits.remove("banana")
print(fruits)
print("Number of fruits:",len(fruits))
print("Fruits List:",fruits)

# Tupple
coordinates = (10.5, 25.3, 40.8)
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])
print("Z-coordinate:", coordinates[2])

#if we uncomment the line below it will show error because tupple are immutable
# coordinates[0] = 12.5

# dictionary
student = {"name": "Subhan", "age": 20, "Degree": "Computer Science"}
student["GPA"] = 3.2  
student["age"] = 23  
print("Student Profile:", student)
print("Keys:", student.keys())
print("Values:", student.values())
del student["Degree"]  
print("Updated Profile:", student)


