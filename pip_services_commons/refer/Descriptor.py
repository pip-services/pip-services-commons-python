# -*- coding: utf-8 -*-
"""
    pip_services_runtime.refer.Descriptor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Component descriptor implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from ..errors.ConfigException import ConfigException

class Descriptor(object):
    """
    Component descriptor used to find a component by its descriptive elements:
    - logical group: package or other logical group of components like 'pip-services-storage-blocks'
    - component type: identifies component interface like 'controller', 'services' or 'cache'
    - component id: identifies component internal content or implementation like 'memory', 'file' or 'mongodb', ...
    - implementation version: '1.0', '1.5' or '10.4'
    """

    _group = None
    _type = None
    _id = None
    _version = None
    
    def __init__(self, group, typ, id, version):
        """
        Creates instance of a component descriptor

        Args:
            group: logical group: 'pip-services-runtime', 'pip-services-logging'
            type: external type: 'cache', 'services' or 'controllers'
            id: internal content/implementation: 'memory', 'file' or 'memcached' 
            version: compatibility version: '1.0'. '1.5' or '10.4'
        """
        group = None if "*" == group else group 
        typ = None if "*" == typ else typ
        id  = None if "*" == id else id
        version = None if "*" == version else version
        
        self._group = group
        self._type = typ
        self._id = id
        self._version = version

    def get_group(self): 
        """
        Gets the component group
        Returns: the component group
        """
        return self._group 

    def get_type(self):
        """
        Gets the component type
        Returns: the component type
        """ 
        return self._type

    def get_id(self):
        """
        Gets the component id
        Returns: the component id
        """ 
        return self._id 

    def get_version(self):
        """
        Gets the implementation version
        Returns: the implementation version
        """ 
        return self._version 

    def match(self, descriptor):
        """
        Matches this descriptor to another descriptor.
        All '*' or null descriptor elements match to any other value.
        Specific values must match exactly.
         
        Args:
            descriptor: another descriptor to match this one.

        Returns: True if descriptors match or False otherwise. 
        """
        # Matching groups
        if self._group != None and descriptor.get_group() != None \
        and self._group != descriptor.get_group():
                return False

        # Matching types
        if self._type != None and descriptor.get_type() != None \
        and self._type != descriptor.get_type():
            return False

        # Matching id
        if self._id != None and descriptor.get_id() != None \
        and self._id != descriptor.get_id():
            return False

        # Matching versions
        if self._version != None and descriptor.get_version() != None \
        and self._version != descriptor.get_version():
            return False
        
        # All checks are passed...
        return True

    def __eq__(self, other):
        if isinstance(other, Descriptor):
            return self.match(other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return (self._group or "*") \
        + ":" + (self._type or "*") \
        + ":" + (self._id or "*") \
        + ":" + (self._version or "*")
    
    @staticmethod
    def from_string(value):
        if value == None or len(value) == 0:
            return None
                
        tokens = value.split(":")
        if len(tokens) != 4:
            raise ConfigException(
                None, "BAD_DESCRIPTOR", "Descriptor " + str(value) + " is in wrong format"
            ).with_details("descriptor", value)
            
        return Descriptor(tokens[0].strip(), tokens[1].strip(), tokens[2].strip(), tokens[3].strip())

