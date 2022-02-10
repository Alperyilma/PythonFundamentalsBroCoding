# exception -> events detected during execution that interrupt the flow of a program

#numerator = int(input("Enter a number to divide: "))
#denominator = int(input("Enter a number to divide by: "))
#result = numerator / denominator
#print(result) # ZeroDivisionError: division by zero

try:
    numerator = float(input("Enter a number to divide: "))
    denominator = float(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero! idiot :)")
except ValueError as e:
    print(e)
    print("Enter only number plz. Is there a problem in your mind?")
except Exception:
   print("Something went wrong :(")
else:
    print("Before the -if:",result) #This is for control
    letter = ".0"
    if letter in str(result):
        print(int(result))
    else:
        print("{:.2f}".format(result))
finally:
    print("This will always execute")


