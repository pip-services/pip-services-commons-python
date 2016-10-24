# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.Opener
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Opener component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IOpenable import IOpenable

class Opener:
    """
    Helper class that opens a collection of components 
    """

    def open(self, correlation_id, components):
        """
        Opens component that implement IOpenable interface

        Args:
            correlation_id: a unique transaction id to trace calls across components
            components: a list of components to be opened
        """
        if components == None:
            return

        for component in components:
            if isinstance(component, IOpenable):
                component.open(correlation_id)
