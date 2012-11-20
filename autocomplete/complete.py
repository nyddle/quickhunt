import urllib2
from redis_completion import RedisEngine
import urlparse
import redis


#url = urlparse.urlparse('redis://rediscloud:I3WJ70skVhVCfy6l@redis-18538.us-east-1-4.1.ec2.garantiadata.com:18538')
#r = redis.Redis(host=url.hostname, port=url.port, password=url.password)
#url = urlparse.urlparse('redis://:bSpyvbncbJCCMn6sjb@pikachu.ec2.myredis.com:6777')
#url = urlparse.urlparse('redis://redistogo:10a295ef108491d0667af6e893b13636@gar.redistogo.com:9362/')
#r = redis.Redis(host=url.hostname, port=url.port, password=url.password)

#engine = RedisEngine(prefix='stocks',host=url.hostname, port=url.port, password=url.password, db=0)
engine = RedisEngine()

#r = redis.StrictRedis(host='dns', port=port, db=0)

print "Connected"

def load_data():
    url = 'http://media.charlesleifer.com/downloads/misc/NYSE.txt'
    contents = urllib2.urlopen(url).read()
    for row in contents.splitlines()[1:]:
        print row
        ticker, company = row.split('\t')
        engine.store_json(ticker, company, {'ticker': ticker, 'company': company}) # id, search phrase, data

def search(p, **kwargs):
    return engine.search_json(p, **kwargs)

if __name__ == '__main__':
    print "Starting out"
    #engine.flush()
    print 'Loading data (may take a few seconds...)'
    load_data()

    print 'Search data by typing a partial phrase, like "uni sta"'
    print 'Type "q" at any time to quit'

    while 1:
        cmd = raw_input('? ')
        if cmd == 'q':
            break
        results = search(cmd)
        print 'Found %s matches' % len(results)
        for result in results:
            print '%s: %s' % (result['ticker'], result['company'])

