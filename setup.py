#!/usr/bin/env python
from setuptools import setup

setup(
    name='skywise-insight',
    version='1.0.9',
    package_data={'': ['README.md']},
    packages=['skywiseinsight'],
    install_requires=[
        'skywise-rest-client>=1.0.7',
        'voluptuous>=0.8.8'
    ],

    # metadata for upload to PyPI
    author='Weather Decision Technologies',
    author_email='jstewart@wdtinc.com',
    description='SkyWise Insight API Python Client Library',
    url='https://github.com/wdtinc/skywise-insight-py',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
