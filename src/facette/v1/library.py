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

"""
Library Interface
"""

from facette.connection import Connection
from facette.v1.collections import Collections
from facette.v1.graphs import Graphs
from facette.v1.scales import Scales
from facette.v1.sourcegroups import SourceGroups
from facette.v1.metricgroups import MetricGroups

class Library:
    def __init__(self, c):
        self.c = c
        self.collections = Collections(self.c)
        self.graphs = Graphs(self.c)
        self.scales = Scales(self.c)
        self.sourcegroups = SourceGroups(self.c)
        self.metricgroups = MetricGroups(self.c)

    def list(self):
        code, js = self.c.get("/api/v1/library/")
        print js
        return ""
        # o = None
        # if code == 200:
        #     o = Origins(js)
        # return code, o
