# -*- coding: utf-8 -*-
"""
    pip_services_commons.config.JsonConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    JSON config reader implementation
    
    :copyright: Digital Living Software Corp. 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import os.path
import json 

from ..errors.FileException import FileException
from ..errors.ConfigException import ConfigException
from .ConfigParams import ConfigParams

class JsonConfigReader(object):
    
    @staticmethod
    def read_object(correlation_id, path):
        if path == None:
            raise ConfigException(correlation_id, "NO_PATH", "Missing config file path")
        
        if not os.path.isfile(path):
            raise FileException(correlation_id, 'FILE_NOT_FOUND', 'Config file was not found at ' + path)
        
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except Exception as ex:
            raise FileException(
                correlation_id,
                "READ_FAILED",
                "Failed reading configuration " + path + ": " + str(ex)
            ).with_details("path", path).with_cause(ex)


    @staticmethod
    def read_config(correlation_id, path):
        value = JsonConfigReader.read_object(correlation_id, path)
        return ConfigParams.from_value(value)
