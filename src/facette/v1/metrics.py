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

from facette.connection import Connection
from facette.utils import *
from facette.v1.metric import Metric
import json

class Metrics:
    def __init__(self, c):
        self.root = "/api/v1/catalog/metrics/"
        self.c = c

    def list(self, filter=None, limit=None, offset=None, origin=None, source=None):
        payload = {}
        payload_add(payload, 'filter', filter)
        payload_add(payload, 'limit',  limit)
        payload_add(payload, 'offset', offset)
        payload_add(payload, 'origin', origin)
        payload_add(payload, 'source', source)
        code, js = self.c.get(self.root, payload)
        return js

    def get(self, name):
        code, js = self.c.get(self.root + name)
        o = None
        if code == 200:
            o = Metric(js)
        return o
