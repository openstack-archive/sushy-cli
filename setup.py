#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="khansa amrouni",
    author_email='khansa.amrouni@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="a Redfish command line interface client tool built on top of sushy library to manage Redfish BMC resources.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sushycli',
    name='sushycli',
    packages=find_packages(include=['sushycli', 'sushycli.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/khansaAmrouni/sushycli',
    version='0.1.0',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sushycli = sushycli.main:main'
        ],
        'sushy.cli': [
            'version = sushycli.version:Version',
            'power_reset = sushycli.power_reset:PowerReset',
        ],
    },
)
