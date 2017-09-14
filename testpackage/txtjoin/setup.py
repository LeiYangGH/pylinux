#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='txtjoin',
    version='1.0.0',
    description="Search all txt files under given directory recursively and"
    "combine their contents to one single txt file.",
    author="Yang Lei",
    author_email='675686066@qq.com',
    packages=[
        'txtjoin',
    ],
    package_dir={'txtjoin': 'txtjoin'},
    
    license="MIT license",
    zip_safe=False,
    keywords='txtjoin',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
