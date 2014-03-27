#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sys
sys.path.append('./src')
sys.path.append('./tests')

setup(name='tdd-trial',
      version='0.1',
      packages=find_packages(),
      )
