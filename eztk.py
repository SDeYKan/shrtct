from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class eztk:
    class mkwindow():
        def __init__(self, title="tk", size="300x300"):
            self.root = Tk()
            self.root.title(title)
            self.root.geometry(size)
    class mklabel():
        def __init__(self, parent, text="Sample", x=0, y=0):
            self.label = tk.Label(parent.root, text=text)
            self.label.place(x=x, y=y)
    class mkentry():
        def __init__(self, parent, x=0, y=0):
            self.variable = StringVar()
            self.entry = tk.Entry(parent.root, textvariable=self.variable)
            self.entry.place(x=x, y=y)
        def getvar(self):
            return self.variable.get()
    class mkcheck():
        def __init__(self, parent, text="Sample", x=0, y=0):
            self.variable = IntVar()
            self.checkbutton = tk.Checkbutton(parent.root, text=text, variable=self.variable)
            self.checkbutton.place(x=x, y=y)
        def getvar(self):
            return self.variable.get()
    class mkradio():
        def __init__(self, parent, text="Sample", value=1, x=0, y=0):
            return
            # Todo: This won't work like this. Radio buttons are intended to be multiple options for a variable in common.
            #self.variable = IntVar()
            #self.radiobutton = tk.Radiobutton(parent.root, text=text, variable=self.variable)
            #self.radiobutton.place(x=x, y=y)
        def getvar(self):
            #return self.variable.get()
            return
    class mktextbox():
        def __init__(self, parent, x=0, y=0, width=50, height=50):
            self.box = Text(parent.root, width=width, height=height)
            self.box.place(x=x, y=y)
        def getvar(self):
            return self.box.get("1.0","end-1c")
    class mkscrolledtextbox():
        def __init__(self, parent, x=0, y=0, width=50, height=50):
            self.box = ScrolledText(parent.root, width=width, height=height)
            self.box.place(x=x, y=y)
        def getvar(self):
            return self.box.get("1.0","end-1c")
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
    class mkbutton():
        def __init__(self, parent, text="", width=15, height=1, command="", x=0, y=0):
            self.button = tk.Button(parent.root, text=text, width=width, height=height, command=command)
            self.button.place(x=x, y=y)
    class mklistbox():
        def __init__(self, parent, width=80, height=150, x=0, y=0):
            self.listbox = tk.Listbox(parent.root, width=width, height=height)
            self.listbox.place(x=x, y=y)
        def mkentry(self, position, text="Sample"):
            self.listbox.insert(position, text)
def main():
    main = eztk.mkwindow(title="Main2")
    main.root.mainloop()
if __name__ == "__main__":
    main()