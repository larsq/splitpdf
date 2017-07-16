"""A setuptools based setup module."""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='splitpdf',
    version='0.0.1',
    url='https://github.com/larsq/splitpdf.git',
    author='Lars Eriksson',
    author_email='lars.q.eriksson@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    packages=['splitpdf'],
    install_requires=['PyPDF2'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pdf-split=splitpdf.cmd_split:main',
            'pdf-outline=splitpdf.cmd_outline:main'
        ],
    },
)
