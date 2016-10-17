# -*- coding: utf-8 -*-
"""
    tests.log.test_LogLevel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.log import LogLevel

class TestLogLevel:

    def test_to_log_level(self):
        assert LogLevel.to_log_level("1") == LogLevel.Fatal
        assert LogLevel.to_log_level("fatal") == LogLevel.Fatal

    def test_to_string(self):
        assert LogLevel.to_string(LogLevel.Fatal) == "FATAL"

    def test_to_integer(self):
        assert LogLevel.to_integer(LogLevel.Fatal) == 1