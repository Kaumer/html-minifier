#!/usr/bin/env python

from distutils.core import setup, find_packages

minify = __import__('html_minifier')

setup(name='html minifier',
      version=minify.get_version(),
      description='a module for minify html',
      author='Leonardo orozco',
      url='https://github.com/Kaumer/html-minifier',
      packages=, find_packages(),
     )