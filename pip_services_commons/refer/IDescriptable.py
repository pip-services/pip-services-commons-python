# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.IDescriptable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for components identified by descriptor.
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IDescriptable:
    """
    Interface for components that are defined by component descriptor.
    """

    def get_descriptor(self):
        """
        Gets the component descriptor object.

        Returns: the component descriptor for this object.
        """
        raise NotImplementedError('Method from interface definition')
