#6.User input

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height))

# Also you can use "," so you wouldn't change to data type.
print("You are", age, "years old")
print("You are", height)