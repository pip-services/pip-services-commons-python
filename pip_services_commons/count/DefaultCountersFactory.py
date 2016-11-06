# -*- coding: utf-8 -*-
"""
    pip_services_commons.count.DefaultCountersFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default counters factory implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .NullCounters import NullCountersDescriptor
from .NullCounters import NullCounters
from .LogCounters import LogCountersDescriptor
from .LogCounters import LogCounters
from .CompositeCounters import CompositeCountersDescriptor
from .CompositeCounters import CompositeCounters

from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..build.IFactory import IFactory

DefaultCountersFactoryDescriptor = Descriptor(
    "pip-services-commons", "factory", "counters", "1.0"
)

class DefaultCountersFactory(object, IFactory, IDescriptable):

    def get_descriptor(self):
        return DefaultCountersFactoryDescriptor

    def can_create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullCountersDescriptor):
                return True

            if locator.match(LogCountersDescriptor):
                return True
            
            if locator.match(CompositeCountersDescriptor):
                return True

        return False

    def create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullCountersDescriptor):
                return NullCounters()

            if locator.match(LogCountersDescriptor):
                return LogCounters()
            
            if locator.match(CompositeCountersDescriptor):
                return CompositeCounters()

        return None
