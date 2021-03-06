# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join
from setuptools import setup, find_packages
#  Fixes import error due to breaking change in pip 10
#  https://stackoverflow.com/a/49867265
#  pip > 10
try:
    from pip._internal.req import parse_requirements
#  pip < 10
except ImportError:
    from pip.req import parse_requirements
from blinkpy.helpers.constants import (
    __version__, PROJECT_PACKAGE_NAME, PROJECT_LICENSE, PROJECT_URL,
    PROJECT_EMAIL, PROJECT_DESCRIPTION, PROJECT_CLASSIFIERS, PROJECT_AUTHOR,
)

this_dir = abspath(dirname(__file__))

install_reqs = parse_requirements('{}/requirements.txt'.format(this_dir), session=False)
test_reqs = parse_requirements('{}/requirements_test.txt'.format(this_dir), session=False)
REQUIRES = [str(ir.req) for ir in install_reqs]
TEST_REQUIRES = [str(ir.req) for ir in test_reqs]

PACKAGES = find_packages(exclude=['tests*', 'docs'])

with open('{}/README.rst'.format(this_dir), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

name = PROJECT_PACKAGE_NAME
version = __version__

setup(
    name = PROJECT_PACKAGE_NAME,
    version = __version__,
    description = PROJECT_DESCRIPTION,
    long_description = long_description,
    author = PROJECT_AUTHOR,
    author_email = PROJECT_EMAIL,
    license = PROJECT_LICENSE,
    url = PROJECT_URL,
    platforms = 'any',
    py_modules = ['blinkpy'],
    packages=PACKAGES,
    include_package_data = True,
    install_requires = REQUIRES,
    test_suite = 'tests',
    classifiers = PROJECT_CLASSIFIERS
)
