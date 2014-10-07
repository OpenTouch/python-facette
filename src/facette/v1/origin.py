from facette.utils import *
import json

ORIGIN_NAME      = "name"
ORIGIN_CONNECTOR = "connector"
ORIGIN_UPDATED   = "updated"

class Origin:
    def __init__(self, js):
        self.origin = {}
        self.name      = facette_to_json(ORIGIN_NAME,      js, self.origin)
        self.connector = facette_to_json(ORIGIN_CONNECTOR, js, self.origin)
        self.updated   = facette_to_json(ORIGIN_UPDATED,   js, self.origin)

    def __str__(self):
        return json.dumps(self.origin)
