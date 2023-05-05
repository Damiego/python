#multi-level inheritance 
class orgnism ():

    alive = True
class animal(orgnism):
    
    def eat(self):
        print("This animal is eating")
class dog (animal):
    def bark(self):
        print("This dog is barking")
 
dog = dog()
print(dog.alive)
dog.eat()
dog.bark()
