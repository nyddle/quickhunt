import urllib2
from redis_completion import RedisEngine
import urlparse
import redis

engine = RedisEngine()
titles = ['python programming', 'programming c', 'unit testing python',
                  'testing software', 'software design']
map(engine.store, titles)


print engine.search('test')
