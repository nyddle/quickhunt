from requests.auth import HTTPBasicAuth
import requests

payload = {'from': 'Excited User <me@samples.mailgun.org>', 'to': 'nyddle@gmail.com', 'subject': 'value2', 'text': 'value2' }
r = requests.post("https://api.mailgun.net/v2/app8222672.mailgun.org/messages", auth=HTTPBasicAuth('api', 'key-9m9vuzkafbyjqhm9ieq71n0lu9dgf9b9'), data=payload)
print r

#API URL : https://api.mailgun.net/v2
#API Key : key-9m9vuzkafbyjqhm9ieq71n0lu9dgf9b9

"""
curl -s -k --user api:key-3ax6xnjp29jd6fds4gc373sgvjxteol0 \
    https://api.mailgun.net/v2/samples.mailgun.org/messages \
    -F from='Excited User <me@samples.mailgun.org>' \
    -F to=serobnic@mail.ru\
    -F to=sergeyo@profista.com \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomness!'
"""
