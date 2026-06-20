#just practice
name = "subhan"
for i in range(1,6):
    print(name)

#pass 
for i in range(1,7):
 if i < 3:
    pass
 else:
    print(i)

#Lists Comprehension
a = [i * 2 for i in range(1,11)]
print(a)

squares = [i ** 2 for i in range(5)]
print(squares)

a = []
for i in range(1,11):
   a.append(i ** 2)
   print(a)

#loop
user_input = ""
while user_input.lower()!= "exit":
    user_input = input("Enter something (type 'stop' to end): ")
    print("You entered:", user_input)