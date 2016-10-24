# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.Closer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Closer component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IClosable import IClosable

class Closer:
    """
    Helper class that closes components
    """

    def close(self, correlation_id, components):
        """
        Closes components that implement ICloseable interface

        Args:
            correlation_id: a unique transaction id to trace calls across components
            components: a list of components to be closed
        """
        if components == None:
            return

        for component in components:
            if isinstance(component, IClosable):
                component.close(correlation_id)
