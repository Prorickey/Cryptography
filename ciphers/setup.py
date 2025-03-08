from setuptools import setup, Extension, find_packages

setup(
    name="ciphers_pkg",
    version="1.0",
    packages=find_packages(), 
    ext_modules=
    [
        Extension("ciphers_pkg.caesar", sources=["caesar.c", "../utilities/text.c"])
    ],  
)