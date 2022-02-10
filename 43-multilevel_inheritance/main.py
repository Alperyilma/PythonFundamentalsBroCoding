# multi-level inheritance -> when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True



class Animal(Organism):

    def __init__(self,animal):
        self.animal = animal

    def eat(self):
        print(f"{self.animal}  is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

class Horse(Animal):
    pass


dog = Dog("Dog")
horse = Animal("Horse")
print(dog.alive) #True
dog.eat() #Dog  is eating
horse.eat() #Horse  is eating

dog.bark() #This dog is barking







