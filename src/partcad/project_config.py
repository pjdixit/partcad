#
# OpenVMP, 2023
#
# Author: Roman Kuzmenko
# Created: 2023-08-19
#
# Licensed under Apache License, Version 2.0.

import os
import json
import yaml

DEFAULT_CONFIG_FILENAME = "partcad.yaml"


class Configuration:
    def __init__(self, config_path=DEFAULT_CONFIG_FILENAME):
        self.config_obj = {}
        self.config_dir = ""
        self.config_path = ""

        if os.path.isdir(config_path):
            config_path += "/" + DEFAULT_CONFIG_FILENAME
        if not os.path.isfile(config_path):
            print("PartCad configuration file is not found: %s" % config_path)
            return
        self.config_path = config_path

        self.config_dir = os.path.dirname(config_path)

        if config_path.endswith(".yaml"):
            self.config_obj = yaml.safe_load(open(config_path, "r"))
        if config_path.endswith(".json"):
            self.config_obj = json.load(open(config_path, "r"))
