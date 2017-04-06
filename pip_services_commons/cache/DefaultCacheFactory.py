# -*- coding: utf-8 -*-
"""
    pip_services_commons.cache.DefaultCacheFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default cache factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .NullCache import NullCache
from .MemoryCache import MemoryCache

from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..build.IFactory import IFactory

DefaultCacheFactoryDescriptor = Descriptor(
    "pip-services-commons", "factory", "cache", "default", "1.0"
)

NullCacheDescriptor = Descriptor(
    "pip-services-commons", "cache", "null", "default", "1.0"
)

MemoryCacheDescriptor = Descriptor(
    "pip-services-commons", "cache", "memory", "default", "1.0"
)

class DefaultCacheFactory(object, IFactory, IDescriptable):

    def get_descriptor(self):
        return DefaultCacheFactoryDescriptor

    def can_create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullCacheDescriptor):
                return True

            if locator.match(MemoryCacheDescriptor):
                return True
            
        return False

    def create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullCacheDescriptor):
                return NullCache()

            if locator.match(MemoryCacheDescriptor):
                return MemoryCache()
            
        return None
