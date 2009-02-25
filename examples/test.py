#!/usr/bin/python

import sys
import pygtk
pygtk.require('2.0')
import gtk
import abiword

window = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
window.set_default_size(640, 480)
window.resize(640,480)
window.show()
window.connect('delete-event', gtk.main_quit)

box = gtk.VBox()
window.add(box)
box.show()

abi = abiword.Canvas()
box.add(abi)
abi.show()

window.show()

b = gtk.Button('render page')
box.add(b)
b.show()

i = gtk.Image()
box.add(i)
i.show()

def _clicked_cb(widget, abi, i):
    i.props.pixbuf = abi.render_page_to_image(0)

b.connect('clicked', lambda widget: _clicked_cb(widget, abi, i))
window.show_all()
gtk.main()
