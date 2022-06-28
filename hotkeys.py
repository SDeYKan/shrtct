
import time
import tkinter as tk
import keyboard
import mouse
# Setup
event = 0
history = []
last = ""
stoponmouse = False
stoponkeys = False

def remove(li: list, times: int, pos = "left") -> list:
  if len(li) >= times:
    if pos == "left":
      for i in range(times):
        li = li[1:]
    elif pos == "right" or pos == "r":
      for i in range(times):
        li = li[:len(li) - 1]
    else: print("Please use 'right' or 'r'")
  else: print("List was not shortened")
  return li
  
  return history

# Loop
while True:
  # Section Listen
  history.append(keyboard.read_key())
  # End Section Listen
  print(history)