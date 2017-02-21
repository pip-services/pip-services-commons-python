# -*- coding: utf-8 -*-
"""
    tests.validate.test_PropertiesComparisonRule
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from .TestObject import TestObject
from pip_services_commons.validate import Schema
from pip_services_commons.validate import PropertiesComparisonRule

class TestPropertiesComparisonRule:

    def test_properties_comparison(self):
        obj = TestObject()
        schema = Schema().with_rule(PropertiesComparisonRule("String_Property", "EQ", "Null_Property"))

        obj.string_property = "ABC"
        obj.null_property = "ABC"
        results = schema.validate(obj)
        assert 0 == len(results)

        obj.null_property = "XYZ"
        results = schema.validate(obj)
        assert 1 == len(results)
