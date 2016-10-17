# -*- coding: utf-8 -*-
"""
    pip_services_commons.log.ConsoleLogger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Console logger implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import sys
import datetime

from .LogLevel import LogLevel
from .ILogger import ILogger
from .Logger import Logger
from ..refer.Descriptor import Descriptor
from ..refer.IDescriptable import IDescriptable

ConsoleLoggerDescriptor = Descriptor(
    "pip-services-commons", "logger", "console", "1.0"
)

class ConsoleLogger(Logger, IDescriptable):

    def get_descriptor(self):
        return ConsoleLoggerDescriptor

    def _compose_error(self, error):
        result = ""
        while (error != None):
            if (len(result) > 0):
                result += " Cause by error: "

            result += result + str(error) + " StackTrace: " + error.stack_trace

            error = error.__traceback__

        return result

    def _write(self, level, correlation_id, error, message):
        if (self._level < level):
            return

        output = "["
        output += correlation_id if correlation_id != None else "---"
        output += ":"
        output += LogLevel.to_string(level)
        output += ":"
        output += datetime.datetime.utcnow().isoformat()
        output += "] "

        output += message

        if (error != None):
            if (len(message) == 0):
                output += "Error: "
            else:
                output += ": "

            output += self._compose_error(error)

        output += "\n"

        if level >= LogLevel.Fatal and level <= LogLevel.Warn:
            sys.stderr.write(output)
        else:
            sys.stdout.write(output)