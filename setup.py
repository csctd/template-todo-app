from setuptools import setup
from setuptools import find_packages

setup(
    name='todo',
    version='0.1.0',
    packages = find_packages(),
    install_requires=[
        'Click', 'pandas',
    ],


)
