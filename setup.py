'''setup file for libripoff

@author: moschlar
'''
from setuptools import setup

# Fix shutdown errors while installing
try:
    import multiprocessing  # @UnusedImport
    import logging  # @UnusedImport
except:
    pass

setup(
    name="libripoff",
    version="0.2.1",
    author="Christian Hundt, Moritz Schlarb",
    author_email="hundt.christian@gmail.com, mail@moritz-schlarb.de",
    description="simple library to detect plagiarism in source code",
    long_description=open('README.md').read(),
    license="BSD",
    url="https://github.com/gravitino/libripoff",
    packages=["ripoff"],
    test_suite='tests',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['numpy', 'hcluster', 'matplotlib'],
)
