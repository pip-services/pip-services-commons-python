# -*- coding: utf-8 -*-
"""
    tests.refer.test_TypeReflector
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import importlib

from pip_services_commons.reflect import TypeDescriptor
from pip_services_commons.reflect import TypeReflector

from .TestClass import TestClass

class TestTypeReflector:

    def test_get_type(self):
        obj_type = TypeReflector.get_type("TypeCode", "pip_services_commons.convert")
        assert None != obj_type

        obj_type = TypeReflector.get_type("pip_services_commons.convert.TypeCode", "pip-services-common")
        assert None == obj_type

    def test_create_instance(self):
        value = TypeReflector.create_instance("TestClass", "reflect.TestClass")
        assert None != value
