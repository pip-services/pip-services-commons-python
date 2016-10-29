# -*- coding: utf-8 -*-
"""
    pip_services_commons.run.FixedRateTimer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Fixed rate timer implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import threading

from .INotifiable import INotifiable
from .IClosable import IClosable

class FixedRateTimer(IClosable):
    task = None
    delay = None
    interval = None
    started = False
    
    _timer = None
    _lock = None


    def __init__(self, task = None, interval = None, delay = None):
        self._lock = threading.Lock()

        self.task = task
        self.delay = delay
        self.interval = interval
        self.started = False


    def start(self):
        self._lock.acquire()
        try:
            # Stop previously set timer
            if self._timer != None:
                self._timer.cancel()
                self._timer = None
            
            # Set a new timer
            self._timer = threading.Timer(self.delay / 1000, self._timer_callback)
            
            # Set started flag
            self.started = True
        finally:
            self._lock.release()


    def _timer_callback(self):
        try:
            self._task.notify("pip-commons-timer")
        except
            # Ignore or better log
            pass

    def stop(self):
        self._lock.acquire()
        try:
            # Stop the timer
            if self._timer != None:
                self._timer.cancel()
                self._timer = None
            
            # Unset started flag
            self.started = False
        finally:
            self._lock.release()


    def close(self, correlation_id):
        self.stop()

