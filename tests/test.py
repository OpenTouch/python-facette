#!/usr/bin/env python2.7

import os, sys
from facette.client import Facette
from facette.v1.collectionentry import CollectionEntry
from facette.v1.options import Options
from facette.v1.collection import Collection
from facette.v1.scale import Scale

# use UTF-8 encoding instead of unicode to support more characters
reload(sys)
sys.setdefaultencoding("utf-8")

srv = "http://demo.facette.io/"
fc = Facette(srv)

code = fc.server.reload()
print code
code, s = fc.server.stats()
print s
o = fc.catalog.origins.list(filter="glob:co*", limit=1)
print o
o = fc.catalog.origins.get('collectd')
print o
s = fc.catalog.sources.list()
print s
s = fc.catalog.sources.get('host1.example.net')
print s
m = fc.catalog.metrics.list()
print m
m = fc.catalog.metrics.get('cpu.0.user')
print m
c = fc.catalog.list()
print c
c = fc.library.collections.list()
print c
c = fc.library.collections.get('8c63a76b-3f62-4c8d-4954-b9338e0d144a')
print c
o = Options()
print o
o.set(title="opt title", percentiles=95)
print o
e = CollectionEntry()
e.set(id="123", options=o)
print e
c = Collection()
c.set(entries=[e])
fc.library.collections.add(c)

s = fc.library.scales.list()
print s
s = fc.library.scales.list_values()
print s
s = fc.library.scales.get('8895f732-8647-4f1f-79f4-0cb56afc6680')
print s
s = Scale()
s.set(name="My Scale", description="My Description", value="10")
fc.library.scales.add(s)

g = fc.library.sourcegroups.list()
print g
s = fc.library.sourcegroups.get('588bf36f-fb30-4800-40df-9e7c61f83ca6')
print s
g = fc.library.metricgroups.list()
print g
gr = fc.library.graphs.list()
for g in gr:
    print g
g = fc.library.graphs.get('44de3587-c2c7-49ff-698b-cbae8d2a0085')
print g

