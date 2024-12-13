# pip install requests
import requests

payload = {'k1':'v1'}

#r = requests.get('https://httpbin.org/get', params=payload)
r = requests.post('https://httpbin.org/post', data=payload)

print(r.status_code)
print(r.text)
print(r.json())




