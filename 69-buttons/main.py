from tkinter import *

# button -> You click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    print(f"You clicked the button! {count} time")


window = Tk(className="Button tables")

photo = PhotoImage(file="person-icon.png")

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="top")
button.pack()

window.mainloop()

