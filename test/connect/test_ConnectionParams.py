# -*- coding: utf-8 -*-
"""
    tests.auth.test_ConnectionParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.connect import ConnectionParams
from pip_services_commons.auth import CredentialParams

class TestConnectionParams:

    def test_discovery(self):
        connection = ConnectionParams()
        connection.set_discovery_key(None)
        assert None == connection.get_discovery_key()
        
        connection.set_discovery_key("Discovery key value")
        assert "Discovery key value" == connection.get_discovery_key()
        assert True == connection.use_discovery()

    def test_protocol(self):
        connection = ConnectionParams()
        connection.set_protocol(None)
        assert None == connection.get_protocol()
        assert None == connection.get_protocol(None)
        assert "https" == connection.get_protocol("https")
        
        connection.set_protocol("https")
        assert "https" == connection.get_protocol()

    def test_host(self):
        connection = ConnectionParams()
        assert None == connection.get_host()
        connection.set_host(None)
        assert None == connection.get_host()
        
        connection.set_host("localhost")
        assert "localhost" == connection.get_host()

    def test_port(self):
        connection = ConnectionParams()
        assert None == connection.get_host()
        
        connection.set_port(3000)
        assert 3000 == connection.get_port()

    def test_uri(self):
        connection = ConnectionParams()
        assert "http://localhost:0" == connection.get_uri()
        
        connection.set_protocol("https")
        connection.set_port(3000)
        connection.set_host("pipgoals")
        assert "https://pipgoals:3000" == connection.get_uri()
