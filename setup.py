from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

APP_NAME = 'GaussNBO'
AUTHOR = 'Sina Gilassi'
VERSION = '0.1.0'
EMAIL = "<sina.gilassi@gmail.com>"
DESCRIPTION = 'GaussNBO is a Python package for parsing Natural Bond Orbital (NBO) data from Gaussian log files.'
LONG_DESCRIPTION = 'GaussNBO is a Python package for parsing Natural Bond Orbital (NBO) data from Gaussian log files.'

# Setting up
setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    include_package_data=True,
    package_data={
        '': ['data/*.json', 'templates/*.html'],
    },
    license='MIT',
    install_requires=['jinja2',],
    keywords=['Python', 'Gaussian Software', 'Computational Chemistry',
              'NBO', 'Natural Bond Orbital', 'NBO Parser'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.10',
)
