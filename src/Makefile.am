
AM_CPPFLAGS = 				\
	-Wno-long-long 			\
	$(PYTHON_CFLAGS) 		\
	$(PYTHON_INCLUDES) 		\
	$(PYGTK_CFLAGS) 		\
	$(ABIWORD_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = pyabiword.defs

pkgpythondir = $(pyexecdir)/abiword
pkgpyexecdir = $(pyexecdir)/abiword

pyabiworddir = $(pkgpythondir)
pyabiword_PYTHON = __init__.py

# pyabiword module
pkgpyexec_LTLIBRARIES = abiword.la
abiword_la_LDFLAGS = -module -avoid-version
abiword_la_LIBADD = $(PYGTK_LIBS) $(ABIWORD_LIBS)
abiword_la_SOURCES = pyabiwordmodule.cpp
nodist_abiword_la_SOURCES = pyabiword.c

BUILT_SOURCES = pyabiword.c
CLEANFILES = pyabiword.c
EXTRA_DIST = pyabiword.override pyabiword.defs

pyabiword.c: pyabiword.defs pyabiword.override
	$(PYGTK_CODEGEN) --prefix pyabiword			\
	--register $(PYGTK_DEFSDIR)/gdk-types.defs	\
	--register $(PYGTK_DEFSDIR)/gtk-types.defs	\
	--override $(srcdir)/pyabiword.override $(srcdir)/pyabiword.defs > $@
