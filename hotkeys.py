
import time
import tkinter as tk
import keyboard
# Variables
settings = {"1": [0, "StopOnSpace"], "2": [0, "StopOnDelete"]}
# Setup
settingsfile = open("settings.txt", "r").readlines()
index = 0
for setting in settings:
  index += 1
  settings[setting][0] = settingsfile[index][:-1]
  index += 1

# Loop
#TODO