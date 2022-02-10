#Write a Python program to get a string which is n (non-negative integer) copies of a given string (write a function).

def larger_string(str,n):
    result = ""
    for i in range(n):
        result += str
    return result

print(larger_string("abc",2))
print(larger_string(".py",3))

