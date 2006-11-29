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

	self.abiword_canvas = Canvas()

	toolbar = Toolbar(self.abiword_canvas)
	hbox.pack_start(toolbar, False)
	toolbar.show()

	hbox.add(self.abiword_canvas)
	self.abiword_canvas.set_property("map-to-screen", True)
	self.abiword_canvas.set_property("load-file", "")
	self.abiword_canvas.show()
        mainWindow.connect("delete_event",self._delete_cb)

    def _delete_cb(self,me,p):
        print "Doing delete \n"
        self.abiword_canvas.set_property("save-immediate","")
        
    def main(self):
        gtk.main()
        
MySugarAbiWord = SugarAbiWord()
MySugarAbiWord.main()
