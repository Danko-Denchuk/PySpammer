# Python
# Simple GUI textspammer

import time
from tkinter import *
import ctypes
import keyboard

window = Tk()
window.title("")

window.geometry("356x200")

# This part is in charge of the output

def writetext():
    counter = 0
    time.sleep(2)
    # Time to put your cursor in the victim's box

    while counter <= int(entry2.get()):
        keyboard.write(entry1.get().lower() + "\n")
        print(entry1.get() + "\n")
        counter += 1
        time.sleep(0.5)

# This closes the window
def closewindow():
    window.destroy()

# This is the layout of text, buttons and boxes within the window.

text1 = Label(window, text = "Put here what you want to spam").place(x = 10, y = 10)
entry1 = StringVar()
box1 = Entry(window, textvariable = entry1).place(x = 10, y = 40)

text2 = Label(window, text = "How many times should it be repeated?").place(x = 10, y = 70)
entry2 = StringVar()
box2 = Entry(window, textvariable = entry2).place(x = 10, y = 100)

butt1 = Button(window, text = "Start SPAM", command = writetext).place(x = 10, y = 130)
butt1 = Button(window, text = "Give up", command = closewindow).place(x = 110, y = 130)

# Slider

#slider = Scale (window, from_ = 0.25, length = 200, orient = "HORIZONTAL", scale = )

# Needed crap for the program to work
window.mainloop()
