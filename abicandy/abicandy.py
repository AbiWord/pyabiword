#!/usr/bin/python
import sys

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade
import abiword
import gettext

class SugarAbiWord:
    """Main class for SugarAbiWord"""
    def __init__(self):
        gtk.gdk.threads_init()


        self.m_pXML = gtk.glade.XML('abicandy.glade')
        self.window = self.m_pXML.get_widget('TopWindow')
        self.MainHbox = self.m_pXML.get_widget('hboxMain')
        self.sugarOpen =  self.m_pXML.get_widget('SugarOpen')
        self.sugarSave =  self.m_pXML.get_widget('SugarSave')
        self.sugarUndo =  self.m_pXML.get_widget('SugarUndo')
        self.sugarRedo =  self.m_pXML.get_widget('SugarRedo')
        self.sugarUnderline =  self.m_pXML.get_widget('SugarUnderline')
        self.sugarBold =  self.m_pXML.get_widget('SugarBold')
        self.sugarLeft =  self.m_pXML.get_widget('SugarLeft')
        self.sugarCenter =  self.m_pXML.get_widget('SugarCenter')
        self.sugarRight =  self.m_pXML.get_widget('SugarRight')
        self.sugarFill =  self.m_pXML.get_widget('SugarFill')
        self.abicanvas = abiword.Canvas()
        self.MainHbox.pack_end(self.abicanvas,True,True,0)

        self.abicanvas.show()
        self.window.show_all()

        self.abicanvas.set_property("map-to-screen", True)
        self.abicanvas.set_property("load-file", "")
    def onOpen_cb(self,me):
        self.abicanvas.set_property("file-open","")

    def onSave_cb(self,me):
        self.abicanvas.set_property("file-save","")

    def onUndo_cb(self,me):
        self.abicanvas.set_property("undo","")

    def onRedo_cb(self,me):
        self.abicanvas.set_property("redo","")

    def onUnderline_cb(self,me):
        self.abicanvas.set_property("toggle-uline","")

    def onBold_cb(self,me):
        self.abicanvas.set_property("toggle-bold","")

    def onLeft_cb(self,me):
        self.abicanvas.set_property("align-left","")

    def onCenter_cb(self,me):
        self.abicanvas.set_property("align-center","")

    def onRight_cb(self,me):
        self.abicanvas.set_property("align-right","")

    def onFill_cb(self,me):
        self.abicanvas.set_property("align-justify","")

    def saveImmediate(self,me):
        self.abicanvas.set_property("save-immediate","")
    
    def connectSignals(self):
        self.window.connect('destroy',self.saveImmediate)
        self.sugarOpen.connect('clicked',self.onOpen_cb)
        self.sugarSave.connect('clicked',self.onSave_cb)
        self.sugarUndo.connect('clicked',self.onUndo_cb)
        self.sugarRedo.connect('clicked',self.onRedo_cb)
        self.sugarUnderline.connect('clicked',self.onUnderline_cb)
        self.sugarBold.connect('clicked',self.onBold_cb)
        self.sugarLeft.connect('clicked',self.onLeft_cb)
        self.sugarCenter.connect('clicked',self.onCenter_cb)
        self.sugarRight.connect('clicked',self.onRight_cb)
        self.sugarFill.connect('clicked',self.onFill_cb)

    def main(self):
        self.connectSignals()
        gtk.main()
        
MySugarAbiWord = SugarAbiWord()
MySugarAbiWord.main()
