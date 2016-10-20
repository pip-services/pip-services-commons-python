# -*- coding: utf-8 -*-
"""
    tests.convert.test_IntegerConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.convert import IntegerConverter

class TestIntegerConverter:

    def test_to_integer(self):
        assert 123 == IntegerConverter.to_integer(123)
        assert 123 == IntegerConverter.to_integer(123.456)
        assert 123 == IntegerConverter.to_integer("123")
        assert 123 == IntegerConverter.to_integer("123.465")

        assert 123 == IntegerConverter.to_integer_with_default(None, 123)
        assert 0 == IntegerConverter.to_integer_with_default(False, 123)
        assert 123 == IntegerConverter.to_integer_with_default("ABC", 123)
