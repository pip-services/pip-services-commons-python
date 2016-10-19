# -*- coding: utf-8 -*-
"""
    pip_services_commons.errors.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Errors module initialization
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

__all__ = [
    'ErrorCategory', 'ErrorDescription', 'ApplicationException',
    'UnknownException', 'InternalException', 'ConfigException',
    'InvalidStateException', 'ConnectionException', 'InvocationException',
    'FileException', 'BadRequestException', 'NotFoundException', 
    'UnauthorizedException', 'ConflictException', 'UnsupportedException'
]

from .ErrorCategory import ErrorCategory
from .ErrorDescription import ErrorDescription
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