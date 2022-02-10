#Write a Python program to accept a filename from the user and print the extension of that.

filename = input("Input the file name: ")
f_extns = filename.split(".")

print(f"The extension of the file is: {f_extns[-1]}") #java

