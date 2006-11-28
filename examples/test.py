#!/usr/bin/python

import sys
import pygtk
pygtk.require('2.0')
import gtk
import abiword

window = gtk.Window()
window.set_default_size(640, 480)
window.connect('delete-event', gtk.main_quit)

abi = abiword.Canvas()
window.add(abi)
window.show_all()

abi.set_property("map-to-screen", True)
abi.set_property("load-file", "test.abw")

gtk.main()
