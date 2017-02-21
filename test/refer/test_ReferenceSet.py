# -*- coding: utf-8 -*-
"""
    tests.refer.test_ReferenceSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.refer import ReferenceSet

class TestDescriptor:

    def test_put(self):
        refs = ReferenceSet()
        refs.put("AAA", 111)
        refs.put("BBB", 222)
        refs.put("CCC", 333)
        refs.put("DDD", 444)
        assert 4 == len(refs.get_all())

    def test_get(self):
        refs = ReferenceSet()
        refs.put("AAA", 111)
        refs.put("BBB", 222)
        refs.put("CCC", 333)
        refs.put("DDD", 444)
        assert 4 == len(refs.get_all())
        
        item = refs.get_one_optional(555)
        assert None == item

        item = refs.get_one_required(111)
        assert "AAA" == item

        items = refs.get_optional(666)
        assert 0 == len(items)

        items = refs.get_required(333)
        assert 1 == len(items)

        item = refs.get_one_before(333, 111)
        assert "AAA" == item
