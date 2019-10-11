# File Name learn_wxpython.py
# Demo of python GUI programming using tkinter lib
# link : https://www.tutorialspoint.com/python3/python_multithreading.htm
#!usr/bin/python3

import wx

app = wx.App()
window = wx.Frame(None, title = "wxPython Frame", size = (300,200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = "Hello World", pos = (100,50))
window.Show(True)
app.MainLoop()
