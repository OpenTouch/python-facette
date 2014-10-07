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
from facette.v1.groupentry import GroupEntry
import json

GROUP_ID           = "id"
GROUP_NAME         = "name"
GROUP_DESCRIPTION  = "description"
GROUP_MODIFIED     = "modified"
GROUP_ENTRIES      = "entries"

class Group:
    def __init__(self, js=""):
        self.group = {}
        self.id           = facette_to_json(GROUP_ID,          js, self.group)
        self.name         = facette_to_json(GROUP_NAME,        js, self.group)
        self.description  = facette_to_json(GROUP_DESCRIPTION, js, self.group)
        self.modified     = facette_to_json(GROUP_MODIFIED,    js, self.group)

        self.entries = []
        if GROUP_ENTRIES in js:
            for x in js[GROUP_ENTRIES]:
                e = GroupEntry(x)
                self.entries.append(e)
        self.group[GROUP_ENTRIES] = self.entries

    def set(self, id=None, name=None, description=None, entries=None):
        self.id           = facette_set(id,          GROUP_ID,          self.group)
        self.name         = facette_set(name,        GROUP_NAME,        self.group)
        self.description  = facette_set(description, GROUP_DESCRIPTION, self.group)
        if entries:
            for x in entries:
                self.entries.append(x)

    def __str__(self):
        js = self.group
        entries = []
        for e in self.entries:
            entries.append(json.loads(str(e)))
        js[GROUP_ENTRIES] = entries
        return json.dumps(js)

    def __repr__(self):
        return str(self)
