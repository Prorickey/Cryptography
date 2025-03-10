#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <string.h>
#include <stdio.h>
#include <ctype.h>

char* text_block(char* text, int block_size) {
    Py_ssize_t textLen = strlen(text);
    Py_ssize_t num_spaces = (textLen > 0) ? (textLen - 1) / block_size : 0;
    Py_ssize_t result_len = textLen + num_spaces;

    char *result = PyMem_Malloc(result_len + 1);

    if (result == NULL) {
        return NULL;
    }

    Py_ssize_t j = 0; 
    
    for (Py_ssize_t i = 0; i < textLen; i++) {
        if (i > 0 && i % block_size == 0) {
            result[j++] = ' ';
        }
        /* Copy the character */
        result[j++] = text[i];
    }
    

    result[j] = '\0';

    return result;
}

static PyObject* mod_text_block(PyObject *self, PyObject *args, PyObject *kwargs) {
    char *text;
    int block_size = 5;

    static char *kwlist[] = {"text", "block_size", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s|i", kwlist, &text, &block_size)) return NULL;

    if (block_size <= 0) {
        PyErr_SetString(PyExc_ValueError, "Block size must be greater than 0");
        return NULL;
    }

    char *result = text_block(text, block_size);
    Py_ssize_t result_len = strlen(result);

    PyObject *return_value = PyUnicode_DecodeUTF8(result, result_len, "strict");
    PyMem_Free(result);

    if (return_value == NULL) {
        PyErr_Clear();
        return_value = PyUnicode_DecodeLatin1(result, result_len, "strict");
        if (return_value == NULL) {
            return NULL;
        }
    }

    return return_value;
}

static PyMethodDef Methods[] = {
    {"text_block", (PyCFunction) mod_text_block, METH_VARARGS | METH_KEYWORDS, "Breaks text into blocks"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "text",  // Module name
    NULL,         // Documentation
    -1,           // Module state
    Methods
};

PyMODINIT_FUNC PyInit_text(void) {
    return PyModule_Create(&mymodule);
}