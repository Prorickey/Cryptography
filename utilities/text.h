/**
 * @file text.h
 * @brief Header file for text utility functions
 */

 #ifndef TEXT_H
 #define TEXT_H
 
 #include <Python.h>  /* For Py_ssize_t */
 
 /**
  * @brief Divides text into blocks of specified size separated by spaces
  *
  * This function takes a null-terminated string and inserts spaces after
  * every block_size characters. The result is a new dynamically allocated
  * string that must be freed by the caller using PyMem_Free().
  *
  * @param text The input text to be divided into blocks
  * @param block_size The size of each block
  * @return A dynamically allocated string with spaces inserted, or NULL if memory allocation fails
  *
  * @note The caller is responsible for freeing the returned string using PyMem_Free()
  */
 char* text_block(char* text, int block_size);
 
 #endif /* TEXT_H */