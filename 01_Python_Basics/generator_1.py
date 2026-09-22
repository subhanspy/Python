# Generators

def my_generator ():
    for i in range (1,6):
        yield f"Numbers {i}"

for x in my_generator():
    print(x)