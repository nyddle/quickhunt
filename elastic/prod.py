#!/usr/bin/python
# -*- coding: utf8

import os
import json
import bson
import pymongo
from pymongo import Connection
import requests
from pyelasticsearch import ElasticSearch

connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
jobs_collection =  connection.app8222672.jobs

es = ElasticSearch('http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs')


"""
jobid = 1
for job in jobs_collection.find():
    job['id'] = str(job['_id'])
    job['_id'] = None
    r   = requests.post('http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs', data=json.dumps(job))
    print r.text
    #curl -XPOST http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs -d '{"title":"Hello world"}'
    jobid = jobid + 1

"""
b = es.search({
  "query" : {
    "text" : {
      "_all" : "scala"
    }
  }
})

qr = {
  "query" : {
    "text" : {
      "_all" : "scala"
    }
  }
}
query = { "query" : '{ "query" : { "text" : { "_all" : "scalaiascasc" } } }' }

b = requests.get('http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs/_search', data=json.dumps(qr))
print b.text

"""
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"mi_Ix5x0TtGLbK7cVXZJ5w","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"4S_w3rB-Qw2ms85-rTpzdg","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"lw1ziFGSSEajpDAQaK2L8w","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"qTdqgtYkRwykF94jYZ4rIA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"aK7fw0zvSJmFERGi476rVw","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"6HNADm2SRVSNSKdBu73AIA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"Ba9fIVh9ThS6alslsP07RQ","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"oqtgkljJQYijjWSjSBzVgA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"EWNw2omzQOepOYLSvOBbqw","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"JyZYXwQlQRy59liMqzp6Qw","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"Hr5KZsQURyWO5bYPCOa6CQ","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"DXvgZXPqTeSD0N3mj8tItg","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"3cdnQeOZRfy_9vDuA1cPKw","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"FPMcaCQ8THCppvoGoy99oA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"31cHY8E1Qm-qbEaE2svj3A","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"7ziQJvJSS7qgLZ4yzLZ5Hw","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"NMhdRWB8Tle1reF8DuP8Vg","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"Ervz9DfhTd6hDQ4airrd7g","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"a5YzfJIvTP2NQIegIngsSA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"99STQqxiSnCzqKy7j5YiZA","_version":1}
{"ok":true,"_index":"ixlr7zanrd8nute9d87g","_type":"jobs","_id":"8cd2dHyCRLmTzpS9TuX7yw","_version":1}


"""
