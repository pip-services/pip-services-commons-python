# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.Notifier
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Notifier component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .INotifiable import INotifiable
from .IParamNotifiable import IParamNotifiable
from .Parameters import Parameters

class Notifier:

    @staticmethod
    def notify(correlation_id, components, parameters = None):
        """
        Triggers notification for components that implement INotifiable and IParamParam interfaces
        and passes to IParamNotifiable them set of parameters.

        Args:
            correlation_id: a unique transaction id to trace calls across components
            components:  components a list of components to be notified
            parameters: a set of parameters to pass to notified components
        """
        if components == None:
            return

        parameters = parameters if parameters != None else Parameters()
        for component in components:
            if isinstance(component, IParamNotifiable):
                component.notify(correlation_id, parameters)
            elif isinstance(component, INotifiable):
                component.notify(correlation_id)
