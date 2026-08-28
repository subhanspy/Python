celsius_temps = [0, 10, 20, 30, 40]

def to_farenhite(c):
    return (c * 9/5) + 32 

Farenhite_temp=list(map(to_farenhite,celsius_temps))
print(Farenhite_temp)


words = ["Python", "Machine", "Learning", "Code"]

find_length=list(map(len,words))
print(find_length)