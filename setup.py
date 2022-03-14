import setuptools

import byslib

setuptools.setup(
    name="byslib-python",
    version=byslib.__version__,
    url="https://bayashi-cl.github.io/byslib-python/",
    author="bayashi-cl",
    author_email="bayashi.cl@gmail.com",
    license="CC0",
    description="Python library for competitive programming",
    packages=setuptools.find_packages(exclude=("tests",)),
)
