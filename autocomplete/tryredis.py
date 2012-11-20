import os
import urlparse
import redis 
#url = urlparse.urlparse('redis://rediscloud:I3WJ70skVhVCfy6l@redis-18538.us-east-1-4.1.ec2.garantiadata.com:18538')
url = urlparse.urlparse('redis://:bSpyvbncbJCCMn6sjb@pikachu.ec2.myredis.com:6777')
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)

#r = redis.Redis(host='redis-18538.us-east-1-4.1.ec2.garantiadata.com', port=18538, db=0, password='quickhuntpass')
print url
print url.hostname
print url.password
print "connected"
r.set(u'','bar')
print r.get('foo')

