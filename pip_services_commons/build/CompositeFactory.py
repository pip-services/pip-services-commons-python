# -*- coding: utf-8 -*-
"""
    pip_services_common.build.CompositeFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Composite factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IFactory import IFactory

class CompositeFactory(IFactory):
    _factories = None

    def __init__(self, *factories):
        self._factories = []
        for factory in factories:
            self._factories.append(factory)


    def add(self, factory):
        if factory == None:
            raise Exception("Factory cannot be null")
        
        self._factories.add(factory)


    def remove(self, factory):
        self._factories.remove(factory)


    def can_create(self, locator):
        if locator == None:
            raise Exception("Locator cannot be null")
        
        # Iterate from the latest factories
        for factory in reversed(self._factories):
            if factory.can_create(locator):
                return True
        
        return False


    def create(locator):
        if locator == None:
            raise Exception("Locator cannot be null")
        
        # Iterate from the latest factories
        for factory in reversed(self._factories):
            if factory.can_create(locator):
                return factory.create(locator)
        
        raise CreateException(None, "Cannot find factory for component " + locator)