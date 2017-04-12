# -*- coding: utf-8 -*-
"""
    tests.config.test_YamlConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.config import YamlConfigReader
from pip_services_commons.config import ConfigParams

class TestYamlConfigReader:

    def test_read_config(self):
        parameters = ConfigParams.from_tuples(
            "param1", "Test Param 1",
            "param2", "Test Param 2"
        )
        config = YamlConfigReader.read_config(None, "data/config.yaml", parameters)
        
        assert 9 == len(config)
        assert 123 == config.get_as_integer("Field1.Field11")
        assert "ABC" == config.get_as_string("Field1.Field12")
        assert 123 == config.get_as_integer("Field2.0")
        assert "ABC" == config.get_as_string("Field2.1")
        assert 543 == config.get_as_integer("Field2.2.Field21")
        assert "XYZ" == config.get_as_string("Field2.2.Field22")
        assert True == config.get_as_boolean("Field3")
        assert "Test Param 1" == config.get_as_string("Field4")
        assert "Test Param 2" == config.get_as_string("Field5")
