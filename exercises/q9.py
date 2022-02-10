#Write a Python program to add two objects if both objects are an integer type (write a function).

def add_numbers(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integer !!"
    return a + b

# The isinstance() function returns True if the specified object is of the specified type,
# otherwise False.
print(add_numbers(10, 20)) #30
print(add_numbers(10, 20.30)) #Inputs must be integer !!
print(add_numbers("20","30")) #Inputs must be integer !!

