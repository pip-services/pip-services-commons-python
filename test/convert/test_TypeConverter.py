# -*- coding: utf-8 -*-
"""
    tests.convert.test_TypeConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from pip_services_commons.convert import TypeCode
from pip_services_commons.convert import TypeConverter
from pip_services_commons.convert import DateTimeConverter

class TestTypeConverter:

    def test_to_type_code(self):
        assert TypeCode.String == TypeConverter.to_type_code(str)
        assert TypeCode.Integer == TypeConverter.to_type_code(int)
        assert TypeCode.Long == TypeConverter.to_type_code(long)
        assert TypeCode.Float == TypeConverter.to_type_code(float)
        assert TypeCode.DateTime == TypeConverter.to_type_code(datetime)
        assert TypeCode.Array == TypeConverter.to_type_code(list)
        assert TypeCode.Array == TypeConverter.to_type_code(tuple)
        assert TypeCode.Array == TypeConverter.to_type_code(set)
        assert TypeCode.Map == TypeConverter.to_type_code(dict)
        assert TypeCode.Object == TypeConverter.to_type_code(object)
        assert TypeCode.Unknown == TypeConverter.to_type_code(None)

        assert TypeCode.String == TypeConverter.to_type_code("123")
        assert TypeCode.Integer == TypeConverter.to_type_code(123)
        assert TypeCode.Long == TypeConverter.to_type_code(123L)
        assert TypeCode.Float == TypeConverter.to_type_code(123.456)
        assert TypeCode.DateTime == TypeConverter.to_type_code(datetime(1975, 4, 8))
        assert TypeCode.Array == TypeConverter.to_type_code([])
        assert TypeCode.Array == TypeConverter.to_type_code(())
        assert TypeCode.Map == TypeConverter.to_type_code({})
        assert TypeCode.Object == TypeConverter.to_type_code(TestTypeConverter)


    def test_to_nullable_type(self):
        assert "123" == TypeConverter.to_nullable_type(str, 123)
        assert 123 == TypeConverter.to_nullable_type(int, "123")
        assert 123L == TypeConverter.to_nullable_type(long, 123.456)
        assert 0.001 > 123 - TypeConverter.to_nullable_type(float, 123)
        assert DateTimeConverter.to_datetime("1975-04-08T17:30:00.00Z") == TypeConverter.to_nullable_type(datetime, "1975-04-08T17:30:00.00Z")
        assert 1 == len(TypeConverter.to_nullable_type(list, 123))
        assert 1 == len(TypeConverter.to_nullable_type(dict, {"abc": 123}))


    def test_to_type(self):
        assert "123" == TypeConverter.to_type(str, 123)
        assert 123 == TypeConverter.to_type(int, "123")
        assert 123L == TypeConverter.to_type(long, 123.456)
        assert 0.001 > 123 - TypeConverter.to_type(float, 123)
        assert DateTimeConverter.to_datetime("1975-04-08T17:30:00.00Z") == TypeConverter.to_type(datetime, "1975-04-08T17:30:00.00Z")
        assert 1 == len(TypeConverter.to_type(list, 123))
        assert 1 == len(TypeConverter.to_type(dict, {"abc": 123}))


    def test_to_type_with_default(self):
        assert "123" == TypeConverter.to_type_with_default(str, None, "123")
        assert 123 == TypeConverter.to_type_with_default(int, None, 123)
        assert 123L == TypeConverter.to_type_with_default(long, None, 123L)
        assert 0.001 > 123 - TypeConverter.to_type_with_default(float, None, 123.)
        assert DateTimeConverter.to_datetime("1975-04-08T17:30:00.00Z") == TypeConverter.to_type_with_default(datetime, "1975-04-08T17:30:00.00Z", None)
        assert 1 == len(TypeConverter.to_type_with_default(list, 123, None))
        assert 1 == len(TypeConverter.to_type_with_default(dict, {"abc":123}, None))
