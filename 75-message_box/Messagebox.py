from tkinter import *
from tkinter import messagebox #import message box library

def click():
    # messagebox.showinfo(title="This is a info message box", message="You are a person")

    # messagebox.showwarning(title="This is a info message box", message="You have a virus!!!")

    # messagebox.showerror(title="ERROR!", message="Something went wrong :(")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do thing?"):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing :(")

    # if messagebox.askretrycancel(title="ask ok cancel", message="Do you retry the thing?"):
    #     print("You retry a thing!")
    # else:
    #     print("You canceled a thing :(")

    # print(messagebox.askquestion(title="ask question",message="Do you like python?"))

    # How can you take password from another computer?
    count = 1

    while True:
        if messagebox.askyesno(title="ask yes or no", message="Do you want your computer to run fast?"):
            messagebox.showinfo(message="it wil be uploaded 2 min later")
            with open("/Users/alperyilmaz/Desktop/secret/password.txt") as file:
                print(file.read())
                break
        else:
            messagebox.showinfo(message="Why? :(")
        if count == 3:
            break
        count += 1

window = Tk()

button = Button(window,
                command=click,
                text="Click me")
button.pack()

window.mainloop()