from facette.connection import *
from facette.utils import *
from facette.v1.graph import Graph
from facette.v1.plots import Plots
import json

class Graphs:
    def __init__(self, c):
        self.root = "/api/v1/library/graphs/"
        self.c = c
        self.plots = Plots(self.c)

    def list(self, collection=None, filter=None, limit=None, offset=None):
        payload = {}
        payload_add(payload, 'collection', collection)
        payload_add(payload, 'filter',     filter)
        payload_add(payload, 'limit',      limit)
        payload_add(payload, 'offset',     offset)
        code, js = self.c.get(self.root, payload)

        graphs = []
        if code == RESULT_OK:
            for x in js:
                g = Graph(x)
                graphs.append(g)
        return graphs

    def get(self, name):
        code, js = self.c.get(self.root + name)
        g = None
        if code == RESULT_OK:
            g = Graph(js)
        return g

    def add(self, c):
        payload = str(c)
        code, js = self.c.post(self.root, payload)
        return facette_http_status(code, RESULT_CREATED, js)

    def update(self, id, c):
        payload = str(c)
        code, js = self.c.put(self.root + id, payload)
        return facette_http_status(code, RESULT_OK, js)

    def delete(self, id):
        code, js = self.c.delete(self.root + id)
        return facette_http_status(code, RESULT_OK, js)
