from tkinter import *

# radio button -> similar to checkbox, but you can only select one from a group

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered a pizza")
    elif (x.get() == 1):
        print("You ordered a hamburger")
    elif (x.get() == 2):
        print("You ordered a hotdog")
    else:
        print("huhh?")


window = Tk()

pizzaImage = PhotoImage(file="fire.png")
hamburgerImage = PhotoImage(file="snow.png")
hotdogImage = PhotoImage(file="hotdog.png")

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # adds text to radio buttons
                               variable=x,  # groups radiobuttons together if they share the same variable
                               value=index,  # assigns each radiobutton a different value
                               padx=25,  # adds padding on x-axis
                               font=("Impact", 50),
                               image=foodImages[index],  # adds image to radiobutton
                               compound="left", #adds image & text (left side)
                               indicatoron=0, #eliminate circle indicators
                               width=375,
                               command=order #set command of radiobutton to function
                               )

    radio_button.pack(anchor=W)

window.mainloop()
