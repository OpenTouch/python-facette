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

GROUP_ENTRY_ORIGIN  = "origin"
GROUP_ENTRY_PATTERN = "pattern"

class GroupEntry:
    def __init__(self, js=""):
        self.entry = {}
        self.origin  = facette_to_json(GROUP_ENTRY_ORIGIN,  js, self.entry)
        self.pattern = facette_to_json(GROUP_ENTRY_PATTERN, js, self.entry)

    def set(self, origin=None, pattern=None):
        self.origin  = facette_set(id, GROUP_ENTRY_ORIGIN,  self.entry)
        self.pattern = facette_set(id, GROUP_ENTRY_PATTERN, self.entry)

    def __str__(self):
        return json.dumps(self.entry)

    def __repr__(self):
        return str(self)
