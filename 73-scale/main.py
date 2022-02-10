from tkinter import *

def submit():
    if scale.get() >= 50:
        print(f"Be careful {scale.get()} degrees C !!!")
    else:
        print(f"The temperature is: {scale.get()} degrees C")


window = Tk()

hot_image = PhotoImage(file="../72-radio_buttons/fire.png")
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_=100, to=0,
              length=500,
              orient=VERTICAL, #orientation of scale
              font=("Consolas",20),
              tickinterval=10, #adds numeric indicators for value
              showvalue=0, #hide current value
              resolution=5, #increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="Black"
              )
scale.set(scale["to"]+10) #Starts always 10 degress
scale.pack()

# cold_image = PhotoImage(file="snow.png")
# cold_label = Label(image=cold_image)
# cold_label.pack()

button = Button(window, text="submit",command=submit)
button.pack()

window.mainloop()