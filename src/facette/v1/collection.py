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
from facette.v1.collectionentry import CollectionEntry
import json

COLLECTION_ID           = "id"
COLLECTION_NAME         = "name"
COLLECTION_DESCRIPTION  = "description"
COLLECTION_PARENT       = "parent"
COLLECTION_HAS_CHILDREN = "has_children"
COLLECTION_MODIFIED     = "modified"
COLLECTION_ENTRIES      = "entries"

class Collection:
    def __init__(self, js=""):
        self.collection = {}
        self.id           = facette_to_json(COLLECTION_ID,
                                            js, self.collection)
        self.name         = facette_to_json(COLLECTION_NAME,
                                            js, self.collection)
        self.description  = facette_to_json(COLLECTION_DESCRIPTION,
                                            js, self.collection)
        self.parent       = facette_to_json(COLLECTION_PARENT,
                                            js, self.collection)
        self.has_children = facette_to_json(COLLECTION_HAS_CHILDREN,
                                            js, self.collection)
        self.modified     = facette_to_json(COLLECTION_MODIFIED,
                                            js, self.collection)

        self.entries = []
        if COLLECTION_ENTRIES in js:
            for x in js[COLLECTION_ENTRIES]:
                e = CollectionEntry(x)
                self.entries.append(e)
        self.collection[COLLECTION_ENTRIES] = self.entries

    def set(self, id=None, name=None, description=None, parent=None,
            has_children=None, entries=None):
        self.id           = facette_set(id, COLLECTION_ID, self.collection)
        self.name         = facette_set(name, COLLECTION_NAME, self.collection)
        self.description  = facette_set(description,
                                        COLLECTION_DESCRIPTION, self.collection)
        self.parent       = facette_set(parent, COLLECTION_PARENT, self.collection)
        self.has_children = facette_set(has_children,
                                        COLLECTION_HAS_CHILDREN, self.collection)
        if entries:
            for x in entries:
                self.entries.append(x)

    def __str__(self):
        js = self.collection
        entries = []
        for e in self.entries:
            entries.append(json.loads(str(e)))
        js[COLLECTION_ENTRIES] = entries
        return json.dumps(js)

    def __repr__(self):
        return str(self)
