# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.Reference
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Reference component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .ILocateable import ILocateable
from .IDescriptable import IDescriptable

class Reference(ILocateable):
    """
    Placeholder to store component references.
    """

    _locator = None
    _reference = None
    _locateableReference = None


    def __init__(self, reference, locator = None):
        if reference == None:
            raise Exception("Object reference cannot be null")
        
        self._reference = reference
        if (locator != None):
            self._locator = locator
        elif isinstance(reference, ILocateable):
            self._locateableReference = reference
        elif isinstance(reference, IDescriptable):
            self._locator = descriptable.get_descriptor()
        else:
            raise Exception("Reference must implement ILocateable or IDescriptable interface")


    def locate(self, locator):
        # Locate by direct reference matching
        if self._reference == locator:
            return True
        # Locate by type
        elif isinstance(locator, type):
            return isinstance(self._reference, locator)
        # Locate locateable objects
        elif self._locateableReference != None:
            return self._locateableReference.locate(locator)
        # Locate by direct locator matching
        else:
            return self._locator == locator

    def get_reference(self):
        return self._reference
