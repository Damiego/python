#method riding
class animal: 
    def eat(self):
        print("this animal is eating")
        
class rabbit(animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = rabbit()
rabbit.eat()
