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

es = ElasticSearch('http://us-east-1.bonsai.io/e7hqscr8ce6v512dp8mg/')


jobid = 1
for job in jobs_collection.find():
    job['id'] = str(job['_id'])
    job['_id'] = None
    es.index("quickhunt", "jobs", job, jobid)
    #jobid = jobid + 1
    #print job 
#print es.refresh("testing")    
#print es.get('testing', 'jobs', 1)

#print es.search('name:joe OR name:freddy', index='testing')

#a = es.search("title:hello")
"""
b = es.search({
  "query" : {
    "text" : {
      "_all" : "scala"
    }
  }
})


print b
"""
"""
quickhunt
http://us-east-1.bonsai.io/e7hqscr8ce6v512dp8mg
"""

