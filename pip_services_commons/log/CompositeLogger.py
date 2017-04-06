# -*- coding: utf-8 -*-
"""
    pip_services_commons.log.CompositeLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Composite logger implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ILogger import ILogger
from .Logger import Logger
from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable
from ..refer.IReferenceable import IReferenceable

CompositeLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "composite", "1.0"
)

class CompositeLogger(Logger, IDescriptable, IReferenceable):
    _loggers = None

    def __init__(self, references = None):
        self._loggers = []

        if references != None:
            self.set_references(references)
            
    def get_descriptor(self):
        return CompositeLoggerDescriptor

    def set_references(self, references):
        descriptor = Descriptor(None, "logger", None, None)
        loggers = references.get_optional(descriptor)
        for logger in loggers:
            if isinstance(logger, ILogger):
                self._loggers.append(logger)

    def _write(self, level, correlation_id, error, message):
        for logger in self._loggers:
            logger.log(level, correlation_id, error, message)

