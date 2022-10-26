#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='transcoder',
    version='1.0.0',
    url='https://github.com/chashtag/transcoder',
    author='chashtag',
    description='URL payload transcoder',
    packages=['transcoder'],
    install_requires=['lxml']
)