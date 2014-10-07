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

METRIC_NAME    = "name"
METRIC_ORIGINS = "origins"
METRIC_SOURCES = "sources"
METRIC_UPDATED = "updated"

class Metric:
    def __init__(self, js):
        self.metric = {}
        self.name    = facette_to_json(METRIC_NAME,    js, self.metric)
        self.origins = facette_to_json(METRIC_ORIGINS, js, self.metric)
        self.sources = facette_to_json(METRIC_SOURCES, js, self.metric)
        self.updated = facette_to_json(METRIC_UPDATED, js, self.metric)

    def __str__(self):
        return json.dumps(self.metric)
