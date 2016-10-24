# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.Cleaner
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Cleaner component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ICleanable import ICleanable

class Cleaner:
    """
    Helper class that cleans components
    """

    def clear(self, correlation_id, components):
        """
        Cleans components that implement ICleanable interface

        Args:
            correlation_id: a unique transaction id to trace calls across components
            components: a list of components to be cleaned
        """
        if components == None:
            return

        for component in components:
            if isinstance(component, ICleanable):
                component.clear(correlation_id)
