
SUBDIRS = src

EXTRA_DIST =			\
	examples		\
	\
	AUTHORS			\
	COPYING			\
	ChangeLog		\
	NEWS			\
	autogen.sh		\
	python.m4

dist-hook:
	rm -rf `find $(distdir)/examples -name .svn`
