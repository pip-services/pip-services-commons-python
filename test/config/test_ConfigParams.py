# -*- coding: utf-8 -*-
"""
    tests.config.test_ConfigParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.data import AnyValueMap
from pip_services_commons.data import AnyValueArray
from pip_services_commons.config import ConfigParams

class TestConfigParams:

    def test_config_sections(self):
        config = ConfigParams.from_tuples(
            "Section1.Key1", "Value1",
            "Section1.Key2", "Value2",
            "Section1.Key3", "Value3"
        )
        assert 3 == len(config)
        assert "Value1" == config.get("Section1.Key1")
        assert "Value2" == config.get("Section1.Key2")
        assert "Value3" == config.get("Section1.Key3")
        assert None == config.get("Section1.Key4")

        section2 = ConfigParams.from_tuples(
            "Key1", "ValueA",
            "Key2", "ValueB"
        )
        config.add_section("Section2", section2)
        assert 5 == len(config)
        assert "ValueA" == config.get("Section2.Key1")
        assert "ValueB" == config.get("Section2.Key2")

        sections = config.get_section_names()
        assert 2 == len(sections)
        assert "Section1" in sections
        assert "Section2" in sections
        
        section1 = config.get_section("section1")
        assert 3 == len(section1)
        assert "Value1" == section1.get("Key1")
        assert "Value2" == section1.get("Key2")
        assert "Value3" == section1.get("Key3")


    def test_config_from_string(self):
        config = ConfigParams.from_string("Queue=TestQueue;Endpoint=sb://cvctestbus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=K70UpCUXN1Q5RFykll6/gz4Et14iJrYFnGPlwiFBlow=")
        assert 4 == len(config)
        assert "TestQueue" == config.get("Queue")


    def test_config_from_object(self):
        value = AnyValueMap.from_tuples(
            "field1", ConfigParams.from_string("field11=123;field12=ABC"),
            "field2", AnyValueArray.from_values(
                123, "ABC", ConfigParams.from_string("field21=543;field22=XYZ")
            ),
            "field3", True
        )
        
        config = ConfigParams.from_value(value);
        assert 7 == len(config)
        assert 123 == config.get_as_integer("Field1.Field11")
        assert "ABC" == config.get_as_string("Field1.Field12")
        assert 123 == config.get_as_integer("Field2.0")
        assert "ABC" == config.get_as_string("Field2.1")
        assert 543 == config.get_as_integer("Field2.2.Field21")
        assert "XYZ" == config.get_as_string("Field2.2.Field22")
        assert True == config.get_as_boolean("Field3")
