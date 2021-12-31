import sys
from setuptools import setup
#from Cython.Build import cythonize

#if 'setuptools.extension' in sys.modules:
#    m = sys.modules['setuptools.extension']
#    m.Extension.__dict__ = m._Extension.__dict__

from distutils.core import setup, Extension

module1 = Extension('fib',
                    sources = ['fib.c'])

#setup(name="cython_example_fib", ext_modules=cythonize('fib.pyx', gdb_debug=True), compiler_directives={'embedsignature': True, "emit_code_comments": True})
setup(name="fib", ext_modules = [module1] )
