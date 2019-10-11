# DEMO GUI
#!usr/bin/python3
import wx

#import the newly created GUI file
import App
class CalcFrame(App.MainFrame):
    def __init__(self,parent):
        App.MainFrame.__init__(self,parent)
        self.click = 0
    def sayHi(self, event):
      self.click += 1
      msg = "Hi! Thank you for click. Total click is " + str(self.click)
      print(msg);
      self.hiLabel.SetLabel(msg)

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()
