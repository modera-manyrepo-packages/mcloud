from __future__ import print_function

import os
import sys
import imp

from setuptools import setup, find_packages

# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup(
    name='mcloud-plugin-haproxy',
    version='0.1',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    maintainer='Alex Rudakov',
    maintainer_email='ribozz@gmail.com',
    url='mcloud.io',
    description='Haproxy integration for mcloud',
    long_description=open('README.rst').read(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
    ],
    packages=['mcloud_haproxy'],
    install_requires=[
        'mcloud',
        'PyYAML'
    ],

    entry_points={
        'mcloud_plugins': [
            'haproxy = mcloud_haproxy:HaproxyPlugin'
        ]
    }
)
