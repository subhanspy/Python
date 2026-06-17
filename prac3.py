#Loops

i = 1
while i <= 10:
    print(i)
    i += 1

#Using range
for i in range(1, 11):
    print(i)

#Loops using lists

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Loops using Dictonary

person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():    #item ka kam inhy pairs mein rakhna hai key or value ko  

    print(f"This is the key: {key}; and its value is: {value}")

#Zip
Names = ["Ali","Ahmad","Asif","AAhmar"]
Age = [20,29,18,23,26]



