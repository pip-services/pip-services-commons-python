# -*- coding: utf-8 -*-
"""
    pip_services_commons.count.DefaultCountersFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default counters factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .NullCounters import NullCounters
from .LogCounters import LogCounters
from .CompositeCounters import CompositeCounters

from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..build.IFactory import IFactory

DefaultCountersFactoryDescriptor = Descriptor(
    "pip-services-commons", "factory", "counters", "default", "1.0"
)

NullCountersDescriptor = Descriptor(
    "pip-services-commons", "counters", "null", "default", "1.0"
)

LogCountersDescriptor = Descriptor(
    "pip-services-commons", "counters", "log", "default", "1.0"
)

CompositeCountersDescriptor = Descriptor(
    "pip-services-commons", "counters", "composite", "default", "1.0"
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
