from tkinter import *
from tkinter import colorchooser #submodule

def click():
    #1.Way
    color = colorchooser.askcolor() #assign color a variable
    colorHex = color[1] #assign element at index 1 to a variable
    window.config(bg=colorHex) #change background color

    #2.Way (Better Way)
    window.config(bg=colorchooser.askcolor()[1]) #change the background color



window = Tk()

window.geometry("420x420")
button = Button(text="click me", command=click)
button.pack()
window.mainloop()







