# index operator [] -> gives access to a sequence's element (str,list,tuples)

name = "alper yilmaz"

if name[0].islower():
    name = name.capitalize()
print(name) #Alper yilmaz

first_name = name[:5].upper()
last_name = name[6:].upper()
last_character = name[-1]
reversed_name = name[::-1]

print(first_name) #AL
print(last_name) #YILMAZ
print(last_character) #z
print(reversed_name) #zamliy replA