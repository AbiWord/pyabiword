#!/usr/bin/python
#
# This script shows how multiple abiword widgets can be used in the
# same application.
#
# It also shows how they can be deleted.
#
import sys
import pygtk
pygtk.require('2.0')
import gtk
import abiword

class TwoWidgets:

    def _clicked_cb1(self,window,data):
        self.abi.destroy()
        self.abi = abiword.Canvas()
        self.abi.show()
        self.box.pack_start(self.abi)
        self.box.reorder_child(self.abi,0)

    def _clicked_cb2(self,window,data):
        self.abi2.destroy()
        self.abi2 = abiword.Canvas()
        self.abi2.show()
        self.box.pack_end(self.abi2)
        self.box.reorder_child(self.abi2,3)

    def __init__(self):
        self.window = gtk.Window()
        self.window.set_default_size(640, 480)
        self.window.connect('delete-event', gtk.main_quit)

        self.box = gtk.VBox()
        self.window.add(self.box)
        self.box.show()

        self.abi = abiword.Canvas()
        self.box.add(self.abi)
        self.abi.show()
        self.window.show()

        self.b1 = gtk.Button('Delete Top')
        self.box.add(self.b1)
        self.b1.show()

        self.b2  = gtk.Button('Delete Bottom')
        self.box.add(self.b2)
        self.b2.show()

        self.abi2 = abiword.Canvas()
        self.box.add(self.abi2)
        self.abi2.show()

        self.b1.connect('clicked', self._clicked_cb1,"delete top")
        self.b2.connect('clicked', self._clicked_cb2,"delete bottom")

    def main(self):
        gtk.main()

if __name__ == "__main__":
    two = TwoWidgets()
    two.main()
