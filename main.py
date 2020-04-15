from tkinter import *

if __name__ == '__main__':

    mainWindow = Tk()
    mainWindow.title("Reverse String")
    label = Label(mainWindow, text="Enter String : ")
    label.grid(row=0)
    entry = Entry(mainWindow)
    entry.grid(row=0, column=1)


    def reverseString():
        string = entry.get()
        reverse = ""
        for i in range(len(string)):
            reverse += string[-1 * (i + 1)]
        reverseVar.set(reverse)

    button = Button(mainWindow, text="Reverse", command=reverseString)
    button.grid(column=0, row=1, )

    reverseVar = StringVar()
    reverseLabel = Label(textvariable=reverseVar)
    reverseLabel.grid(column=1, row=1)

    mainWindow.mainloop()
