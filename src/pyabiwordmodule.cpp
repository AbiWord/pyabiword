
/*
 * TODO: shut down abiword app when no longer needed.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>
#include <libabiword.h>

extern "C" {

extern void pyabiword_register_classes (PyObject *d);
extern PyMethodDef pyabiword_functions[];

DL_EXPORT(void)
initabiword (void)
{
    PyObject *m, *d;
    char *argv[] = { PACKAGE, NULL };

    init_pygobject ();
    libabiword_init (1, argv);

    m = Py_InitModule ("abiword", pyabiword_functions);
    d = PyModule_GetDict (m);

    pyabiword_register_classes (d);

    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module pyabiword");
    }
}

}; // extern "C"
