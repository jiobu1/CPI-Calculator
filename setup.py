#setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cpi", # the name that you will install via pip
    version="1.22",
    author="Jisha Obukwelu",
    author_email="jisha@lambdastudents.com",
    description="Converts monetary amounts either to present day values (2019) or historical values (1992-2018)",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jiobu1/CPI-Calculator",
    #keywords="",
    packages=find_packages() # ["CPI-Calculator"]
)
