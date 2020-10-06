#!/usr/bin/env python

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ncpa-nvidiasmi-plugin',
        python_requires='>3.5.2',
        version="0.1.0",
        author='Matt Cockayne',
        author_email='matt@phpboyscout.uk',
        license="MIT",
        zip_safe=True,
        packages=find_packages('src'),
        package_dir={'': 'src'},
        keywords="nagios ncpa nvidia smi gpu plugin",
        url='https://github.com/phpboyscout/ncpa-nvidiasmi-plugin',
        description='NCPA plugin to check Nvidia GPU status using nvidia-smi',
        long_description=readme(),
        install_requires=[
            "argparse",
            "nagiosplugin"],
        scripts=["check_nvidiasmi.py"],

)