#!/usr/bin/python

# Copyright (C) 2006, Martin Sevior <msevior@physics.unimelb.edu.au>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
import sys

import pygtk
pygtk.require('2.0')
import gtk
import abiword
import gettext
from abiword import Canvas
from toolbar import Toolbar
class SugarAbiWord:
    """Main class for SugarAbiWord"""
    def __init__(self):
        gtk.gdk.threads_init()
        mainWindow = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        mainWindow.resize(640,480)
        mainWindow.show()
        hbox = gtk.HBox(False, 0)
        mainWindow.add(hbox)
        hbox.show()
        print 'Pullin in Canvas \n '
	self.abiword_canvas = Canvas()
        print 'Canvas obtained \n'
	toolbar = Toolbar(self.abiword_canvas)
	hbox.pack_start(toolbar, False)
	toolbar.show()

	hbox.add(self.abiword_canvas)
	self.abiword_canvas.show()
        mainWindow.connect("delete_event",self._delete_cb)
#
# test out signals
#
        self.styleName_id = self.abiword_canvas.connect("style-name",self.styleName_cb)
        self.fontFamily_id = self.abiword_canvas.connect("font-family",self.fontFamily_cb)
        self.fontSize_id = self.abiword_canvas.connect("font-size",self.fontSize_cb)
        self.textSelected_id = self.abiword_canvas.connect("text-selected",self.textSelected_cb)
        self.imageSelected_id = self.abiword_canvas.connect("image-selected",self.imageSelected_cb)
        self.selectionCleared_id = self.abiword_canvas.connect("selection-cleared",self.selectionCleared_cb)
        self.enterSelection_id = self.abiword_canvas.connect("enter-selection",self.enterSelection_cb)
        self.leaveSelection_id = self.abiword_canvas.connect("leave-selection",self.leaveSelection_cb)

    def _delete_cb(self,me,p):
        print "Doing delete \n"
        self.abiword_canvas.save_immediate()
        gtk.main_quit()
        
    def main(self):
        gtk.main()

    def styleName_cb(self,abi,sz):
        print 'Style is ',sz
		
    def fontFamily_cb(self,abi,sz):
        print 'Font Family is ',sz
		 
    def fontSize_cb(self,abi,iSize):
        print 'Font Size is ',iSize
		
    def textSelected_cb(self,abi,b):
        if b:
            print 'Text selected \n'
        else:
            print 'Text unselected \n'
		
    def imageSelected_cb(self,abi,b):
        if b:
            print 'Image selected \n'
        else:
            print 'Image unselected \n'
		
    def selectionCleared_cb(self,abi,b):
        if b:
            print 'Selected cleared\n'
        else:
            print 'Selection cleared -error wrong bool \n'

		
    def enterSelection_cb(self,abi,b):
        if b:
            print 'Enter Selection \n'
        else:
            print 'enter selection -error wrong bool \n'
		
    def leaveSelection_cb(self,abi,b):
        if b:
            print 'Leave Selection \n'
        else:
            print 'Leave selection -error wrong bool \n'
		
        
MySugarAbiWord = SugarAbiWord()
MySugarAbiWord.main()
