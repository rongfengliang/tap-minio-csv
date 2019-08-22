#!/usr/bin/env python

from setuptools import setup

setup(name='tap-minio-csv',
      version='1.2.1',
      description='Singer.io tap for extracting CSV files from minio',
      author='rongfengliang',
      url='https://github.com/rongfengliang',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_minio_csv'],
      install_requires=[
          'backoff==1.3.2',
          'boto3==1.9.57',
          'singer-encodings==0.0.3',
          'singer-python==5.1.5',
          'voluptuous==0.10.5'
      ],
      extras_require={
          'dev': [
              'ipdb==0.11'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-minio-csv=tap_minio_csv:main
      ''',
      packages=['tap_minio_csv'])
