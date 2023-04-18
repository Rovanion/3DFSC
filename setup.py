#!/usr/bin/env python

import pathlib

import pkg_resources
from setuptools import setup

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements_txt)
    ]



setup(name='3DFSC',
      version='3.0',
      description='Programs that deal with anisotropy, both resolution and sampling.',
      author='Philip Baldwin',
      author_email='pbaldwin@salk.edu',
      url='https://github.com/nysbc/Anisotropy',
      packages=['ThreeDFSC', 'ThreeDFSC.programs'],
      entry_points={
        'console_scripts': [ 'run3DFSC=ThreeDFSC.ThreeDFSC_Start:main']
      },
      install_requires=install_requires
     )
