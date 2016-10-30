# -*- coding: utf-8 -*-
"""
    tests.logs.test_NullCounters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.count import NullCounters

class TestNullCounters:

    counters = None

    def setup_method(self, method):
        self.counters = NullCounters()

    def test_simple_counters(self):
        self.counters.last("Test.LastValue", 123)
        self.counters.increment("Test.Increment", 3)
        self.counters.stats("Test.Statistics", 123)

    def test_measure_elapsed_time(self):
        timer = self.counters.begin_timing("Test.Elapsed")
        timer.end_timing()