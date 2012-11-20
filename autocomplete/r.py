# -*- coding: utf8

import urllib2
from redis_completion import RedisEngine
import urlparse
import redis

engine = RedisEngine()
titles = ['python programming', 'programming c', 'unit testing python', u'программирование'.decode('utf-8')]
map(engine.store, titles)




