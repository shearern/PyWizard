#!/usr/bin/python
'''
Setup script for deploying py_wizard
'''

from distutils.core import setup

VERSION='2.0.0'
PACKAGES=[
    'py_wizard',
    'py_wizard.console_wiz_iface',
    'py_wizard.questions',
    ]

setup(name='PyWizard',
      description="Nate's Pyton Wizard Library",
      author='Nathan Shearer',
      author_email='shearern@gmail.com',
      url='https://github.com/shearern/PyWizard',
      version=VERSION,
      packages=PACKAGES,
      )

