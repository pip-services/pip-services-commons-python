# -*- coding: utf-8 -*-
"""
    pip_services_commons.cache.NullCache
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Null cache component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ICache import ICache

from ..refer.IDescriptable import IDescriptable
from ..refer.Descriptor import Descriptor

NullCacheDescriptor = Descriptor(
    "pip-services-commons", "cache", "null", "1.0"
)

class NullCache(ICache, IDescriptable):
    """
    Null cache component that doesn't do caching at all.
    It's mainly used in testing. However, it can be temporary
    used to disable cache to troubleshoot problems or study
    effect of caching on overall system performance. 
    """

    def get_descriptor(self):
        return NullCacheDescriptor
        

    def retrieve(self, correlation_id, key):
        return None

    def store(self, correlation_id, key, value, timeout):
        return value
    
    def remove(self, correlation_id, key):
        pass
