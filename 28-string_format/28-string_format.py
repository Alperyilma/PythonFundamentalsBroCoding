# str.format() -> optional method that gives users
#                 more control when displaying output

animal = "cow"
item = "moon"

print(f"The {animal} jumped over the {item}") #The cow jumped over the moon
print("The {} jumped over the {}".format(animal,item)) #The cow jumped over the moon
print("The {1} jumped over the {0}".format(animal,item)) #The moon jumped over the cow
print("The {animal} jumped over the {item}".format(animal="monkey",item="table")) #The monkey jumped over the table

text = "The {} jumped over the {}"
print(text.format(animal,item)) #The cow jumped over the moon

name = "Bro"

print("Hello, my name is {}".format(name)) #Hello, my name is Bro
print("Hello, my name is {:10}. Nice to meet you".format(name)) #Hello, my name is Bro       . Nice to meet you
print("Hello, my name is {:<10}. Nice to meet you".format(name)) #Hello, my name is Bro       . Nice to meet you
print("Hello, my name is {:>10}. Nice to meet you".format(name)) #Hello, my name is        Bro. Nice to meet you
print("Hello, my name is {:^10}. Nice to meet you".format(name)) #Hello, my name is    Bro    . Nice to meet you

pi = 3.1434114123
number = 1000

print("The number pi is {:.2f}".format(pi)) #3.14
print("The number is {:.3f}".format(number)) #1000.000
print("The number is {:,}".format(number)) #1,000
print("The number is {:b}".format(number)) #1111101000 -> binary
print("The number is {:o}".format(number)) #1750
print("The number is {:X}".format(number)) #3E8
print("The number is {:E}".format(number)) #1.000000E+03





