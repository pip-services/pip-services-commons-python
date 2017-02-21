# -*- coding: utf-8 -*-
"""
    pip_services_commons.convert.DateTimeConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    DateTime conversion utilities
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from datetime import *
import iso8601

class DateTimeConverter(object):

    @staticmethod
    def to_nullable_datetime(value):
        # Shortcuts
        if value == None:
            return None
        if type(value) == datetime:
            return value 

        if type(value) in (int, float, long):
            return datetime.fromtimestamp(value)
        if type(value) == date:
            return datetime.combine(value, time(0,0,0))
        if type(value) == time:
            return datetime.combine(datetime.utcnow().date, value)
        
        try:
            value = str(value)
            return iso8601.parse_date(value)
        except:
            return None

    @staticmethod
    def to_datetime(value):
        return DateTimeConverter.to_datetime_with_default(value, None)

    @staticmethod
    def to_datetime_with_default(value, default_value):
        result = DateTimeConverter.to_nullable_datetime(value)
        return result if result != None else default_value
