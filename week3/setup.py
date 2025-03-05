from setuptools import setup, Extension

module = Extension("eea", sources=["eea.c"])

setup(
    name="eea",
    version="1.0",
    ext_modules=[module],
)
