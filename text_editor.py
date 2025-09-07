from tkinter import *
import tkinter.filedialog

# Main Window
main = Tk()
main.title("Text Editor")
text = Text(main)
text.grid()

# Function for saving text
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"),("All files", "*.*")])
    # Takes what the user writes and saves it as a file in the location they choose
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

# Function for opening a file (currently only txt)
def open_file():
    # Asks user to select a file
    filepath = tkinter.filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Only activates if the user selects a file
    if filepath:
        with open(filepath, "r") as file:
            content = file.read()

        # Clear current text
        text.delete("1.0", "end-1c")
        # Insert file text
        text.insert("1.0", content)

# Fonts
def FontVerdana():
    global text
    text.config(font=("Verdana", 12))

def FontCourier():
    global text
    text.config(font=("Courier", 12))

def FontArial():
    global text
    text.config(font=("Arial", 12))

def FontComicSans():
    global text
    text.config(font=("Comic Sans MS", 12))

# Creates a top menu bar
menubar = Menu(main)
main.config(menu=menubar)

# File Menu Button
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Save as...", command=saveas)
file_menu.add_command(label="Open", command=open_file)
menubar.add_cascade(label="File", menu=file_menu)

# Font menu Button
font_menu = Menu(menubar, tearoff=0)
font_menu.add_radiobutton(label="Verdana", command=FontVerdana)
font_menu.add_radiobutton(label="Courier", command=FontCourier)
font_menu.add_radiobutton(label="Arial", command=FontArial)
font_menu.add_radiobutton(label="Comic Sans", command=FontComicSans)
menubar.add_cascade(label="Font", menu=font_menu)

main.mainloop()