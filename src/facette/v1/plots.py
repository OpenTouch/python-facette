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
from facette.v1.plot import Plot
import json

class Plots:
    def __init__(self, c):
        self.root = "/api/v1/library/graphs/plots"
        self.c = c

    def get(self, name, range):
        payload = {}
        payload_add(payload, 'id', name)
        payload_add(payload, 'range',  range)
        code, js = self.c.post(self.root, json.dumps(payload))
        g = None
        if code == RESULT_OK:
            g = Plot(js)
        return g
