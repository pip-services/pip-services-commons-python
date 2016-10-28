# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.IParamNotifiable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for notifiable components with parameters
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IParamNotifiable:
    """
    Interface for components that support parameterized one-way notification 
    """

    def notify(self, correlation_id, parameters):
        """
        Executes a unit of work with given parameters

        Args:
            correlation_id: a unique transaction id to trace calls across components
            parameters: a set of parameters for execution
        
        Raises: ApplicationException on any error
        """
        raise NotImplementedError('Method from interface definition')