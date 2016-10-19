# -*- coding: utf-8 -*-
"""
    pip_services_common.validate.ValidationException
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Validation exception type
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ValidationResultType import ValidationResultType
from .ValidationResult import ValidationResult
from ..errors.BadRequestException import BadRequestException

class ValidationException(BadRequestException):

    def __init__(self, correlation_id, results):
        message = ValidationException.compose_message(results)
        super(BadRequestException, self).__init__(correlation_id, 'INVALID_DATA', message)

    @staticmethod
    def compose_message(results):
        message = ''
        message += 'Validation failed'

        if results != None and len(results) > 0:
            first = True
            for result in results:
                if result.type != ValidationResultType.Information:
                    if not first: 
                        message += ': '
                    else:
                        message += ', '
                    message += result.message
                    first = False

        return message
