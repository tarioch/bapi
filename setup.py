from setuptools import setup, find_packages
import ast
import os
import re

with open('bapi/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(re.search(
        r'__version__\s+=\s+(.*)',
        f.read().decode('utf-8')).group(1)))

def _read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path).read()

setup(
    version=VERSION,
    name='bapi',
    description='A Beancount REST API',
    long_description=_read('README.rst'),
    url='https://github.com/tarioch/bapi',
    author='Patrick Ruckstuhl',
    author_email='patrick@ch.tario.org',
    license='GPLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
    ],
    keywords='beancount rest api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3',
    install_requires=[
        'beancount',
        'flask',
        'flask-restplus',
        'click',
        'gitpython'
    ],
    entry_points={
        'console_scripts': [
            'bapi=bapi.app:main ',
        ],
    },
)

