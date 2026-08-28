from functools import reduce

numbers = [45, 12, 89, 3, 27, 6]

small_num = reduce(lambda a,b :a if a < b else b,numbers)
print(small_num)
