#widgets -> GUI elements: buttons, textboxes, labels, images
#windows -> server as a container to hold or contain these widgets

from tkinter import *

window = Tk(className="Alper's First Window") #instantiate an instance of a window
window.geometry("700x700")

#For download image
icon = PhotoImage(file="image.png")
window.iconphoto(True,icon)

#For change to background
window.config(background="#5cfcff")
# window["background"] = "blue" #2.Way

window.mainloop() #place window on computer screen listen for events


