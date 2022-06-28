#IMPORTS
#import time
import tkinter as tk
from tkinter import *
#import keyboard
# VARIABLES
settings = {"1": [0, "StopOnSpace"], "2": [0, "StopOnDelete"]}
# SETUP
settingsfile = open("settings.txt", "r").readlines()
index = 0
for setting in settings:
  index += 1
  settings[setting][0] = settingsfile[index][:-1]
  index += 1
# SETTINGS WINDOW
def createsettings():
  new = Toplevel(root)
  new.title("Settings")
  newcanvas = tk.Canvas(new, width="280", height="600", bg="#FFFFFF")
  newcanvas.grid(columnspan=3)
# MAIN USER INTERFACE
root = tk.Tk()
root.title("Shrtct")
# MAIN CANVAS
canvas = tk.Canvas(root, width="760", height="400", bg="#FFFFFF")
canvas.grid(columnspan=3)
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
editmenu.add_command(label="New Shortcut", command="")
editmenu.add_command(label="Edit Shortcut", command="")
editmenu.add_command(label="Remove Shortcut", command="")
editmenu.add_separator()
editmenu.add_command(label="Settings", command=createsettings)
editmenu.add_command(label="Open Source Folder", command="")
# MAINLOOP
root.mainloop()