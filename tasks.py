#Temprature
def Temprature(C):
    return C*9/5+32

celcius_input = float(input("Enter temprature in celcius"))

Farenhite_result=Temprature(celcius_input)
print("Temprature in farenhite is:",Farenhite_result)

# fizzbizz condition
i = int(input("Enter here"))
for i in range(1,16):
    
    if i % 3==0 and i % 5==0:
        print("FizzBizz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Bizz")
    else:
        print(i)