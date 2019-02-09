#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

import csv_doli

setup(
    name='csv-doli',
    version=csv_doli.__version__,
    packages=find_packages(),
    author="Pewho Lewok",
    author_email="pewho@sudri.fr",
    description="Transforme le csv de la banque en quelque chose d'acceptable par Dolibear",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='http://github.com/pewho/',
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points = {
        'console_scripts': [
            'csv-doli = csv_doli.core:main',
        ],
    },
    license="MIT",
)
