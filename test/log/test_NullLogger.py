# -*- coding: utf-8 -*-
"""
    tests.log.test_NullLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.log import NullLogger
from .LoggerFixture import LoggerFixture

class TestNullLogger:

    log = None
    fixture = None

    def setup_method(self, method):
        self.log = NullLogger()
        self.fixture = LoggerFixture(self.log)

    def test_log_level(self):
        self.fixture.test_log_level()

    def test_text_output(self):
        self.fixture.test_text_output()