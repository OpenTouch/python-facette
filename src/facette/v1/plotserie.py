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
from facette.v1.plotseriesummary import PlotSerieSummary
import json

PLOT_SERIE_NAME     = "name"
PLOT_SERIE_STACK_ID = "stack_id"
PLOT_SERIE_SUMMARY     = "summary"
PLOT_SERIE_PLOTS    = "plots"

class PlotSerie:
    def __init__(self, js=""):
        self.serie = {}
        self.name     = facette_to_json(PLOT_SERIE_NAME,     js, self.serie)
        self.stack_id = facette_to_json(PLOT_SERIE_STACK_ID, js, self.serie)
        self.plots    = facette_to_json(PLOT_SERIE_PLOTS,    js, self.serie)

        self.summary = {}
        if PLOT_SERIE_SUMMARY in js:
            self.summary = PlotSerieSummary(js[PLOT_SERIE_SUMMARY])
        self.serie[PLOT_SERIE_SUMMARY] = self.summary

    def __str__(self):
        js = self.serie
        summary = json.loads(str(self.summary))
        js[PLOT_SERIE_SUMMARY] = summary
        return json.dumps(js)

    def __repr__(self):
        return str(self)
