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
from facette.v1.plotserie import PlotSerie
import json

PLOT_ID           = "id"
PLOT_NAME         = "name"
PLOT_DESCRIPTION  = "description"
PLOT_TYPE         = "type"
PLOT_SERIES       = "series"
PLOT_STACK_MODE   = "stack_mode"
PLOT_START        = "start"
PLOT_END          = "end"
PLOT_STEP         = "step"
PLOT_MODIFIED     = "modified"
PLOT_UNIT_LABEL   = "unit_label"
PLOT_UNIT_TYPE    = "unit_type"

GRAPH_TYPE_AREA = 1
GRAPH_TYPE_LINE = 2

STACK_MODE_NONE = 1
STACK_MODE_NORMAL = 2
STACK_MODE_PERCENT = 3

class Plot:
    def __init__(self, js=""):
        self.plot = {}
        self.id          = facette_to_json(PLOT_ID,          js, self.plot)
        self.name        = facette_to_json(PLOT_NAME,        js, self.plot)
        self.description = facette_to_json(PLOT_DESCRIPTION, js, self.plot)
        self.type        = facette_to_json(PLOT_TYPE,        js, self.plot)
        self.stack_mode  = facette_to_json(PLOT_STACK_MODE,  js, self.plot)
        self.start       = facette_to_json(PLOT_START,       js, self.plot)
        self.end         = facette_to_json(PLOT_END,         js, self.plot)
        self.step        = facette_to_json(PLOT_STEP,        js, self.plot)
        self.modified    = facette_to_json(PLOT_MODIFIED,    js, self.plot)
        self.unit_label  = facette_to_json(PLOT_UNIT_LABEL,  js, self.plot)
        self.unit_type   = facette_to_json(PLOT_UNIT_TYPE,   js, self.plot)

        self.series = []
        if js.get(PLOT_SERIES):
            for x in js[PLOT_SERIES]:
                e = PlotSerie(x)
                self.series.append(e)
        self.plot[PLOT_SERIES] = self.series

    def __str__(self):
        js = self.plot
        series = []
        for s in self.series:
            series.append(json.loads(str(s)))
        js[PLOT_SERIES] = series
        return json.dumps(js)

    def __repr__(self):
        return str(self)
