#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from nose.tools import *  # PEP8 asserts
from nose.plugins.attrib import attr

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


class Test{{ cookiecutter.repo_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_feature(self):
        assert False, 'finish me'


if __name__ == '__main__':
    unittest.main()
