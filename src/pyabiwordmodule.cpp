
/*
 * TODO: shut down abiword app when no longer needed.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>
#include <ap_Args.h>
#include <ap_UnixApp.h>

extern "C" {

extern void pyabiword_register_classes (PyObject *d);
extern PyMethodDef pyabiword_functions[];

static AP_UnixApp *_abiword_app = NULL;

DL_EXPORT(void)
initabiword (void)
{
    PyObject *m, *d;

    init_pygobject ();

    XAP_Args XArgs = XAP_Args(PACKAGE);
    _abiword_app = new AP_UnixApp(&XArgs, PACKAGE);
    AP_Args Args = AP_Args(&XArgs, PACKAGE, _abiword_app);
    Args.parsePoptOpts();

    m = Py_InitModule ("abiword", pyabiword_functions);
    d = PyModule_GetDict (m);

    pyabiword_register_classes (d);

    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module pyabiword");
    }
}

};
