# -*- coding: utf-8 -*-
"""
    pip_services_commons.count.NullCounter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Null counter implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ICounters import ICounters
from .Timing import Timing
from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable

NullCountersDescriptor = Descriptor(
    "pip-services-commons", "counters", "null", "1.0"
)

class NullCounters(ICounters, IDescriptable):

    def get_descriptor(self):
        return NullCountersDescriptor

    def begin_timing(self, name):
        return Timing()

    def stats(self, name, value):
        pass

    def last(self, name, value):
        pass

    def timestamp_now(self, name):
        pass

    def timestamp(self, name, value):
        pass

    def increment_one(self, name):
        pass

    def increment(self, name, value):
        pass
