#!/usr/bin/python
import sys

import pygtk
pygtk.require('2.0')
import gtk
import abiword

gtk.gdk.threads_init()

window = gtk.Window()
window.set_default_size(640, 480)

abicanvas = abiword.Canvas()

window.add(abicanvas)

abicanvas.show()
window.show()

abicanvas.set_property("AbiWidget--map-to-screen", True)
abicanvas.set_property("AbiWidget--load-file", "test.abw")

gtk.main()
