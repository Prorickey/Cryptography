//
// Created by Trevor Bedson on 2/19/25.
//
#define PY_SSIZE_T_CLEAN
#include "Python.h"

// Extended Euclidean Algorithm

typedef struct {
    int x, y;
} EEAValues;

EEAValues eea(const int n, const int mod) {
    int x1 = 1, y1 = 0;
    int x2 = 0, y2 = 1;
    int a1 = n, a2 = mod;

    while (a2 != 0) {
        const int q = a1 / a2;
        const int r = a1 % a2;

        const int x = x1 - q * x2;
        const int y = y1 - q * y2;

        a1 = a2;
        x1 = x2;
        y1 = y2;

        a2 = r;
        x2 = x;
        y2 = y;
    }

    const EEAValues values = { x1, y1 };
    return values;
}

static PyObject *
eea_extended_euclidean_alg(PyObject *self, PyObject *args)
{
    const int n, mod;

    if (!PyArg_ParseTuple(args, "ii", &n, &mod)) return NULL;

    EEAValues res = eea(n, mod);
    PyObject* tuple = PyTuple_New(2);

    PyTuple_SetItem(tuple, 0, PyLong_FromLong(res.y));  
    PyTuple_SetItem(tuple, 1, PyLong_FromLong(res.x)); 

    return tuple;
}

// Define module methods
static PyMethodDef MyMethods[] = {
    {"extended_euclidean_alg", eea_extended_euclidean_alg, METH_VARARGS, "Returns a tuple (1, 2)"},
    {NULL, NULL, 0, NULL}
};

// Define module
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "eea",  // Module name
    NULL,         // Documentation
    -1,           // Module state
    MyMethods
};

// Initialize module
PyMODINIT_FUNC PyInit_eea(void) {
    return PyModule_Create(&mymodule);
}