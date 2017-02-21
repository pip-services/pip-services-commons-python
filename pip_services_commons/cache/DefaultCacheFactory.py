# -*- coding: utf-8 -*-
"""
    pip_services_commons.cache.DefaultCacheFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default cache factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .NullCache import NullCacheDescriptor
from .NullCache import NullCache
from .MemoryCache import MemoryCacheDescriptor
from .MemoryCache import MemoryCache

from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..build.IFactory import IFactory

DefaultCacheFactoryDescriptor = Descriptor(
    "pip-services-commons", "factory", "cache", "1.0"
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
