secret = input("Enter your string to encrypt: ")

key = input("Enter the key: ")

secarr = []

keyarr = []

x = 0


def keyfunc(key, keyarr, x):
    for character in key:
        keyarr.append(ord(character))
    for i in keyarr:
        x += i


def secretfucn(secret, secarr, key, x):
    for character in secret:
        secarr.append(ord(character))

    for i in range(len(secarr)):
        if 97 <= secarr[i] <= 122:
            secarr[i] = secarr[i]-6
        else:
            if 65 <= secarr[i] <= 90:
                secarr[i] = secarr[i]-11

    if len(key) % 2 == 0:
        x = x + 1
    else:
        x = x + 3

    if x % 2 == 0:
        secarr[i] = secarr[i] + 3
    else:
        secarr[i] = secarr[i] + 2

    encrypted = ""

    for val in secarr:
        encrypted = encrypted + chr(val)
    print("Encrypted Text: " + encrypted)


keyfunc(key, keyarr, x)

secretfucn(secret, secarr, key, x)


# print(keyarr)
# print(x)


# enc_data = "IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu" #"6G:653"

# keys = ['T3NR1NG$', 'T3nR1ng$', 'TenRings', 'T3nR!ngs',
#         'T3nR!ng$', '73NR1GN$', '73nRing$', 'T3nR!nG$']


# def decrypt(secret, secarr, key, x):
#     for character in secret:
#         secarr.append(ord(character))

#     for i in range(len(secarr)):
#         if (97-6) <= secarr[i] <= (122-6):
#             secarr[i] = secarr[i]+6
#         else:
#             if (65-11) <= secarr[i] <= (90-11):
#                 secarr[i] = secarr[i]+11

#     if len(key) % 2 == 0:
#         x = x + 1
#     else:
#         x = x + 3

#     if x % 2 == 0:
#         secarr[i] = secarr[i] - 3
#     else:
#         secarr[i] = secarr[i] - 2

#     decrypted = ""

#     for val in secarr:
#         decrypted = decrypted + chr(val)
#     print("Encrypted Text: " + decrypted)


# for k in keys:
#     secarr = []
#     keyarr = []
#     x = 0
#     print(k)
#     decrypt(enc_data, secarr, k, x)

#     # KCTF{AREA51_TonyTheBadBoyGotScaredOfTheFatBos}



# 37n3vq6s45ch6731bn4pg6gh5tr2z76kf2nt5zc56a6w0