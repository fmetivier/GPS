# -*- coding: utf-8 -*-

# Learn more: https://github.com/francoismetivier/setup.py

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="LibGPS",
    version="0.1.0",
    description="python scripts to handle gps data",
    long_description=readme,
    author="François Métivier",
    author_email="metivier@ipgp.fr",
    url="http://github.com/francoismetivier/libGPS",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
