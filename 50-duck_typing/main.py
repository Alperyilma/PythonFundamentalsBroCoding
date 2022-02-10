# Duck typing -> concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/atributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck."

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is qwuacking")

class Person:
    def catch(self, prm):
        prm.walk()
        prm.talk()
        print("You caught the critter..")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) # -> This chicken is walking
                      #     This chicken is qwuacking
                      #     You caught the critter..
print()

person.catch(duck) # -> This duck is walking
                   #    This duck is qwuacking
                   #    You duck the critter..







