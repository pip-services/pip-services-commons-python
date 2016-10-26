# -*- coding: utf-8 -*-
"""
    pip_services_commons.reflect.MethodReflector
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Method reflector implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class MethodReflector:

    @staticmethod
    def _match_method(method, name):
        if method == None:
            return False
        if not callable(method):
            return False
        method_name = method.__name__
        if method_name.startswith("_"):
            return False
        return method_name.lower() == name.lower() 


    @staticmethod
    def has_method(obj, name):
        if obj == None:
            raise Exception("Object cannot be null")
        if name == None:
            raise Exception("Method name cannot be null")

        if not hasattr(obj, name):
            return False

        method = getattr(obj, name)
        return MethodReflector._match_method(method, name)


    @staticmethod
    def invoke_method(obj, name, *args):
        if obj == None:
            raise Exception("Object cannot be null")
        if name == None:
            raise Exception("Method name cannot be null")
        
        if not hasattr(obj, name):
            return None

        try:
            method = getattr(obj, name)
            if MethodReflector._match_method(method, name):
                return method(*args)
        except:
            pass
        
        return None


    @staticmethod
    def get_method_names(obj):
        methods = []
        
        for name in dir(obj):
            method = getattr(obj, name)
            if MethodReflector._match_method(method, name):
                methods.append(name)

        return methods
