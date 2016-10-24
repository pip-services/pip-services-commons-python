# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.ReferenceSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    ReferenceSet component implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import threading

from .IReferenceable import IReferenceable
from .IUnreferenceable import IUnreferenceable
from .IReferences import IReferences
from .Reference import Reference

class ReferenceSet(IReferences):
    """
    Basic implementation of IReferences that stores component as a flat list
    """

    _references = None
    _lock = None

    def __init__(self, *references):
        self._references = []
        self._lock = threading.Lock()

        if references != None:
            for reference in references:
                self.put(reference)


    def put(self, reference, locator = None):
        if reference == None:
            raise Exception("Reference cannot be null")

        self._lock.acquire()
        try:
            # If the reference is already the reference use it directly
            if isinstance(reference, Reference):
                self._references.append(reference)
            else:
                self._references.append(Reference(reference, locator))
        finally:
            self._lock.release()


    def remove(self, locator):
        if locator == None:
            return None

        self._lock.acquire()
        try:
            for reference in reversed(self._references):
                if reference.locate(locator):
                    self._references.remove(reference);
                    return reference.get_reference()
        finally:
            self._lock.release()
        
        return None


    def get_all(self):
        references = []
        
        self._lock.acquire()
        try:
            for reference in self._references:
                references.append(reference.get_reference())
        finally:
            self._lock.release()

        return references


    def _resolve_missing(self, locator):
        return None


    def get_optional(self, locator):
        if locator == None:
            raise Exception("Locator cannot be null")

        references = []
        
        self._lock.acquire()
        try:
            # Find all references that match the locator
            for reference in reversed(self._references):
                if reference.locate(locator):
                    references.append(reference.get_reference())
        finally:
            self._lock.release()

        return references


    def get_required(self, locator):
        references = self.get_optional(locator)
        print(references)
        self._lock.acquire()
        try:
            # Try to resolve missing dependency
            if len(references) == 0:
                reference = self.resolve_missing(locator)

                if reference != None:
                    references.append(reference)
        finally:
            self._lock.release()

        if len(references) == 0:
            raise ReferenceException(None, locator)

        return references


    def get_one_optional(self, locator):
        self._lock.acquire()
        try:
            # Find reference that matches the locator
            for reference in reversed(self._references):
                if reference.locate(locator):
                    return reference.get_reference()
        finally:
            self._lock.release()
            
        return None


    def get_one_required(self, locator):
        reference = self.get_one_optional(locator)

        self._lock.acquire()
        try:
            # Try to create a missing reference
            if reference == None:
                reference = self.resolve_missing(locator)
        finally:
            self._lock.release()

        if reference == None:
            raise ReferenceException(None, locator)

        return reference


    def get_one_before(self, prior, locator):
        if prior == None:
            raise Exception("Reference cannot be null")
        if locator == None:
            raise Exception("Locator cannot be null")
        
        self._lock.acquire()
        try:
            index = len(self._references) - 1
            
            # Locate prior reference
            while index >= 0:
                reference = self._references[index]
                index -= 1
                if reference.locate(prior):
                    break
            
            # Locate a reference 
            while index >= 0:
                reference = self._references[index]
                index -= 1
                if reference.locate(locator):
                    return reference.get_reference() 
        finally:
            self._lock.release()

        # Raise hard exception
        raise Exception(None, locator)


    @staticmethod
    def from_list(*references):
        return ReferenceSet(references)
