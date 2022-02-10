#4.String Methods

name = "bro code"
print(len(name))
print(name.find("Code"))
print(name.capitalize()) # Bro code --> converts only firstletter to uppercase
print(name.upper()) #BRO CODE
print(name.lower()) #bro code
print(name.isdigit()) #False --> if variable contains only numbers, it will return True
print(name.isalpha()) #False --> It returned False, because there is a empty
print(name.count("o"))
print(name.replace("o","i")) #bri cide
print(name * 3) #bro codebro codebro code --> It returned 3 times same string

