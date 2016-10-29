# -*- coding: utf-8 -*-
"""
    tests.run.test_Parameters
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.config import ConfigParams
from pip_services_commons.run import Parameters

class TestParameters:

    def test_defaults(self):
        result = Parameters.from_tuples(
            "value1", 123, 
            "value2", 234
        )
        defaults = Parameters.from_tuples(
            "value2", 432, 
            "value3", 345
        )
        result = result.set_defaults(defaults, False)
        assert 3 == len(result)
        assert 123 == result.get("value1")
        assert 234 == result.get("value2")
        assert 345 == result.get("value3")

    def test_override_recursive(self):
        result = Parameters.from_json(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 } }"
        )
        defaults = Parameters.from_json(
            "{ \"value2\": { \"value22\": 777, \"value23\": 333 }, \"value3\": 345 }"
        )
        result = result.set_defaults(defaults, True)

        assert 3 == len(result)
        assert 123 == result.get("value1")
        assert 345 == result.get("value3")

        deep_result = result.get_as_map("value2")
        assert 3 == len(deep_result)
        assert 111 == deep_result.get("value21")
        assert 222 == deep_result.get("value22")
        assert 333 == deep_result.get("value23")

    def test_override_with_nulls(self):
        result = Parameters.from_json(
            "{ \"value1\": 123, \"value2\": 234 }"
        )
        result = result.override(None, True)

        assert 2 == len(result)
        assert 123 == result.get("value1")
        assert 234 == result.get("value2")

    def test_get(self):
        config = Parameters.from_json(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 } }"
        )

        value = config.get("")
        assert None == value

        value = config.get("value1")
        assert 123 == value

        value = config.get("value2")
        assert None != value

        value = config.get("value3")
        assert None == value

        value = config.get("value2.value21")
        assert 111 == value

        value = config.get("value2.value31")
        assert None == value

        value = config.get("value2.value21.value211")
        assert None == value

        value = config.get("valueA.valueB.valueC")
        assert None == value


    def test_contains(self):
        config = Parameters.from_json(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 } }"
        )

        has = config.contains_key("")
        assert False == has

        has = config.contains_key("value1")
        assert True == has

        has = config.contains_key("value2")
        assert True == has

        has = config.contains_key("value3")
        assert False == has

        has = config.contains_key("value2.value21")
        assert True == has

        has = config.contains_key("value2.value31")
        assert False == has

        has = config.contains_key("value2.value21.value211")
        assert False == has

        has = config.contains_key("valueA.valueB.valueC")
        assert False == has

    def test_put(self):
        config = Parameters()
        
        config.put(None, 123)
        assert 0 == len(config)
        
        config.put("field1", 123)
        assert 1 == len(config)
        assert 123 == config.get("field1")

        config.put("field2", "ABC")
        assert 2 == len(config)
        assert "ABC" == config.get("field2")

        config.put("field2.field1", 123)
        assert "ABC" == config.get("field2")

        config.put("field3.field31", 456)
        assert 3 == len(config)
        sub_config = config.get_as_map("field3")
        assert None != sub_config
        assert 456 == sub_config.get("field31")
        
        config.put("field3.field32", "XYZ")
        assert "XYZ" == config.get("field3.field32")

    def test_from_config(self):
        config = ConfigParams.from_tuples(
            "field1.field11", 123,
            "field2", "ABC",
            "Field1.Field12", "XYZ"
        )
        
        params = Parameters.from_config(config)
        assert 2 == len(params)
        assert "ABC" == params.get("Field2")
        value = params.get_as_map("Field1")
        assert 2 == len(value)
        assert "123" == value.get("field11")
        assert "XYZ" == value.get("Field12")

