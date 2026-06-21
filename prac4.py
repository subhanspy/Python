#Functions in Python

def multiply(x,y):
    return x*y

product = multiply(4,5)
print(product)

def addition(a, b, c, d=10):
    return a+b+c+d

print(addition(c=10, a=10, b=10))

def divide (numerator,denominator):
    if numerator==0:
        return  "Error: Cannot divide by zero"
    if denominator==0:
        return "Error: Enter other numbers"
    return numerator/denominator

Answer = divide (12,3)
print(Answer)

# Keywords Arguments

def person(age,name,city):
    return f"{name} is {age} years old and lives in {city}"

profile = person(age=22,name="Subhan",city="Nankana sahib")
print(profile)

#Variable Length Arguments

def vari_length(*args):
    return " ".join(args)

concatenate = vari_length("My","Name","is","subhan")
print(concatenate)

# by itration :
def concatenation(*args):
    for i in args:
        print (" ",i)

seq = concatenation("Ali",7,33.4,"Ahmad")

def addition (*args):
    total = 0
    for i in args:
        total+=i
        
    return total

add = addition(10,20,30,40,10)
print(add)    