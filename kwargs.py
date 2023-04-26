#kwargs
#parameter that can pack all arguments  into a dictionary useful so that a function can accept a varying amount of keyword agruments 

def hello(**names):
    # print("hello " + names['first'] + " " + names['last'])  #this limited
    print("hello", end=" ")
    for keys,value in names.items():
        print(value,end=" ")
hello(first="dami",middle="john",last="willmas",age=16)
