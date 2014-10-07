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

from facette.connection import *
from facette.utils import *
from facette.v1.group import Group
import json

class MetricGroups:
    def __init__(self, c):
        self.root = "/api/v1/library/metricgroups/"
        self.c = c

    def list(self, filter=None, limit=None, offset=None):
        payload = {}
        payload_add(payload, 'filter',  filter)
        payload_add(payload, 'limit',   limit)
        payload_add(payload, 'offset',  offset)
        code, js = self.c.get(self.root, payload)

        groups = []
        if code == RESULT_OK:
            for x in js:
                g = Group(x)
                groups.append(g)
        return groups

    def get(self, name):
        code, js = self.c.get(self.root + name)
        g = None
        if code == RESULT_OK:
            g = Group(js)
        return g

    def add(self, s):
        payload = str(s)
        code, js = self.c.post(self.root, payload)
        return facette_http_status(code, RESULT_CREATED, js)

    def update(self, id, s):
        payload = str(s)
        code, js = self.c.put(self.root + id, payload)
        return facette_http_status(code, RESULT_OK, js)

    def delete(self, id):
        code, js = self.c.delete(self.root + id)
        return facette_http_status(code, RESULT_OK, js)
