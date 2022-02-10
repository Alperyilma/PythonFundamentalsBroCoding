class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    #overriding -> Function nane have to same
    def eat(self):
        print("This Rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()