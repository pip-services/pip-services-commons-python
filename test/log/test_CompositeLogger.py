# -*- coding: utf-8 -*-
"""
    tests.log.test_CompositeLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.log import ConsoleLogger
from pip_services_commons.log import NullLogger
from pip_services_commons.log import CompositeLogger
from pip_services_commons.refer.ReferenceSet import ReferenceSet
from .LoggerFixture import LoggerFixture

class TestCompositeLogger:

    log = None
    fixture = None

    def setup_method(self, method):
        refs = ReferenceSet.from_list(ConsoleLogger(), NullLogger())

        self.log = CompositeLogger(refs)
        self.fixture = LoggerFixture(self.log)

    def test_log_level(self):
        self.fixture.test_log_level()

    def test_text_output(self):
        self.fixture.test_text_output()