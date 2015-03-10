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

import json
import requests

CONTENT_TYPE_JSON = 'application/json'
HEADER_X_TOTAL_RECORDS = 'X-Total-Records'

RESULT_OK = 200
RESULT_CREATED = 201
RESULT_BAD_REQUEST = 400
RESULT_NOT_FOUND = 404
RESULT_NOT_ALLOWED = 405
RESULT_CONFLICT = 409
RESULT_UNSUPPORTED = 415
RESULT_UNAVAILABLE = 503

class Connection:
    def __init__(self, root, user = None, passwd = None):
        self.root = root
        self.auth = None
        if user and passwd:
            self.auth = (user, passwd)
        self.headers = { 'content-type': CONTENT_TYPE_JSON }

    def get(self, uri, payload=None):
        r = requests.get(self.root + uri, auth=self.auth, params=payload)
        #if HEADER_X_TOTAL_RECORDS in r.headers:
        #    print r.headers[HEADER_X_TOTAL_RECORDS]
        if r.headers['content-type'].startswith(CONTENT_TYPE_JSON):
            return r.status_code, r.json()
        else:
            return r.status_code, r.text

    def post(self, uri, payload):
        r = requests.post(self.root + uri, data=payload,
                          auth=self.auth, headers=self.headers)
        if r.headers['content-type'].startswith(CONTENT_TYPE_JSON):
            return r.status_code, r.json()
        else:
            return r.status_code, r.text

    def put(self, uri, payload):
        r = requests.delete(self.root + uri, data=payload,
                          auth=self.auth, headers=self.headers)
        if r.headers['content-type'].startswith(CONTENT_TYPE_JSON):
            return r.status_code, r.json()
        else:
            return r.status_code, r.text

    def delete(self, uri):
        r = requests.delete(self.root + uri, auth=self.auth)
        if r.headers['content-type'].startswith(CONTENT_TYPE_JSON):
            return r.status_code, r.json()
        else:
            return r.status_code, r.text
