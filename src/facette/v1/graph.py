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
from facette.v1.graphgroup import GraphGroup
import json

GRAPH_ID           = "id"
GRAPH_NAME         = "name"
GRAPH_DESCRIPTION  = "description"
GRAPH_MODIFIED     = "modified"
GRAPH_TYPE         = "type"
GRAPH_STACK_MODE   = "stack_mode"
GRAPH_UNIT_LABEL   = "unit_label"
GRAPH_UNIT_TYPE    = "unit_type"
GRAPH_GROUPS       = "groups"

GRAPH_TYPE_AREA = 1
GRAPH_TYPE_LINE = 2

STACK_MODE_NONE = 1
STACK_MODE_NORMAL = 2
STACK_MODE_PERCENT = 3

UNIT_TYPE_FIXED = 1
UNIT_TYPE_METRIC = 2

class Graph:
    def __init__(self, js=""):
        self.graph = {}
        self.id          = facette_to_json(GRAPH_ID,          js, self.graph)
        self.name        = facette_to_json(GRAPH_NAME,        js, self.graph)
        self.description = facette_to_json(GRAPH_DESCRIPTION, js, self.graph)
        self.modified    = facette_to_json(GRAPH_MODIFIED,    js, self.graph)
        self.type        = facette_to_json(GRAPH_TYPE,        js, self.graph)
        self.stack_mode  = facette_to_json(GRAPH_STACK_MODE,  js, self.graph)
        self.unit_label  = facette_to_json(GRAPH_UNIT_LABEL,  js, self.graph)
        self.unit_type   = facette_to_json(GRAPH_UNIT_TYPE,   js, self.graph)

        self.groups = []
        if GRAPH_GROUPS in js:
            for x in js[GRAPH_GROUPS]:
                e = GraphGroup(x)
                self.groups.append(e)
        self.graph[GRAPH_GROUPS] = self.groups

    def set(self, id=None, name=None, description=None, type=None,
            stack_mode=None, unit_label=None, unit_type=None, groups=None):
        self.id           = facette_set(id,          GRAPH_ID,          self.graph)
        self.name         = facette_set(name,        GRAPH_NAME,        self.graph)
        self.description  = facette_set(description, GRAPH_DESCRIPTION, self.graph)
        self.type         = facette_set(type,        GRAPH_TYPE,        self.graph)
        self.stack_mode  = facette_set(stack_mode,  GRAPH_STACK_MODE,  self.graph)
        self.unit_label   = facette_set(unit_label,  GRAPH_UNIT_LABEL,  self.graph)
        self.unit_type    = facette_set(unit_type,    GRAPH_UNIT_TYPE,   self.graph)

        if groups:
            for x in groups:
                self.groups.append(x)

    def __str__(self):
        js = self.graph
        groups = []
        for g in self.groups:
            groups.append(json.loads(str(g)))
        js[GRAPH_GROUPS] = groups
        return json.dumps(js)

    def __repr__(self):
        return str(self)
