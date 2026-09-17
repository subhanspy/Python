#basic

print(4 * (6+5))
print(4*6+5)
print(4+6*5)

#square & square root
a=5**2
print(a)

import math
a = 64
sq_root=math.sqrt(a)
print(sq_root)

#print e of hello using indexing
a = "Hello"
print(a[1])

#print "Hello" Reverse
a = "Hello"
print(a[::-1])

#Reassign nested list "Hello" with "Goodbye"
list3 = [1,2,[3,4,'hello']]
list3[2][2]="Goodbye"
print(list3)

#sorting list:
list4 = [5,3,4,6,1]
sort_list=set(list4)
print(sort_list)

list4.sort()
print(list4)

# Grab 'hello'
d = {'k1':{'k2':'hello'}}
value= d['k1']['k2']
print(value)


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
value=d['k1'][0]['nest_key'][1][0]
print(value)

#Tupple Unpacking
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(list2)

for (t1,t2) in list2:
    print(t1)