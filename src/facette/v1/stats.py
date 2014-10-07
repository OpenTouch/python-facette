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

STAT_CATALOG_UPDATED = "catalog_updated"
STAT_GROUPS          = "groups"
STAT_COLLECTIONS     = "collections"
STAT_GRAPHS          = "graphs"
STAT_METRICS         = "metrics"
STAT_SOURCES         = "sources"
STAT_ORIGINS         = "origins"

class Stats:
    def __init__(self, js):
        self.stats = {}
        self.catalog_updated = facette_to_json(STAT_CATALOG_UPDATED, js, self.stats)
        self.groups          = facette_to_json(STAT_GROUPS,          js, self.stats)
        self.collections     = facette_to_json(STAT_COLLECTIONS,     js, self.stats)
        self.graphs          = facette_to_json(STAT_GRAPHS,          js, self.stats)
        self.metrics         = facette_to_json(STAT_METRICS,         js, self.stats)
        self.sources         = facette_to_json(STAT_SOURCES,         js, self.stats)
        self.origins         = facette_to_json(STAT_ORIGINS,         js, self.stats)

    def __str__(self):
        return json.dumps(self.stats)
