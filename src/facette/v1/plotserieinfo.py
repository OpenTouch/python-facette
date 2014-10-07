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

PLOT_INFO_MIN   = "min"
PLOT_INFO_MAX   = "max"
PLOT_INFO_LAST  = "last"
PLOT_INFO_AVG   = "avg"

class PlotSerieInfo:
    def __init__(self, js=""):
        self.info = {}
        self.min    = facette_to_json(PLOT_INFO_MIN,  js, self.info)
        self.max    = facette_to_json(PLOT_INFO_MAX,  js, self.info)
        self.last   = facette_to_json(PLOT_INFO_LAST, js, self.info)
        self.avg    = facette_to_json(PLOT_INFO_AVG,  js, self.info)

    def __str__(self):
        return json.dumps(self.info)

    def __repr__(self):
        return str(self)
