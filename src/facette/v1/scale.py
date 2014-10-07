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

SCALE_ID           = "id"
SCALE_NAME         = "name"
SCALE_DESCRIPTION  = "description"
SCALE_MODIFIED     = "modified"
SCALE_VALUE        = "value"

class Scale:
    def __init__(self, js=""):
        self.scale = {}
        self.id           = facette_to_json(SCALE_ID,            js, self.scale)
        self.name         = facette_to_json(SCALE_NAME,          js, self.scale)
        self.description  = facette_to_json(SCALE_DESCRIPTION,   js, self.scale)
        self.modified     = facette_to_json(SCALE_MODIFIED,      js, self.scale)
        self.value        = facette_to_json(SCALE_VALUE,         js, self.scale)

    def set(self, id=None, name=None, description=None, value=None):
        self.id           = facette_set(id,          SCALE_ID,          self.scale)
        self.name         = facette_set(name,        SCALE_NAME,        self.scale)
        self.description  = facette_set(description, SCALE_DESCRIPTION, self.scale)
        self.value        = facette_set(value,       SCALE_VALUE,       self.scale)

    def __str__(self):
        return json.dumps(self.scale)

    def __repr__(self):
        return str(self)
