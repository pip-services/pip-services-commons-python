# -*- coding: utf-8 -*-
"""
    pip_services_commons.errors.ErrorDescription
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Log message implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import traceback

from .ErrorCategory import ErrorCategory
from .ApplicationException import ApplicationException
from .UnknownException import UnknownException
from .InternalException import InternalException
from .ConfigException import ConfigException
from .InvalidStateException import InvalidStateException
from .ConnectionException import ConnectionException
from .InvocationException import InvocationException
from .FileException import FileException
from .BadRequestException import BadRequestException
from .NotFoundException import NotFoundException
from .UnauthorizedException import UnauthorizedException
from .ConflictException import ConflictException
from .UnsupportedException import UnsupportedException

class ErrorDescription(object):
    category = None
    status = None
    code = None
    message = None
    details = None
    correlation_id = None
    cause = None
    stack_trace = None

    def __init__(self):
        pass

    def create_exception(self):
        error = None
        
        # Create well-known exception type based on error category
        if ErrorCategory.Unknown == self.category:
            error = UnknownException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.Internal == self.category:
            error = InternalException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.Misconfiguration == self.category:
            error = ConfigException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.NoResponse == self.category:
            error = ConnectionException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.FailedInvocation == self.category:
            error = InvocationException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.FileError == self.category:
            error = FileException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.BadRequest == self.category:
            error = BadRequestException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.Unauthorized == self.category:
            error = UnauthorizedException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.Conflict == self.category:
            error = ConflictException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.NotFound == self.category:
            error = NotFoundException(self.correlation_id, self.code, self.message)
        elif ErrorCategory.Unsupported == self.category:
            error = UnsupportedException(self.correlation_id, self.code, self.message)
        else:
            error = UnknownException()
            error.category = self.category
            error.status = self.status
        
        # Fill error with details
        error.details = self.details
        error.set_cause_string(self.cause)
        error.set_stack_trace_string(self.stack_trace)
        
        return error

    def to_json(self):
        return {
            'category': self.category,
            'status': self.status,
            'code': self.code,
            'message': self.message,
            'details': self.details,
            'correlation_id': self.correlation_id,
            'cause': self.cause,
            'stack_trace': self.stack_trace
        }

    @staticmethod
    def from_exception(ex):
        description = ErrorDescription()

        if isinstance(ex, ApplicationException):
            description.category = ex.category
            description.status = ex.status
            description.code = ex.code
            description.message = ex.message
            description.details = ex.details
            description.correlation_id = ex.correlation_id
            description.cause = ex.get_cause_string()
            description.stack_trace = ex.get_stack_trace_string()
        elif isinstance(ex, Exception):
            description.category = ErrorCategory.Unknown
            description.status = 500
            description.code = 'UNKNOWN'
            description.message = ex.message
            #description.cause = ex.xxx
            if hasattr(ex, 'tb_trace'):
                description.stack_trace = traceback.format_tb(ex)
        else:
            description.category = ErrorCategory.Unknown
            description.status = 500
            description.code = 'UNKNOWN'
            description.message = str(ex)

        return description

    @staticmethod
    def from_json(json):
        error = ErrorDescription()
        
        error.category = json['category']
        error.status = json['status']
        error.code = json['code']
        error.message = json['message']
        error.details = json['details']
        error.correlation_id = json['correlation_id']
        error.cause = json['cause']
        error.stack_trace = json['stack_trace']

        return error
