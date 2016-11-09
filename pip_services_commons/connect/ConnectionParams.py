# -*- coding: utf-8 -*-
"""
    pip_services_common.connect.ConnectionParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Connection parameters implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from ..config.ConfigParams import ConfigParams

class ConnectionParams(ConfigParams):
    """
    Connection parameters as set in component configuration or retrieved by discovery service. 
    It contains service protocol, host, port number, route, database name, timeouts 
    and additional configuration parameters.
    """

    def __init__(self, map = None):
        """
        Create an instance of service address with free-form configuration map.

        Args:
            content: a map with the address configuration parameters.
        """
        super(ConnectionParams, self).__init__(map)

    def use_discovery(self):
        """
        Checks if discovery registration or resolution shall be performed.
        The discovery is requested when 'discover' parameter contains
        a non-empty string that represents the discovery name.

        Returns: True if the address shall be handled by discovery
                 and False when all address parameters are defined statically.
        """
        return "discovery_key" in self

    def get_discovery_key(self):
        """
        Gets a key under which the connection shall be registered or resolved by discovery service.
        Returns: a key to register or resolve the connection
        """
        return self.get_as_nullable_string("discovery_key")

    def set_discovery_key(self, value):
        """
        Sets the key under which the connection shall be registered or resolved by discovery service

        Args:
            value: a key to register or resolve the connection
        """
        self.put("discovery_key", value)

    def get_protocol(self):
        """
        Gets the connection protocol
        Returns: the connection protocol
        """
        return self.get_as_nullable_string("protocol")

    def get_protocol(self, default_value = None):
        """
        Gets the connection protocol

        Args:
            default_value: the default protocol

        Returns: the connection protocol
        """
        return self.get_as_string_with_default("protocol", default_value)

    def set_protocol(self, value):
        """
        Sets the connection protocol

        Args:
            value: the connection protocol
        """
        self.put("protocol", value)

    def get_host(self):
        """
        Gets the service host name or IP address.
        Returns: a string representing service host
        """
        host = self.get_as_nullable_string("host")
        host = host if host != None else self.get_as_nullable_string("ip")
        return host

    def set_host(self, value):
        """
        Sets the service host name or IP address.

        Args:
            value: a string representing service host
        """
        self.put("host", value)

    def get_port(self):
        """
        Gets the service port number
        Returns: integer representing the service port.
        """
        return self.get_as_integer("port")

    def set_port(self, value):
        """
        Sets the service port number

        Args:
            value: integer representing the service port.
        """
        self.set_as_object("port", value)

    def get_uri(self):
        """
        Gets the endpoint uri constructed from protocol, host and port
        Returns: uri as <protocol>://<host | ip>:<port>
        """
        if self.get_protocol() == None:
            self.set_protocol("http")
        
        if self.get_host() == None:
            self.set_host("localhost")
        
        return self.get_protocol() + "://" + self.get_host() + ":" + str(self.get_port())

    @staticmethod
    def from_string(line):
        map = StringValueMap.from_string(line)
        return ConnectionParams(map)
