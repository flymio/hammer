from distutils.core import setup, Extension

module1 = Extension('chasher',
                    sources = ['chasher.c'])

setup (name = 'CHasher',
       version = '1.0',
       description = 'C implementation of the hasher method',
       ext_modules = [module1])

