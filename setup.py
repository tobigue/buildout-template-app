#!/usr/bin/env python

from setuptools import setup


setup(name='projectname',
      version='0.0.1',
      description='',
      long_description=open('README.md', 'rt').read(),
      license='',
      author='',
      url='',

      install_requires=[
          'tornado'
      ],

      entry_points={
          'console_scripts': [
              'start_app = projectname.app:start_app',
          ]
      }
      )
