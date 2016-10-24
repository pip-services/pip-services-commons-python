# -*- coding: utf-8 -*-
"""
    pip_services_common.refer.ReferenceException
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Reference exception type
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from ..errors.InternalException import InternalException

class ReferenceException(InternalException):
    """
    Exception thrown when required component is not found in references
    """

    def __init__(self, correlation_id = None, message = None):
        super(ReferenceException, self).__init__(correlation_id, "REF_ERROR", message)
