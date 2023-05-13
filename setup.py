from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="Statisticia",
    version="0.1",
    packages=find_packages(),
    ext_modules=cythonize("src/cython/*.pyx"),
)