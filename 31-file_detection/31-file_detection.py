import os

path = "/Users/alperyilmaz/Desktop/text.txt"

if os.path.exists(path):
    print("That location is exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")








