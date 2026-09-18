# Lists
list_a=[x for x in 'word']
print(list_a)

numb=[1,2,3,4,5,6,7,8,9,10]
list_1=[x**2 for x in numb]
print(list_1)

even_1=[x for x in numb if x % 2 == 0]
print(even_1) 

my_lst=[x**2 for x in [x**2 for x in numb]]
print(my_lst)

celcius=[2,20,36,39,26,43]
temp_1=[((9/5)*temp+32) for temp in celcius]
print(temp_1)
