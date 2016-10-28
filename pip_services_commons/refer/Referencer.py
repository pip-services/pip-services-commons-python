# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.Referencer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Referencer component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IReferenceable import IReferenceable
from .IUnreferenceable import IUnreferenceable

class Referencer:
    """
    Helper class that assigns references to components
    """

    def set_references(self, references, components):
        """
        Assigns references to components that implement IReferenceable interface  

        Args:
            references: references to be assigned
            components: a list of components to assign references
        """
        if components == None:
            return

        for component in components:
            if isinstance(component, IReferenceable):
                component.set_references(references)

    def unset_references(self, components):
        """
        Clears references for components that implement IUnreferenceable interface

        Args:
            components: a list of components to clear references
        """
        if components == None:
            return

        for component in components:
            if isinstance(component, IUnreferenceable):
                component.unset_references(references)