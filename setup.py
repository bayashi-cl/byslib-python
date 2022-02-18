from setuptools import find_packages, setup

import byslib

setup(
    name="byslib",
    version=byslib.__version__,
    packages=find_packages(where="byslib"),
    author="Masaki Kobayash",
    author_email="bayashi.cl@gmail.com",
)
