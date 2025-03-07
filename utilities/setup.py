from setuptools import setup, Extension, find_packages

setup(
    name="utilities_pkg",
    version="1.0",
    packages=find_packages(), 
    ext_modules=
    [
        Extension("utilities_pkg.gcd", sources=["gcd.c"])
    ],  
)