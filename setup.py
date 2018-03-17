#!/usr/bin/env python
"""
    Pip module setup
"""
from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

# Load in requirements from Pipfile
pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)

setup(name='plexcli',
      version='0.0.1',
      description='Plex CLI for configuration from the cli',
      url='http://github.com/michaeljs1990/plexcli',
      author='Michael Schuett',
      author_email='michaelj1990@gmail.com',
      license='MIT',
      install_requires=requirements,
      packages=["plexcli", "plexcli/cli"],
      entry_points={
        'console_scripts': [
            'plexcli=plexcli.cli.main:cli',
        ],
      },
      )  # end setup
