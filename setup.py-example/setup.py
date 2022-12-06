#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Hello',
    version='1.0',
    description='Example package',
    author='Me',
    author_email='shakefu@gmail.com',
    packages=find_packages(),
    install_requires=[
        "requests"
        ],
    test_suite='nose.collector',
    tests_require=[
        "nose",
        ]
)
