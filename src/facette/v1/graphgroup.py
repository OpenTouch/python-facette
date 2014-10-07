from facette.utils import *
from facette.v1.graphgroupserie import GraphGroupSerie
import json

GRAPH_GROUP_NAME     = "name"
GRAPH_GROUP_TYPE     = "type"
GRAPH_GROUP_STACK_ID = "stack_id"
GRAPH_GROUP_SERIES   = "series"

class GraphGroup:
    def __init__(self, js=""):
        self.group = {}
        self.name     = facette_to_json(GRAPH_GROUP_NAME,     js, self.group)
        self.type     = facette_to_json(GRAPH_GROUP_TYPE,     js, self.group)
        self.stack_id = facette_to_json(GRAPH_GROUP_STACK_ID, js, self.group)

        self.series = []
        if GRAPH_GROUP_SERIES in js:
            for x in js[GRAPH_GROUP_SERIES]:
                e = GraphGroupSerie(x)
                self.series.append(e)
        self.group[GRAPH_GROUP_SERIES] = self.series

    def set(self, name=None, type=None, stack_id=None, series=None):
        self.name      = facette_set(name,     GRAPH_GROUP_NAME,     self.group)
        self.type      = facette_set(type,     GRAPH_GROUP_TYPE,     self.group)
        self.stack_id  = facette_set(stack_id, GRAPH_GROUP_STACK_ID, self.group)
        if series:
            for x in series:
                self.series.append(x)

    def __str__(self):
        js = self.group
        series = []
        for s in self.series:
            series.append(json.loads(str(s)))
        js[GRAPH_GROUP_SERIES] = series
        return json.dumps(js)

    def __repr__(self):
        return str(self)
