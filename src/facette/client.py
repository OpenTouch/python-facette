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
from facette.v1.server import Server
from facette.v1.catalog import Catalog
from facette.v1.library import Library

class Facette:
    def __init__(self, uri, user = None, passwd = None):
        self.uri = uri
        if self.uri.endswith('/'):
            self.uri = self.uri[:-1]
        self.user = user
        self.passwd = passwd
        self.c = Connection(self.uri, self.user, self.passwd)

        self.server = Server(self.c)
        self.catalog = Catalog(self.c)
        self.library = Library(self.c)
