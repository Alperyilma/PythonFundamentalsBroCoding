
text = "Yoooooooo\nThis is some text\nHave a good one :)"
text2 = "Uh oh! This text has been overwritten"
text3 = "\nHave a nice day! See ya !"

# w -> makes overwritten
# a -> adds another text and it is not delete current text before second text
with open("33-test.txt", "w") as file:
    file.write(text3)