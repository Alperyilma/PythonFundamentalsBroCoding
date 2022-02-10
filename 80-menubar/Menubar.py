from tkinter import *
from tkinter import filedialog


def openFile():
    filePath =  filedialog.askopenfile(defaultextension=".txt", filetypes=[
        ("Txt File", ".txt"),("All Files", "*.*")])
    print(filePath.read())


def saveFile():
    filePath = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[
        ("Text File", ".txt"),("HTML File", ".html"),("All Files", "*.*")
    ])

    fileText = text.get(1.0,END)
    filePath.write(fileText)


def cut():
    print("You cut some text")

def copy():
    print("You copy some text")

def paste():
    print("You paste some text")

window = Tk()

openImage = PhotoImage(file="")
saveImage = PhotoImage(file="")
existImage = PhotoImage(file="")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Sans",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

text = Text(window)
text.pack()
button = Button(window, text="save", command=saveFile)
button.pack()

text.pack()

window.mainloop()


