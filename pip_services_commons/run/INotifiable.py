# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.INotifiable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for notifiable components
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class INotifiable:
    """
    Interface for active components that can be notified (called without expecting a result).
    In contrast to IParamNotifiable this interface does not require parameters
    """

    def notify(self, correlation_id):
        """
        Executes a unit of work

        Args:
            correlation_id: a unique transaction id to trace calls across components
        
        Raises: ApplicationException on any error
        """
        raise NotImplementedError('Method from interface definition')
