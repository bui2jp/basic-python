import urllib.parse
import urllib.request
import json

payload = {"key1": 'value1', "key2": "value2"}

# url = 'https://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# print('####')
# print(url)
# print('####')

# GET
# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(r)

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'https://httpbin.org/post', data=payload, method='POST'
)
#POST
with urllib.request.urlopen(req) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)