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

PLOT_SUMMARY_MIN   = "min"
PLOT_SUMMARY_MAX   = "max"
PLOT_SUMMARY_LAST  = "last"
PLOT_SUMMARY_AVG   = "avg"

class PlotSerieSummary:
    def __init__(self, js=""):
        self.summary = {}
        self.min    = facette_to_json(PLOT_SUMMARY_MIN,  js, self.summary)
        self.max    = facette_to_json(PLOT_SUMMARY_MAX,  js, self.summary)
        self.last   = facette_to_json(PLOT_SUMMARY_LAST, js, self.summary)
        self.avg    = facette_to_json(PLOT_SUMMARY_AVG,  js, self.summary)

    def __str__(self):
        return json.dumps(self.summary)

    def __repr__(self):
        return str(self)
