#!/usr/bin/env python
from distutils.core import setup

setup(name='pidforest',
      version='0.1',
      description='PIDForest algorithm for anomaly detection ',
      author='vatsalsharan',
      author_email='',
      url='https://github.com/vatsalsharan/pidforest',
      packages=['pidforest'],
      install_requires=[
        "scikit-learn",
    "pandas",
    "numpy"]
     )

