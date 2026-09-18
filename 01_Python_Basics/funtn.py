# Calling function with ()

def say_hello():
    print('Hello')

say_hello()

#Accepting Parameters (Args)

def helping_verb(verb):
    print(f'You {verb} my friend')

helping_verb('are')

#Using return
def addition(num1,num2):
    return num1+num2

add=addition(8,9)
print(add)

add=addition('one','two')
print(add)

#Return multiple values with tupple

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


def check_hours(work_hours):
     
     maxi_hours=0

     employee_of_month=''

     for employee,hours in work_hours:
         if hours>maxi_hours:
            maxi_hours=hours
            employee_of_month=employee

         else:
             pass
         
     return (maxi_hours,employee_of_month)

print(check_hours(work_hours))

#game 

from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('Pick a number : 0, 1 ,2')
    return int(guess)

def check_guess(my_list,guess):
    if my_list[guess]==0:
        print('You Wins !!')

my_list=['','0','']
mixed_num=shuffle_list(my_list)
print(mixed_num)
guess_1=player_guess()
print(guess_1)
end_game=check_guess(mixed_num,guess_1)
print(end_game)
         
def choosing_num():
   choice=input("Enter the number in range (0 to 10):")

   if choice.isdigit()== False:
         print("Sorry this is not a number")

   if choice.isdigit()== True:
       if int(choice) in range(0,11):
           print("Number found")

       else:
           print("Number is out of range")
        

choosing_num()
