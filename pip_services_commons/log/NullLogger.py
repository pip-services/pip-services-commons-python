# -*- coding: utf-8 -*-
"""
    pip_services_commons.log.NullLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Null logger implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .LogLevel import LogLevel
from .ILogger import ILogger
from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable

NullLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "null", "1.0"
)

class NullLogger(ILogger, IDescriptable):

    def get_descriptor(self):
        return NullLoggerDescriptor

    def get_level(self):
        return LogLevel.Nothing

    def set_level(self, level):
        pass

    def log(self, level, correlation_id, error, message, *args, **kwargs):
        pass

    def fatal(self, correlation_id, error, message, *args, **kwargs):
        pass

    def error(self, correlation_id, error, message, *args, **kwargs):
        pass

    def warn(self, correlation_id, message, *args, **kwargs):
        pass

    def info(self, correlation_id, message, *args, **kwargs):
        pass

    def debug(self, correlation_id, message, *args, **kwargs):
        pass

    def trace(self, correlation_id, message, *args, **kwargs):
        pass

