# -*- coding: utf8
import sys

import os
import json
import bson
import pymongo
from pymongo import Connection
import urllib2
from redis_completion import RedisEngine
import urlparse
import redis

engine = RedisEngine()

connection = Connection('mongodb://quickhunt:qhpassword@alex.mongohq.com:10013/app8222672')
jobs_collection =  connection.app8222672.jobs


jobs = []
for job in jobs_collection.find():
    a = job['title']
    a = a.lower()
    for word in a.split():
        print word.encode('cp1251')



"""        
        jobs.append(word.encode('cp1251'))


map(engine.store, jobs)


if __name__ == '__main__':
    while(1):
        cmd = raw_input('? ')
        if cmd == 'q':
            break
        results = engine.search(cmd.decode('utf-8'))
        print results



for job in jobs_collection.find():
    a = job['title']
    a = a.lower()
    for word in a.split():
       print word.encode('cp1251')
       print engine.search(word)

"""
