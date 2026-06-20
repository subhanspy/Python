#Functions in Python
def multiply(x,y):
    return x*y

product = multiply(4,5)
print(product)

def addition(a, b, c, d=10):
    return a+b+c+d

print(addition(c=10, a=10, b=10))

def divide(numerator, denominator):
    if denominator == 0:
        return "Error: Cannot divide by zero."
    return numerator / denominator

# Correct usage
result = divide(10, 2)  
print(result)  

# Incorrect order
result = divide(denominator=2, numerator=10)  
print(result) 
