#Comparison Operators

a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 5)  # True
print(b <= 10) # True

#Logical Operators

a = 5
b = 10

print(a > 0 and b > 0)  
print(a > 0 or b < 0)   
print(not(a == b)) 

#Conditional Statements
# if
a = int(input("Enter the number:"))
print(f"{a}")
if a > 0 :
    print("The number is poritive.")

#if-else
number = int(input("Enter the number"))
print(f"{number}")
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative or zero.")

#if else if

number = int(input("Enter the number:"))
print(f"{number}")
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#nested conditions
number = 4
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative or zero.")

#conditions for different data types

number = 15
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
