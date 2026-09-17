#Statement assesment

st = 'Print only the words that start with s in this sentence'
state_1=st.split()

for word in state_1:
    if word.lower().startswith('s'):
        print(word)

#using range
numb=range(0,11)

for evn in numb:
    if evn % 2==0:
        print(evn)

#  
divide_by_3=[x for x in range(1,51) if x % 3 == 0]
print(divide_by_3)


print(len('Print every word in this sentence that has an even number of letters'))


st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 ==0:
        print(word +'<---This is even')

