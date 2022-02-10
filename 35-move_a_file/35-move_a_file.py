import os

source = "alperdirectory"
destination = "/Users/alperyilmaz/Desktop/topsecret"

sentences = "Hii amigoo. What are you doing here!"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source, "was moved")
        with open("/Users/alperyilmaz/Desktop/topsecret/alper.txt", "a") as file:
            file.write(sentences)

except FileNotFoundError:
    print(source, "was not found")

with open("/Users/alperyilmaz/Desktop/topsecret/alper.txt") as file:
    print(file.read())


