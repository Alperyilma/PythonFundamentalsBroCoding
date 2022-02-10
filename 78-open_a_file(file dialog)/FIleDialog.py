from tkinter import *
from tkinter import filedialog

def openFile():
    # Below code allows to find a file or txt in pycharm projects
    # file_in_directory_in_pycharm = filedialog.askopenfilename(initialdir="/Users/alperyilmaz/PycharmProjects/Bro_Coding/78-open_a_file(file dialog)",
    #                                                           title="Open file in pycharm",
    #                                                           filetypes=(("text files","*.txt"),
    #                                                                      ("all files","*.*")))
    # file = open(file_in_directory_in_pycharm)
    # print(file.read())
    # file.close()

    filepath = filedialog.askopenfilename()
    file = open(filepath)
    print(file.read())
    file.close()

window = Tk()

button = Button(text="open", command=openFile)
button.pack()

window.mainloop()
