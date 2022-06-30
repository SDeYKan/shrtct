# DEPENDENCIES
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class place():
    def place(self, object, x, y, side):
        # Place is the default method for an easy xy coords object placements
        # Because it can take longer than pack() or grid() to place correctly, it can be unconfortable for some
        # If you don't want to use it, you can either just overwrite it by using other method in the next line
        # You can add a side="" argument to change it for pack()
        # Grid needs too many arguments. You can still manually write it in a new line under the declaration!
        if not side:
            object.place(x=x, y=y)
        elif side:
            object.pack(side=side)
# MAIN WINDOW
class mkwindow():
    def __init__(self, title="tk", size="300x300"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(size)
# TOP LEVEL WINDOW
class mktoplevel():
    def __init__(self, title="tk", size="300x300"):
        self.root = Toplevel()
        self.root.title(title)
        self.root.geometry(size)
# PLAIN TEXT
class mklabel(place):
    def __init__(self, parent, text="Sample", x=0, y=0, side=""):
        self.label = tk.Label(parent.root, text=text)
        self.place(self.label, x, y, side)
# SMALL INPUT BOX
class mkentry(place):
    def __init__(self, parent, x=0, y=0, side=""):
        self.variable = StringVar()
        self.entry = tk.Entry(parent.root, textvariable=self.variable)
        self.place(self.entry, x, y, side)
    def getvar(self):
        return self.variable.get()
# SIMPLE BUTTON
class mkbutton(place):
    def __init__(self, parent, text="", width=15, height=1, command="", x=0, y=0, side=""):
        self.button = tk.Button(parent.root, text=text, width=width, height=height, command=command)
        self.place(self.button, x, y, side)
# CHECKBOX
class mkcheck(place):
    def __init__(self, parent, text="Sample", x=0, y=0, side=""):
        self.variable = IntVar()
        self.checkbutton = tk.Checkbutton(parent.root, text=text, variable=self.variable)
        self.place(self.checkbutton, x, y, side)
    def getvar(self):
        return self.variable.get()
# LIST OF RADIO BUTTONS
class mkradiobuttons(place):
    def __init__(self):
        self.variable = IntVar()
        self.lastposition = 0
        self.buttons = {}
    def addbutton(self, parent, number_of_buttons=1, names=["example"], x=0, y=0, side="", clearx=0, cleary=20):
        list(names)
        if number_of_buttons == len(names) and number_of_buttons >= 1:
            for i in range(number_of_buttons):
                self.buttons[names[i]] = tk.Radiobutton(parent.root, text=names[i], variable=self.variable, value=self.lastposition + 1)
                self.place(self.buttons[names[i]], x+clearx*i, y+cleary*i, side)
                self.lastposition += 1
        else:
            print("The number of buttons does not equal the number of names you have given.")
            return 1
    def getvar(self):
        return self.variable.get()
# LIST
class mklistbox(place):
    def __init__(self, parent, width=80, height=150, x=0, y=0, side=""):
        self.listbox = tk.Listbox(parent.root, width=width, height=height)
        self.place(self.listbox, x, y, side)
    def mkentry(self, position, text="Sample"):
        self.listbox.insert(position, text)
# BIG INPUT BOX
class mktextbox(place):
    def __init__(self, parent, x=0, y=0, width=50, height=50, side=""):
        self.box = Text(parent.root, width=width, height=height)
        self.place(self.box, x, y, side)
    def getvar(self):
        return self.box.get("1.0","end-1c")
# BIG INPUT BOX WITH SCROLL BAR
class mkscrolledtextbox(place):
    def __init__(self, parent, x=0, y=0, width=50, height=50, side=""):
        self.box = ScrolledText(parent.root, width=width, height=height)
        self.place(self.box, x, y, side)
    def getvar(self):
        return self.box.get("1.0","end-1c")
# TOP MENU
class topmenu():
    class mktopmenu():
        def __init__(self, parent):
            self.submenus = {}
            self.menu = tk.Menu()
            parent.root.config(menu=self.menu)
    class mkentry():
        def __init__(self, master_menu, name):
            master_menu.submenus[name] = tk.Menu()
            master_menu.menu.add_cascade(label=name, menu=master_menu.submenus[name])
    class mkoption():
        def __init__(self, master_menu, submenu, name, command=""):
            master_menu.submenus[submenu].add_command(label=name, command=command)
    class mkseparator():
        def __init__(self, master_menu, submenu):
            master_menu.submenus[submenu].add_separator()
# GUI START
def run_forever(program):
    program.root.mainloop()
def run_multitask(program):
    # Must be declared in a while() loop that repeats forever or until something is triggered
    program.root.update()