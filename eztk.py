# DEPENDENCIES
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

# todo: add treeview, add separator, add messagebox(if useful)

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
    def __init__(self, title="tk", size="300x300", iconpath="", height_resizable="False", width_resizable="False", close_function=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(width_resizable, height_resizable)
        if close_function:
            self.root.protocol("WM_DELETE_WINDOW", close_function)
        # Icon path is not relative to current path
        self.root.iconbitmap(default=iconpath)
    def run(self):
        self.root.mainloop()
    def update(self):
        # Must be declared in a while(True) loop together with other code you want to repeat
        # Although it is a possibility, it's relatively not good practice, as there is usually no need to run things in background
        self.root.update()
# TOP LEVEL WINDOW
class mktoplevel():
    def __init__(self, title="tk", size="300x300"):
        self.root = Toplevel()
        self.root.title(title)
        self.root.geometry(size)
# PLAIN TEXT
class mklabel(place):
    def __init__(self, parent, text="Sample", x=0, y=0, side=""):
        self.object = tk.Label(parent, text=text)
        self.place(self.object, x, y, side)
# SMALL INPUT BOX
class mkentry(place):
    def __init__(self, parent, x=0, y=0, side=""):
        self.variable = StringVar()
        self.object = tk.Entry(parent, textvariable=self.variable)
        self.place(self.object, x, y, side)
    def getvar(self):
        return self.variable.get()
# SIMPLE BUTTON
class mkbutton(place):
    def __init__(self, parent, text="", width=15, height=1, command="", x=0, y=0, side=""):
        self.object = tk.Button(parent, text=text, width=width, height=height, command=command)
        self.place(self.object, x, y, side)
# CHECKBOX
class mkcheck(place):
    def __init__(self, parent, text="Sample", x=0, y=0, side=""):
        self.variable = IntVar()
        self.object = tk.Checkbutton(parent, text=text, variable=self.variable)
        self.place(self.object, x, y, side)
    def getvar(self):
        return self.variable.get()
# LIST OF RADIO BUTTONS
class mkradiobuttons(place):
    def __init__(self):
        self.variable = IntVar()
        self.lastposition = 0
        self.buttons = {}
    def addbuttons(self, parent, names=["example"], x=0, y=2, side="", clearx=0, cleary=20, background="#FFFFFF", activebackground="#FFFFFF"):
        list(names)
        for i in range(len(names)):
            self.buttons[names[i]] = tk.Radiobutton(parent, text=names[i], variable=self.variable, value=self.lastposition, bg=background, activebackground=activebackground)
            self.place(self.buttons[names[i]], x+clearx*i, y+cleary*i, side=side)
            self.lastposition += 1
    def getvar(self):
        return self.variable.get()
# LIST
class mklistbox(place):
    def __init__(self, parent, width=80, height=150, x=0, y=0, side="", background="#FFFFFF"):
        self.object = tk.Listbox(parent, width=width, height=height, bg=background)
        self.object.bind("<<ListboxSelect>>", lambda x: self.getvar())
        self.place(self.object, x, y, side)
        self.lastposition = 0
        self.selection = int
    def addentry(self, names=["Sample"], start_position=-1):
        if start_position < -1:
            print("Wrong index!")
            return 1
        if start_position >= self.lastposition or start_position == -1:
            for i in range(len(names)):
                self.object.insert(self.lastposition, names[i])
                self.lastposition += 1
        else:
            for i in range(len(names)):
                if start_position < self.lastposition:
                    self.object.delete(start_position)
                    self.object.insert(start_position, names[i])
                    start_position += 1
                if start_position >= self.lastposition:
                    self.lastposition += 1
    def getvar(self):
        self.selection = self.object.curselection()[0]
# BIG INPUT BOX
class mktextbox(place):
    def __init__(self, parent, x=0, y=0, width=50, height=50, side=""):
        self.object = Text(parent, width=width, height=height)
        self.place(self.object, x, y, side)
    def getvar(self):
        return self.object.get("1.0","end-1c")
# BIG INPUT BOX WITH SCROLL BAR
class mkscrolledtextbox(place):
    def __init__(self, parent, x=0, y=0, width=50, height=50, side=""):
        self.object = ScrolledText(parent, width=width, height=height)
        self.place(self.object, x, y, side)
    def getvar(self):
        return self.object.get("1.0","end-1c")
# TOP MENU
class ezmenus():
    class mktopmenu():
        def __init__(self, parent):
            self.object = tk.Menu()
            parent.config(menu=self.object)
    class mkentry():
        def __init__(self, master_menu, name):
            self.object = tk.Menu()
            master_menu.add_cascade(label=name, menu=self.object)
    class mkoption():
        def __init__(self, parent, name, command=""):
            parent.add_command(label=name, command=command)
    class mkseparator():
        def __init__(self, parent):
            parent.add_separator()
class eznotebooks():
    class mknotebook(place):
        def __init__(self, parent, x=0, y=0, side=""):
            self.object = ttk.Notebook(parent)
            self.place(self.object, x, y, side)
    class mktab():
        def __init__(self, parent, name, width, height):
            self.object = ttk.Frame(parent, width=width, height=height)
            parent.add(self.object, text=name)
class mklabelframe(place):
    def __init__(self, parent, name, width, height, x=0, y=0, side=""):
        self.object = ttk.Labelframe(parent, text=name, width=width, height=height)
        self.place(self.object, x, y, side)