from tkinter import *


def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You don't agree :(")


window = Tk()

photo = PhotoImage(file="image.png")

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="green",
                           bg="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=23,
                           pady=10,
                           image=photo,
                           compound="left")

check_button.pack()

window.mainloop()
