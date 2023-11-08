from os import chdir, path, pardir
from setuptools import setup, find_packages

with open(path.join(path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

#Allow setup.py to be run from any path
chdir(path.normpath(path.join(path.abspath(__file__), pardir)))

setup(
    name="general-utils",
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    description="Utils package",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Joao Wiedehrkehr",
    author_email="jgpwieder@gmail.com",
    keywords=["utils"],
    install_requires=[
        "matplotlib~=2.2.5",
    ],
    version="1.0.0"
)
