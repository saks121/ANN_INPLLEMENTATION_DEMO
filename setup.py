## we put setup related files here

from setuptools import setup

with open("README.md","r",encoding='utf-8') as f:
    long_description= f.read()


setup(
    name= "src",
    version="0.0.1",
    author="saksham",
    description= "A Simple package implementing ANN",
    long_description= long_description,
    long_description_content_type ="text/markdown",
    url ="https://github.com/saks121/ANN_INPLLEMENTATION_DEMO.git",
    author_email ="sakshamrajput72@gmail.com",
    packages=['src'],
    python_requires =">3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "pandas",
        "numpy"
    ]
)