# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.IParameterized
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for parameterized components
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

class IParameterized:
    """
    Interface for components that require parameters 
    """

    def close(self, correlation_id):
        """
        Sets component configuration parameters

        Args:
            parameters: configuration parameters

        Raises: ConfigException when configuration is wrong
        """
        raise NotImplementedError('Method from interface definition')
