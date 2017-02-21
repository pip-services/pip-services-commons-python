# -*- coding: utf-8 -*-
"""
    tests.errors.test_ErrorDescription
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.errors import UnsupportedException
from pip_services_commons.errors import ErrorDescription
from pip_services_commons.errors import ErrorCategory

class TestApplicationException:

    def test_from_exception(self):
        error = UnsupportedException('123', 'TEST_ERROR', 'Test error')
        description = ErrorDescription.from_exception(error)
            
        assert ErrorCategory.Unsupported == description.category
        assert '123' == description.correlation_id
        assert 'TEST_ERROR' == description.code
        assert 'Test error' == description.message

    def test_create_exception(self):
        error = UnsupportedException('123', 'TEST_ERROR', 'Test error')
        description = ErrorDescription.from_exception(error)
            
        error = description.create_exception()

        assert isinstance(error, UnsupportedException)
        assert ErrorCategory.Unsupported == error.category
        assert '123' == error.correlation_id
        assert 'TEST_ERROR' == error.code
        assert 'Test error' == error.message
