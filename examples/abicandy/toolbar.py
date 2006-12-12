# Copyright (C) 2006, Red Hat, Inc.
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
import logging
import gtk
import pango

class Toolbar(gtk.Toolbar):
	def __init__(self, abiword_canvas):
		gtk.Toolbar.__init__(self)
		
		self.set_orientation(gtk.ORIENTATION_VERTICAL)
		self.set_style(gtk.TOOLBAR_ICONS)

		self._abiword_canvas = abiword_canvas
	
		self._open = gtk.ToolButton()
		self._open.set_icon_name('gtk-open')
		self._open.connect("clicked", self._open_cb)
		self.insert(self._open, -1)
		self._open.show()

		self._save = gtk.ToolButton()
		self._save.set_icon_name('gtk-save')
		self._save.connect("clicked", self._save_cb)
		self.insert(self._save, -1)
		self._save.show()
		self._abiword_canvas.connect("is-dirty",self._isDirty_cb)

		self._insert_separator()

		self._undo = gtk.ToolButton()
		self._undo.set_icon_name('gtk-undo')
		self._undo.connect("clicked", self._undo_cb)
		self.insert(self._undo, -1)
		self._undo.show()
		self._abiword_canvas.connect("can_undo",self._canUndo_cb)

		self._redo = gtk.ToolButton()
		self._redo.set_icon_name('gtk-redo')
		self._redo.connect("clicked", self._redo_cb)
		self.insert(self._redo, -1)
		self._redo.show()
		self._abiword_canvas.connect("can_redo",self._canRedo_cb)

		self._insert_separator()

		self._underline = gtk.ToggleToolButton()
		self._underline.set_icon_name('gtk-underline')
		self._underline_id = self._underline.connect("clicked", self._underline_cb)
		self.insert(self._underline, -1)
		self._underline.show()
		self._abiword_canvas.connect("underline",self._isUnderline_cb)

		self._bold = gtk.ToggleToolButton()
		self._bold.set_icon_name('gtk-bold')
		self._bold_id =self._bold.connect("clicked", self._bold_cb)
		self.insert(self._bold, -1)
		self._bold.show()
		self._abiword_canvas.connect("bold",self._isBold_cb)

		self._insert_separator()

		self._align_left = gtk.ToggleToolButton()
		self._align_left.set_icon_name('gtk-justify-left')
		self._align_left.connect("clicked", self._align_left_cb)
		self.insert(self._align_left, -1)
		self._align_left.show()

		self._align_center = gtk.ToggleToolButton()
		self._align_center.set_icon_name('gtk-justify-center')
		self._align_center.connect("clicked", self._align_center_cb)
		self.insert(self._align_center, -1)
		self._align_center.show()

		self._align_right = gtk.ToggleToolButton()
		self._align_right.set_icon_name('gtk-justify-right')
		self._align_right.connect("clicked", self._align_right_cb)
		self.insert(self._align_right, -1)
		self._align_right.show()

		self._align_fill = gtk.ToggleToolButton()
		self._align_fill.set_icon_name('gtk-justify-fill')
		self._align_fill.connect("clicked", self._align_fill_cb)
		self.insert(self._align_fill, -1)
		self._align_fill.show()

	def _insert_separator(self):
		separator = gtk.SeparatorToolItem()
		separator.set_draw(True)
		self.insert(separator, -1)
		separator.show()

	def setToggleButtonState(self,button,b,id):
		button.handler_block(id)
		button.set_active(b)
		button.handler_unblock(id)
		
		
	def _open_cb(self, button):
		self._abiword_canvas.file_open()

	def _save_cb(self, button):
		self._abiword_canvas.file_save()

	def _isDirty_cb(self,abi,b):
		print "isDirty",b
		self._save.set_sensitive(b)

	def _undo_cb(self, button):
		self._abiword_canvas.undo()

	def _canUndo_cb(self,abi,b):
		self._undo.set_sensitive(b)

	def _redo_cb(self, button):
		self._abiword_canvas.redo()

	def _canRedo_cb(self,abi,b):
		self._redo.set_sensitive(b)

	def _underline_cb(self, button):
		self._abiword_canvas.toggle_underline()

	def _isUnderline_cb(self,abi,b):
		self.setToggleButtonState(self._underline,b,self._underline_id)

	def _bold_cb(self, button):
		self._abiword_canvas.toggle_bold()

	def _isBold_cb(self,abi,b):
		self.setToggleButtonState(self._bold,b,self._bold_id)

	def _align_left_cb(self, button):
		self._abiword_canvas.align_left()

	def _align_center_cb(self, button):
		self._abiword_canvas.align_center()

	def _align_right_cb(self, button):
		self._abiword_canvas.align_right()

	def _align_fill_cb(self, button):
		self._abiword_canvas.align_justify()

