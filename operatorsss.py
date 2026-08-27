#Enumirate for index number and element both
for i,letter in enumerate('abcdef'):
    print("At index {} the letter is {}".format(i,letter))

print(list(enumerate('abcde')))

#zip for two or more lists
list1=[1,2,3,4,5,6,7]
list2=['a','b','c','d','e','f','g']
values=list(zip(list1,list2))
print(values)


#for loop for tupple to statements
for item1,item2 in zip(list1,list2):
    print(f"for this tupple , the first value {item1} is paired with {item2}")

#In and Not In operators
letters=['a','b','c','x']
print('x' in letters)

print('x' not in letters)

#Min & Max
a=[23,45,11,100,24,19]
print(min(a))
print(max(a))

#Random Library
a=[23,24,100,45,69]
from random import shuffle
shuffle(a)
print(a)

#Random number from this range
from random import randint
numbis=randint(0,300)
print(numbis)

age=int(input('Enter your age here:' ))
print(f'You are young now!!{age}')