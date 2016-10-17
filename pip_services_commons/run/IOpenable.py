# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.IOpenable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for components that require explicit opening
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IOpenable:
    """
     Interface for components that require explicit opening
    """

    def open(self, correlation_id):
        """
        Opens component, establishes connections to services

        Args:
            correlation_id: a unique transaction id to trace calls across components
        """
        raise NotImplementedError('Method from interface definition')
