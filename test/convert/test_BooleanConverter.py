# -*- coding: utf-8 -*-
"""
    tests.convert.test_BooleanConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.convert import BooleanConverter

class TestBooleanConverter:

    def test_to_boolean(self):
        assert BooleanConverter.to_boolean(True)
        assert BooleanConverter.to_boolean(1)
        assert BooleanConverter.to_boolean("True")
        assert BooleanConverter.to_boolean("yes")
        assert BooleanConverter.to_boolean("1")
        assert BooleanConverter.to_boolean("Y")

        assert not BooleanConverter.to_boolean(False)
        assert not BooleanConverter.to_boolean(0)
        assert not BooleanConverter.to_boolean("False")
        assert not BooleanConverter.to_boolean("no")
        assert not BooleanConverter.to_boolean("0")
        assert not BooleanConverter.to_boolean("N")

        assert not BooleanConverter.to_boolean(123)
        assert BooleanConverter.to_boolean_with_default("XYZ", True)
