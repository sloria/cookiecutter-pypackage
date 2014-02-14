# -*- coding: utf-8 -*-
import re
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


REQUIRES = [

]
PUBLISH_CMD = "python setup.py register sdist bdist_wheel upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist bdist_wheel upload -r test'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("{{ cookiecutter.repo_name }}/__init__.py")


if 'publish' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='{{ cookiecutter.repo_name }}',
    version=__version__,
    description='{{ cookiecutter.short_description }}',
    long_description=(read("README.rst") + '\n\n' +
                        read("HISTORY.rst")),
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=("test*", )),
    package_dir={'{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=[

    ],
    license=read("LICENSE"),
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={'test': PyTest}

)
