# -*- coding: utf-8 -*-
"""
    pip_services_runtime.logs.MemoryCache
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Memory cache component implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import time
import threading

from .ICache import ICache
from .CacheEntry import CacheEntry
from ..config.IReconfigurable import IReconfigurable
from ..run.ICleanable import ICleanable

class MemoryCache(object, ICache, IReconfigurable, ICleanable):
    """
    Local in-memory cache that can be used in non-scaled deployments or for testing.
    
    Todo: Track access time for cached entries to optimize cache shrinking logic
    """

    _default_timeout = 60000
    _default_max_size = 1000

    _cache = None
    _count = None
    _timeout = None
    _max_size = None
    _lock = None

    def __init__(self):
        self._cache = {}
        self._count = 0
        self._max_size = self._default_max_size
        self._timeout = self._default_timeout
        self._lock = threading.Lock()

    def configure(self, config):
        self._timeout = config.get_as_long_with_default("options.timeout", self._default_timeout)
        self._max_size = config.get_as_long_with_default("options.max_size", self._default_max_size)

    def _cleanup(self):
        oldest = None
        self._count = 0
        
        # Cleanup obsolete entries and find the oldest
        for (key, entry) in self._cache.items():
            # Remove obsolete entry
            if entry.is_expired():
                self._cache.pop(key, None)
            # Count the remaining entry 
            else:
                self._count += 1
                if oldest == None or oldest.expiration > entry.expiration:
                    oldest = entry
        
        # Remove the oldest if cache size exceeded maximum
        if self._count > self._max_size and oldest != None:
            self._cache.pop(oldest.key, None)
            self._count -= 1

    def retrieve(self, correlation_id, key):
        self._lock.acquire()
        try:
            # Cache has nothing
            if key not in self._cache:
                return None
                
            # Get entry from the cache
            entry = self._cache[key]
                    
            # Remove entry if expiration set and entry is expired
            if entry.is_expired():
                self._cache.pop(key, None)
                self._count -= 1
                return None
            
            # Update access timeout
            return entry.value
        finally:
            self._lock.release()

    def store(self, correlation_id, key, value, timeout):
        timeout = timeout if timeout > 0 else self._default_timeout

        self._lock.acquire()
        try:
            entry = None
            if key in self._cache:
                entry = self._cache[key]

            # Shortcut to remove entry from the cache
            if value == None:
                if entry != None:
                    self._cache.pop(key, None)
                    self._count -= 1
                return None
            
            # Update the entry
            if entry != None:
                entry.set_value(value, timeout)
            # Or create a new entry 
            else:
                entry = CacheEntry(key, value, timeout)
                self._cache[key] = entry
                self._count += 1

            # Clean up the cache
            if self._max_size > 0 and self._count > self._max_size:
                self._cleanup()
            
            return value
        finally:
            self._lock.release()
    
    def remove(self, correlation_id, key):
        self._lock.acquire()
        try:
            # Get the entry
            entry = self._cache.pop(key, None)

            # Remove entry from the cache
            if entry != None:
                self._count -= 1
        finally:
            self._lock.release()
    
    def clear(self, correlation_id):
        self._lock.acquire()
        try:
            self._cache = {}
        finally:
            self._lock.release()
    