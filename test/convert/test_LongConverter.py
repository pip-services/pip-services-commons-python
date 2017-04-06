# -*- coding: utf-8 -*-
"""
    tests.convert.test_LongConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.convert import LongConverter

class TestLongConverter:

    def test_to_long(self):
        assert 123L == LongConverter.to_long(123L)
        assert 123L == LongConverter.to_long(123.456)
        assert 123L == LongConverter.to_long("123")
        assert 123L == LongConverter.to_long("123.465")

        assert 123L == LongConverter.to_long_with_default(None, 123L)
        assert 0L == LongConverter.to_long_with_default(False, 123L)
        assert 123L == LongConverter.to_long_with_default("ABC", 123L)
