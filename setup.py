#setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="consumer_price_index", # the name that you will install via pip
    version="1.0",
    author="Jisha Obukwelu",
    author_email="jisha@lambdastudents.com",
    description="Converts monetary amounts (from 1992) to present day values(2019)",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jiobu1/CPI-Calculator",
    #keywords="",
    packages=find_packages() # ["CPI-Calculator"]
)