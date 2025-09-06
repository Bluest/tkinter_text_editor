from tkinter import *
import tkinter.filedialog

main = Tk("Text Editor")
text = Text(main)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")

    savelocation = tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(main, text="Save", command = saveas)
button.grid()

main.mainloop()
