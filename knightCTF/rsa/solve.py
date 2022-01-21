import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import os

priv_file = "gitlab"
flag = "flag.enc"

rsa_key_broken = open(priv_file, "rb").read()
rsa_key_broken_list = list(rsa_key_broken)

for i in range(256):
    print(i)
    for j in range(256): 
        for k in range(256): 
            for x in range(256):
                rsa_key_broken_list[(137 * 2) + 2] = i
                rsa_key_broken_list[(138 * 2) + 2] = j
                rsa_key_broken_list[(139 * 2) + 2] = k
                rsa_key_broken_list[(140 * 2) + 2] = x
                try: 
                 rsa_key = RSA.importKey(b''.join(rsa_key_broken_list))
                 enc_data = open(flag, 'r').read()
                 os.system('say "I hack it"')
                 print(rsa_key.decrypt(enc_data))
                except:
                    # print(".", end='')
                    pass
