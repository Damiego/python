#args
#parameter that can pack all arguments  into a tuple useful so that a function can accept a varying amount of agruments 

def add(*addition):
    sum = 0
    for i in addition:
        sum+=i
    return sum
print(add(2,2,2))
