#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

values = input("Input some comma seprated numbers: ")
list = values.split(",")
tuple = tuple(list)

print(f"list: {list}")
print(f"Tuple: {tuple}") #list: ['1', '5', '7', '9', '11']
                         #Tuple: ('1', '5', '7', '9', '11')