import json
import json
import requests

key = ''
for i in range(10):
    res = requests.post('http://137.184.133.81:5000/api/request/auth_token')
    res.json())

print(key)