from facette.utils import *
import json

GRAPH_GROUP_SERIE_NAME   = "name"
GRAPH_GROUP_SERIE_ORIGIN = "origin"
GRAPH_GROUP_SERIE_SOURCE = "source"
GRAPH_GROUP_SERIE_METRIC = "metric"

class GraphGroupSerie:
    def __init__(self, js=""):
        self.serie = {}
        self.name   = facette_to_json(GRAPH_GROUP_SERIE_NAME,   js, self.serie)
        self.origin = facette_to_json(GRAPH_GROUP_SERIE_ORIGIN, js, self.serie)
        self.source = facette_to_json(GRAPH_GROUP_SERIE_SOURCE, js, self.serie)
        self.metric = facette_to_json(GRAPH_GROUP_SERIE_METRIC, js, self.serie)

    def set(self, name=None, origin=None, source=None, metric=None):
        self.name   = facette_set(name,   GRAPH_GROUP_SERIE_NAME,   self.serie)
        self.origin = facette_set(origin, GRAPH_GROUP_SERIE_ORIGIN, self.group)
        self.source = facette_set(source, GRAPH_GROUP_SERIE_SOURCE, self.group)
        self.metric = facette_set(metric, GRAPH_GROUP_SERIE_METRIC, self.group)

    def __str__(self):
        return json.dumps(self.serie)

    def __repr__(self):
        return str(self)
