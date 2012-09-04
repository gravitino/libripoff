from setuptools import setup

setup(
    name = "libripoff",
    version = "0.1",
    author = "Christian Hundt, Moritz Schlarb",
    author_email = "hundt.christian@gmail.com, mail@moritz-schlarb.de",
    description = "simple library to detect plagiarism in source code",
    license = "BSD",
    url = "https://github.com/gravitino/libripoff",
    packages = ["ripoff"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires = ['numpy', 'matplotlib'],
)