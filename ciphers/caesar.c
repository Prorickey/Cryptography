//
// Created by Trevor Bedson on 3/7/25.
//
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include "../utilities/text.h"

static PyObject* caesar_cipher(PyObject *self, PyObject *args, PyObject *kwargs) {

    const char *text;
    int key;
    int decrypt = 0;
    const char *letters = "abcdefghijklmnopqrstuvwxyz";

    static char *kwlist[] = {"text", "key", "decrypt", "letters", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "si|pz", kwlist, &text, &key, &decrypt, &letters)) return NULL;

    size_t lettersLen = strlen(letters);
    if (lettersLen == 0) {
        PyErr_SetString(PyExc_ValueError, "Letters cannot be empty");
        return NULL;
    }

    Py_ssize_t textLen = strlen(text);

    char *result = PyMem_Malloc(textLen + 1);
    if (result == NULL) {
        return PyErr_NoMemory();
    }

    key = key > 0 ? key % lettersLen : (lettersLen - (-key % lettersLen)) % lettersLen;
    if(decrypt) key = lettersLen - key;

    int j = 0;
    for (Py_ssize_t i = 0; i < textLen; i++) {
        char c = tolower(text[i]);
        const char *pos = strchr(letters, c);
        
        if (pos != NULL) {
            // Character found in letters
            int index = pos - letters;  // Get the index of the character
            int new_index;
            
            new_index = (index + key) % lettersLen;
            
            char new_char = letters[new_index];
            result[j] = decrypt ? letters[new_index] : toupper(letters[new_index]);
            j++;
        } 
    }

    result[j] = '\0'; 

    if(decrypt == 0) {
        char *blocked_text = text_block(result, 5);
        PyMem_Free(result);
        result = blocked_text;
    }

    PyObject *return_value = PyUnicode_FromString(result);
    PyMem_Free(result);
    
    return return_value;
}

// Define module methods
static PyMethodDef Methods[] = {
    {"caesar", (PyCFunction) caesar_cipher, METH_VARARGS | METH_KEYWORDS, "Encrypt and decrypt using the caesar cipher"},
    {NULL, NULL, 0, NULL}
};

// Define module
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "caesar",  // Module name
    "A module that provides Caesar cipher functionality", // Documentation
    -1,           // Module state
    Methods
};

// Initialize module
PyMODINIT_FUNC PyInit_caesar(void) {
    return PyModule_Create(&module);
}