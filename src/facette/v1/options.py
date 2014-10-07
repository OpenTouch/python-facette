# Copyright (c) 2014 Alcatel-Lucent Enterprise
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from facette.utils import *
import json

OPTIONS_TITLE       = "title"
OPTIONS_SAMPLE      = "sample"
OPTIONS_RANGE       = "range"
OPTIONS_PERCENTILES = "percentiles"
OPTIONS_CONSTANTS   = "constants"

class Options:
    def __init__(self, js=""):
        self.options = {}
        self.title       = facette_to_json(OPTIONS_TITLE,       js, self.options)
        self.sample      = facette_to_json(OPTIONS_SAMPLE,      js, self.options)
        self.range       = facette_to_json(OPTIONS_RANGE,       js, self.options)
        self.percentiles = facette_to_json(OPTIONS_PERCENTILES, js, self.options)
        self.constants   = facette_to_json(OPTIONS_CONSTANTS,   js, self.options)

    def set(self, title=None, sample=None, range=None,
               percentiles=None, constants=None):
        self.title       = facette_set(title,       OPTIONS_TITLE,       self.options)
        self.sample      = facette_set(sample,      OPTIONS_SAMPLE,      self.options)
        self.range       = facette_set(range,       OPTIONS_RANGE,       self.options)
        self.percentiles = facette_set(percentiles, OPTIONS_PERCENTILES, self.options)
        self.constants   = facette_set(constants,   OPTIONS_CONSTANTS,   self.options)

    def __str__(self):
        return json.dumps(self.options)

    def __repr__(self):
        return str(self)

