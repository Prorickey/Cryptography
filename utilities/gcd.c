//
// Created by Trevor Bedson on 2/19/25.
//
#include "Python.h"

// Euclidean Algorithm Implementation
static PyObject *
gcd(PyObject *self, PyObject *args)
{
    int n1, n2;

    if (!PyArg_ParseTuple(args, "ii", &n1, &n2)) return NULL;

    if(n1 < 0) { n1 = -n1; }
    if(n2 < 0) { n2 = -n2; }

    if (n1 == 0) {
        return PyLong_FromLong(n2);
    } else if (n2 == 0) {
        return PyLong_FromLong(n1);
    }

    while (n1 != n2) {
        if (n1 > n2) {
            n1 = n1 - n2;
        } else {
            n2 = n2 - n1;
        }
    }

    return PyLong_FromLong(n1);
}

// Define module methods
static PyMethodDef Methods[] = {
    {"gcd", gcd, METH_VARARGS, "Returns the greatest common divisor"},
    {NULL, NULL, 0, NULL}
};

// Define module
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "gcd",  // Module name
    NULL,         // Documentation
    -1,           // Module state
    Methods
};

// Initialize module
PyMODINIT_FUNC PyInit_gcd(void) {
    return PyModule_Create(&mymodule);
}