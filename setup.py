#/usr/bin/env python
import os
from setuptools import setup, find_packages
from polytester import __name__ as PACKAGE_NAME

DESCRIPTION = "A simple, easy-to-use multi-language test runner."
ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
VERSION = "1.0.2"

reqs = []
with open("requirements.txt", "r+") as f:
    for line in f.readlines():
        reqs.append(line.strip())

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
    try:
        import os
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
    except:
        long_description = DESCRIPTION + '\n'

setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=long_description,
    author="Steven Skoczen",
    author_email="skoczen@gmail.com",
    url="https://github.com/skoczen/polytester",
    version=VERSION,
    download_url = ['https://github.com/skoczen/polytester/tarball/%s' % VERSION, ],
    install_requires=reqs,
    packages=find_packages(),
    include_package_data=True,
    keywords = ["test", "multi-language", "nose", "karma", "jasmine", "rails", "runner", "junit"],
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': ['pt = polytester.main:main', 'polytester = polytester.main:main'],
    },

)
