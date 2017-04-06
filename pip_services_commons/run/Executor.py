# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.Executor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Executor component implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .IExecutable import IExecutable
from .IParamExecutable import IParamExecutable
from .Parameters import Parameters

class Executor:
    """
    Helper class that triggers execution for components
    """

    @staticmethod
    def execute(correlation_id, components, parameters = None):
        """
        Triggers execution for components that implement IExecutable and IParamExecutable interfaces
        and passes to IParamExecutable them set of parameters. 

        Args:
            correlation_id: a unique transaction id to trace calls across components
            components:  components a list of components to be notified
            parameters: a set of parameters to pass to executed components

        Returns: execution results
        """
        results = []

        if components == None:
            return

        parameters = parameters if parameters != None else Parameters()
        for component in components:
            if isinstance(component, IParamExecutable):
                results.append(component.execute(correlation_id, parameters))
            elif isinstance(component, INotifiable):
                results.appent(component.execute(correlation_id))

        return results
