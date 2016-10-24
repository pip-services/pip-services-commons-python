# -*- coding: utf-8 -*-
"""
    tests.build.test_CompositeFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.build import CompositeFactory

class TestCompositeFactory:

    def test_can_create(self):
        factory = CompositeFactory()
        assert False == factory.can_create(111)