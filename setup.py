#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

minify = __import__('html_minifier')

install_requires = []

if sys.version_info.major < 3 or sys.version_info.minor < 4:
    install_requires.append("pathlib")

setup(name='html-minifier',
      version=minify.get_version(),
      description='a module for minify html',
      author='Leonardo orozco',
      url='https://github.com/Kaumer/html-minifier',
      packages=find_packages(),
      install_requires=install_requires,
      keywords=['html', 'minifier'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Utilities']
      )
