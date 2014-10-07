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
from facette.v1.options import Options
import json

COLLECTION_ENTRY_ID        = "id"
COLLECTION_ENTRY_OPTIONS   = "options"

class CollectionEntry:
    def __init__(self, js=""):
        self.entry = {}
        self.id = facette_to_json(COLLECTION_ENTRY_ID, js, self.entry)
        self.options = None
        if COLLECTION_ENTRY_OPTIONS in js:
            self.options = Options(js[COLLECTION_ENTRY_OPTIONS])

    def set(self, id=None, options=None):
        self.title = facette_set(id, COLLECTION_ENTRY_ID, self.entry)
        if options:
            self.options = options

    def __str__(self):
        js = self.entry
        if self.options:
            js[COLLECTION_ENTRY_OPTIONS] = json.loads(str(self.options))
        return json.dumps(js)

    def __repr__(self):
        return str(self)
