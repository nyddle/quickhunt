# -*- coding: utf8

import os
import json
import bson
import pymongo
from pymongo import Connection
import urllib2
from redis_completion import RedisEngine
import urlparse
import redis

url = urlparse.urlparse('redis://:bSpyvbncbJCCMn6sjb@pikachu.ec2.myredis.com:6777')
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)


engine = RedisEngine(host=url.hostname, port=url.port, password=url.password)

connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
jobs_collection =  connection.app8222672.jobs


jobs = []
for job in jobs_collection.find():
    a = job['title']
    a = a.lower()
    for word in a.split():
        jobs.append(word)

print jobs
map(engine.store, jobs)
#print engine.search(query.decode('cp1252'))
"""
if __name__ == '__main__':
    print "Starting out"
        cmd = raw_input('? ')
        if cmd == 'q':
            break
        results = engine.search(cmd)
        print 'Found %s matches' % len(results)
        #for result in results:
        #    print '%s: %s' % (result['ticker'], result['company'])
"""
