# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.ILocateable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for components identified by locator object.
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class ILocateable:
    """
    Interface for components to provide check to match location 
    """

    def locate(self, locator):
        """
        Checks if locator matches the current component

        Args:
            locator: a location object. It can be standard Descriptor or something else

        Returns: True if component matches the locator or False otherwise.
        """
        raise NotImplementedError('Method from interface definition')
