#Write a Python program to test whether a passed letter is a vowel or not (write a function).

def letter(char):
    all_letters = "aeiou"
    return char in all_letters

print(letter("a"))
print(letter("c"))

