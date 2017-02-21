# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomFloat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.random import RandomFloat

class TestRandomFloat:

    def test_next_float(self):
        value = RandomFloat.next_float(5)
        assert value < 5
        
        value = RandomFloat.next_float(2, 5)
        assert value < 5 and value > 2

    def test_update_float(self):
        value = RandomFloat.update_float(0, 5)
        
        assert value <= 5 and value >= -5
