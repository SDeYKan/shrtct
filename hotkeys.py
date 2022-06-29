#IMPORTS

import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import subprocess
import os
#from turtle import width
#from unicodedata import name
#from matplotlib.pyplot import text
#from numpy import var
#from pyparsing import col
# SETUP
def settingssetup():
  # Variables
  defaultsettings = [0, 0, 0, "Tab", 12, 0, 0, 0]
  settings = []
  # Code
  settingsfile = open("settings.txt", "r").readlines() # Reads the settings file
  index = 0
  for setting in range(len(defaultsettings)):
    index += 1
    settings.append(settingsfile[index][:-1])
    index += 1
  return settings
# VARIABLES
settings = settingssetup()
# ------------GUI MENU------------
# (WINDOW) SETTINGS
def createsettingswindow():
  new = Toplevel(root)
  new.title("Settings")
  newcanvas = tk.Canvas(new, width="280", height="600", bg="#FFFFFF").grid(columnspan=3)
# (WINDOW) NEW SHORTCUT
def createshortcutwindow():
  new = Toplevel(root)
  new.title("New Shortcut")
  new.geometry("700x580")
  tk.Label(new, text="Name: ").place(x=20, y=20)
  name = tk.StringVar()
  entryname = tk.Entry(new, textvariable=name).place(x=65, y=20)
  tk.Label(new, text="Shortcut: ").place(x=340, y=20)
  short = tk.StringVar()
  entryshort = tk.Entry(new, textvariable=short).place(x=400, y=20)
  tk.Label(new, text="Text to Paste:").place(x=20, y=75)
  paste = ScrolledText(new, height=9, width=80)
  paste.place(x=20, y=100) # Place method is called on newline because i need to get() its content.
  tk.Label(new, text="Text to Paste:").place(x=20, y=275)
  script = ScrolledText(new, height=9, width=80)
  script.place(x=20, y=300) # Place method is called on newline because i need to get() its content.
  def getinput():
    data = []
    data.append(name.get())
    data.append(short.get())
    data.append(paste.get("1.0","end-1c"))
    data.append(script.get("1.0","end-1c"))
    print(data)
    new.destroy()
  menu = tk.Menu(new)
  new.config(menu=menu)
  filemenu = tk.Menu(menu)
  menu.add_cascade(label="File", menu=filemenu)
  filemenu.add_command(label="Save", command=getinput)
  filemenu.add_command(label="Exit", command=new.destroy)
# MAIN USER INTERFACE
def mainwindow():
  def opensourcefolder():
    path =  os.getcwd()
    subprocess.Popen('explorer "'+path+'"')
  root.title("Shrtct")
  # MAIN CANVAS
  canvas = tk.Canvas(root, width="760", height="400", bg="#FFFFFF").grid(columnspan=3)
  # TOP MENU
  menu = tk.Menu(root) # Create a main menu object
  root.config(menu=menu)
  # FILE
  filemenu = tk.Menu(menu) # Create a menu child for "menu", it will be one of the options
  menu.add_cascade(label="File", menu=filemenu) # Make "filemenu" an option on main menu, it'll appear as "File"
  filemenu.add_command(label="Exit", command=root.quit) # Add command "Exit" that will show when you click on "File" menu
  # EDIT
  editmenu = tk.Menu(menu) # Another menu child
  menu.add_cascade(label="Edit", menu=editmenu)
  editmenu.add_command(label="New Shortcut", command=createshortcutwindow)
  editmenu.add_command(label="Edit Shortcut", command="")
  editmenu.add_command(label="Remove Shortcut", command="")
  editmenu.add_separator()
  editmenu.add_command(label="Settings", command=createsettingswindow)
  editmenu.add_command(label="Open Source Folder", command=opensourcefolder)
  # MAINLOOP
  root.mainloop()
# ------------END GUI MENU------------
root = tk.Tk()
mainwindow()