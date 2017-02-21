# -*- coding: utf-8 -*-
"""
    tests.convert.test_StringConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.convert import StringConverter

class TestStringConverter:

    def test_to_string(self):
        assert StringConverter.to_nullable_string(None) == None
        assert "xyz" == StringConverter.to_string("xyz")
        assert "123" == StringConverter.to_string(123)
        assert "True" == StringConverter.to_string(True)
        #assert "{ prop = xyz }" == StringConverter.to_string(new { prop = "xyz" }, "xyz"));

        assert "xyz" == StringConverter.to_string_with_default(None, "xyz")