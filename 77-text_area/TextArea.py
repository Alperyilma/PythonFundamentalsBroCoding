from tkinter import *

# text widget -> functions like a text area, you can enter multiple lines of text

def submit():
    input = text.get("1.0",END)
    print(input)


window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",20),
            fg="Purple",
            width=30,
            height=11,
            padx=20,
            pady=20)
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()