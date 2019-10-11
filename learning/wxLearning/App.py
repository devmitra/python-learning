# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan  3 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		frameSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.titleLabel = wx.StaticText( self, wx.ID_ANY, u"Hello World", wx.Point( -1,-1 ), wx.Size( -1,20 ), wx.ALIGN_CENTRE )
		self.titleLabel.Wrap( -1 )
		frameSizer.Add( self.titleLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.hiButton = wx.Button( self, wx.ID_ANY, u"Hi!", wx.DefaultPosition, wx.Size( 30,15 ), wx.BU_LEFT )
		frameSizer.Add( self.hiButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.hiLabel = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.hiLabel.Wrap( -1 )
		frameSizer.Add( self.hiLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( frameSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.hiButton.Bind( wx.EVT_BUTTON, self.sayHi )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sayHi( self, event ):
		event.Skip()
	

