# -*- coding: utf-8 -*-
"""
    tests.config.test_JsonConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.config import JsonConfigReader

class TestJsonConfigReader:

    def test_read_config(self):
        config = JsonConfigReader.read_config(None, "data/config.json")
        
        assert 7 == len(config)
        assert 123 == config.get_as_integer("Field1.Field11")
        assert "ABC" == config.get_as_string("Field1.Field12")
        assert 123 == config.get_as_integer("Field2.0")
        assert "ABC" == config.get_as_string("Field2.1")
        assert 543 == config.get_as_integer("Field2.2.Field21")
        assert "XYZ" == config.get_as_string("Field2.2.Field22")
        assert True == config.get_as_boolean("Field3")
