from tkinter import *

# listbox -> A listing of selectable text items within it's own container

def submit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You have ordered: ")
    for i in food:
        print(i)

def add():
    if entryBox.get() != "" and entryBox.get() != " ":
        listbox.insert(listbox.size(),entryBox.get())
    else:
        print("Please Enter something!!")
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="gray",
                  font=("Constatia",35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()
