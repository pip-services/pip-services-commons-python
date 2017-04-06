# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.IExecutable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for executable components
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IExecutable:
    """
    Interface for active components that can called to execute work.
    In contrast to IParamExecutable this interface does not require parameters
    """

    def execute(self, correlation_id):
        """
        Executes a unit of work

        Args:
            correlation_id: a unique transaction id to trace calls across components
        
        Returns: execution result

        Raises: ApplicationException on any error
        """
        raise NotImplementedError('Method from interface definition')
