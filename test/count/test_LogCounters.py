# -*- coding: utf-8 -*-
"""
    tests.logs.test_LogCounters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.refer import ReferenceSet
from pip_services_commons.log import ConsoleLogger
from pip_services_commons.count import LogCounters
from .CountersFixture import CountersFixture

class TestLogCounters:

    counters = None
    fixture = None

    def setup_method(self, method):
        refs = ReferenceSet.from_list(ConsoleLogger())

        self.counters = LogCounters()
        self.counters.set_references(refs)

        self.fixture = CountersFixture(self.counters)

    def test_simple_counters(self):
        self.fixture.test_simple_counters()

    def test_measure_elapsed_time(self):
        self.fixture.test_measure_elapsed_time()
