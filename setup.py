# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages
from setuptools import setup

import fastentrypoints

if not sys.version_info[0] == 3:
    sys.exit("Python 3 is required. Use: \'python3 setup.py install\'")

dependencies = ['messagepack']

config = {
    "version": "1.0",
    "name": "mpp",
    "url": "https://github.com/jakeogh/mpp",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "writes paths given as args to messagepacked bytes to stdout",
    "long_description": __doc__,
    "packages": find_packages(exclude=['tests']),
    "package_data": {"mpp": ['py.typed']},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "mpp=mpp.mpp:main",
        ],
    },
}

setup(**config)
