# -*- coding: utf-8 -*-
"""
    pip_services_commons.refer.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    References module initialization
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

__all__ = [
    'Descriptor', 'IDescriptable', 'ILocateable', 
    'IReferenceable', 'IUnreferenceable', 'IReferences',
    'ReferenceException', 'Referencer', 'Reference',
    'ReferenceSet'
]

from .Descriptor import Descriptor
from .IDescriptable import IDescriptable
from .ILocateable import ILocateable
from .IReferenceable import IReferenceable
from .IUnreferenceable import IUnreferenceable
from .IReferences import IReferences
from .ReferenceException import ReferenceException
from .Referencer import Referencer
from .Reference import Reference
from .ReferenceSet import ReferenceSet