# -*- coding: utf-8 -*-
"""
    pip_services_commons.log.DefaultLoggerFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default logger factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .NullLogger import NullLogger
from .ConsoleLogger import ConsoleLogger
from .CompositeLogger import CompositeLogger

from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..build.IFactory import IFactory

DefaultLoggerFactoryDescriptor = Descriptor(
    "pip-services-commons", "factory", "logger", "default", "1.0"
)

NullLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "null", "default", "1.0"
)

ConsoleLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "console", "default", "1.0"
)

CompositeLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "composite", "default", "1.0"
)

class DefaultLoggerFactory(object, IFactory, IDescriptable):

    def get_descriptor(self):
        return DefaultLoggerFactoryDescriptor

    def can_create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullLoggerDescriptor):
                return True

            if locator.match(ConsoleLoggerDescriptor):
                return True
            
            if locator.match(CompositeLoggerDescriptor):
                return True

        return False

    def create(self, locator):
        if isinstance(locator, Descriptor):
            if locator.match(NullLoggerDescriptor):
                return NullLogger()

            if locator.match(ConsoleLoggerDescriptor):
                return ConsoleLogger()
            
            if locator.match(CompositeLoggerDescriptor):
                return CompositeLogger()

        return None
