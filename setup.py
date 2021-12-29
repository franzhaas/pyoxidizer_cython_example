import sys
from setuptools import setup
from Cython.Build import cythonize

#if 'setuptools.extension' in sys.modules:
#    m = sys.modules['setuptools.extension']
#    m.Extension.__dict__ = m._Extension.__dict__

setup(name="cython_example_fib", ext_modules=cythonize('fib.pyx'))
