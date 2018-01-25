# File Name learn_tkinter.py
# Demo of python GUI programming using tkinter lib
# link : https://www.tutorialspoint.com/python3/python_multithreading.htm
#!usr/bin/python3

import tkinter as tk # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import PIL.Image
import PIL.ImageTk

root = tk.Tk()
root.title("Laba")
# Code to add widgets will go here...
# Logo-image
#logo = tk.PhotoImage(file="icon.gif")
im = PIL.Image.open(fp="icc.jpg", mode="r")
#im2 = im.convert(mode="RGBA")
photo = PIL.ImageTk.PhotoImage(im)

print("height = ", photo.height(),", width = ", photo.width())
w1 = tk.Label(root, image=photo, bg="red", height=64, width=64)
w1.image = photo
w1.pack(side="right")
# Adding Label
w = tk.Label(root, height=5, width=30, justify=tk.LEFT, text="Hello Tkinter!").pack(side="left")

root.mainloop()
