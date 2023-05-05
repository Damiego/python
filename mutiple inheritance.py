#mutiple inheritance 

class prey():
    def flee(self):
        print("This animal flees")
class predator:
    def hunt (self):
        print("this animal is hunting")
class rabbit(prey):
    pass
class hawk(predator):
    pass
class fish(predator):
    pass

rabbit = rabbit()
hawk = hawk()
fish = fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
