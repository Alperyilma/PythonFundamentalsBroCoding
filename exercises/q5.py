#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three
# times of their sum (write a function).

def sum_thrice(x,y,z):
    sum = x+y+z
    if x == y == z:
        sum *= 3
    return sum

print(sum_thrice(1,2,3)) #6
print(sum_thrice(3,3,3)) #27

