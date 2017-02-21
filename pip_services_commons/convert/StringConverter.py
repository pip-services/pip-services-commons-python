# -*- coding: utf-8 -*-
"""
    pip_services_commons.convert.StringConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    String conversion utilities
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class StringConverter(object):

    @staticmethod
    def to_nullable_string(value):
        if value == None:
            return None        
        return str(value)

    @staticmethod
    def to_string(value):
        return StringConverter.to_string_with_default(value, None)

    @staticmethod
    def to_string_with_default(value, default_value):
        result = StringConverter.to_nullable_string(value)
        return result if result != None else default_value
