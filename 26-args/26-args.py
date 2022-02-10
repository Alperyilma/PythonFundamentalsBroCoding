# *args -> parameter that will pack all arguments into a tuple
#          useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6)) # 21

def convert_tuple_to_list(*args): # if i wanna convert first index, i have to convert tuple to list
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum
print(convert_tuple_to_list(1,2,3,4,5,6)) # 20
