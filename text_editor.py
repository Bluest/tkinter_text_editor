from tkinter import *
import tkinter.filedialog

# Main Window
main = Tk("Text Editor")
text = Text(main)
text.grid()

# Function for saving text
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                        filetypes=[("Text files", "*.txt"),
                                                                   ("All files", "*.*")])
    # Takes what the user writes and saves it as a file in the location they choose
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

# Button used for save text function
button = Button(main, text="Save", command=saveas)
button.grid()

# Fonts
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

# Creates font selector widget
font = Menubutton(main, text="Font")
font.grid()
font.menu=Menu(font, tearoff=0) # creates drop down menu
font["menu"] = font.menu
# Keeps track of whether an item is checked
helvetica = IntVar()
courier = IntVar()
# Adds two buttons to the font menu
font.menu.add_checkbutton(label="Helvetica", variable=helvetica,
command = FontHelvetica)
font.menu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)

main.mainloop()