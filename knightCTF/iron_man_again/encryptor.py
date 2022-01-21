import base64
# str1 = input("Enter text to encrypt: ")
# arr1 = []
# l_c = ''.join(chr(c) for c in range(97, 123))
# u_c = ''.join(chr(c) for c in range(65, 91))
# l_e = l_c[13:] + l_c[:13]
# u_e = u_c[13:] + u_c[:13]
# so = ""
# for c in str1:
#     if c in l_c:
#         so = so + l_e[l_c.find(c)]
#     elif c in u_c:
#         so = so + u_e[u_c.find(c)]
#     else:
#         so = so + c
# d1 = {"A": "~",
#       "B": "`",
#       "C": "@",
#       "D": "#",
#       "E": "$",
#       "F": "%",
#       "G": "^",
#       "H": "&",
#       "I": "*",
#       "J": "(",
#       "K": ")",
#       "L": "-",
#       "M": "_",
#       "N": "=",
#       "O": "+",
#       "P": "{",
#       "Q": "[",
#       "R": "]",
#       "S": ":",
#       "T": ";",
#       "U": "\'",
#       "V": "\"",
#       "W": ",",
#       "X": "<",
#       "Y": ".",
#       "Z": ">",
#       "a": "?",
#       "b": "/",
#       "c": "5",
#       "d": "1",
#       "e": "3",
#       "f": "2",
#       "g": "4",
#       "h": "9",
#       "i": "0",
#       "j": "8",
#       "k": "6",
#       "l": "7",
#       "m": "K",
#       "n": "Q",
#       "o": "F",
#       "p": "V",
#       "q": "X",
#       "r": "D",
#       "s": "S",
#       "t": "A",
#       "u": "J",
#       "v": "N",
#       "w": "M",
#       "x": "P",
#       "y": "I",
#       "z": "T",
#       "~": "A",
#       "`": "B",
#       "@": "C",
#       "#": "D",
#       "$": "E",
#       "%": "F",
#       "^": "G",
#       "&": "H",
#       "*": "I",
#       "(": "J",
#       ")": "K",
#       "-": "L",
#       "_": "M",
#       "=": "N",
#       "+": "O",
#       "{": "P",
#       "[": "Q",
#       "]": "R",
#       ":": "S",
#       ";": "T",
#       "\'": "U",
#       "\"": "V",
#       ",": "W",
#       "<": "X",
#       ".": "Y",
#       ">": "Z",
#       "?": "a",
#       "/": "b",
#       "5": "c",
#       "1": "d",
#       "3": "e",
#       "2": "f",
#       "4": "g",
#       "9": "h",
#       "0": "i",
#       "8": "j",
#       "6": "k",
#       "7": "l",
#       }
# vas1 = ""

# for i in so:
#     scr1 = str(d1.get(i))
#     vas1 += str(scr1)
# for c in vas1:
#     arr1.append(ord(c))
# arr2 = []
# for i in arr1:
#     if i % 2 == 0:
#         i += 2
#     else:
#         i += 1
#     arr2.append(i)
# saa2t = ""
# for c in arr2:
#     saa2t += chr(c)
# d2 = {"~": "A",
#       "`": "B",
#       "@": "C",
#       "#": "D",
#       "$": "E",
#       "%": "F",
#       "^": "G",
#       "&": "H",
#       "*": "I",
#       "(": "J",
#       ")": "K",
#       "-": "L",
#       "_": "M",
#       "=": "N",
#       "+": "O",
#       "{": "P",
#       "[": "Q",
#       "]": "R",
#       ":": "S",
#       ";": "T",
#       "\'": "U",
#       "\"": "V",
#       ",": "W",
#       "<": "X",
#       ".": "Y",
#       ">": "Z",
#       "?": "a",
#       "/": "b",
#       "5": "c",
#       "1": "d",
#       "4": "e",
#       "2": "f",
#       "3": "g",
#       "9": "h",
#       "0": "i",
#       "8": "j",
#       "6": "k",
#       "7": "l",
#       "K": "m",
#       "Q": "n",
#       "F": "o",
#       "V": "p",
#       "X": "q",
#       "D": "r",
#       "S": "s",
#       "A": "t",
#       "J": "u",
#       "N": "v",
#       "M": "w",
#       "P": "x",
#       "I": "y",
#       "T": "z",
#       "A": "~",
#       "B": "`",
#       "C": "*",
#       "D": "#",
#       "E": "$",
#       "F": "%",
#       "G": "^",
#       "H": "&",
#       "I": "@",
#       "J": "(",
#       "K": ")",
#       "L": "-",
#       "M": "_",
#       "N": "=",
#       "O": "+",
#       "P": "{",
#       "Q": "[",
#       "R": "]",
#       "S": ":",
#       "T": ";",
#       "U": "\'",
#       "V": "\"",
#       "W": ",",
#       "X": "<",
#       "Y": ".",
#       "Z": ">",
#       "a": "?",
#       "b": "/",
#       "c": "5",
#       "d": "7",
#       "e": "3",
#       "f": "2",
#       "g": "4",
#       "h": "9",
#       "i": "0",
#       "j": "8",
#       "k": "6",
#       "l": "1",
#       }
# vas2 = ""
# for i in saa2t:
#     scr2 = str(d2.get(i))
#     vas2 += str(scr2)
# sarev = vas2[::-1]
# msg_b = sarev.encode("ascii")
# b64_bytes = base64.b64encode(msg_b)
# b64_string = b64_bytes.decode("ascii")
# print(b64_string)

d1 = {"A": "~",
      "B": "`",
      "C": "@",
      "D": "#",
      "E": "$",
      "F": "%",
      "G": "^",
      "H": "&",
      "I": "*",
      "J": "(",
      "K": ")",
      "L": "-",
      "M": "_",
      "N": "=",
      "O": "+",
      "P": "{",
      "Q": "[",
      "R": "]",
      "S": ":",
      "T": ";",
      "U": "\'",
      "V": "\"",
      "W": ",",
      "X": "<",
      "Y": ".",
      "Z": ">",
      "a": "?",
      "b": "/",
      "c": "5",
      "d": "1",
      "e": "3",
      "f": "2",
      "g": "4",
      "h": "9",
      "i": "0",
      "j": "8",
      "k": "6",
      "l": "7",
      "m": "K",
      "n": "Q",
      "o": "F",
      "p": "V",
      "q": "X",
      "r": "D",
      "s": "S",
      "t": "A",
      "u": "J",
      "v": "N",
      "w": "M",
      "x": "P",
      "y": "I",
      "z": "T",
      "~": "A",
      "`": "B",
      "@": "C",
      "#": "D",
      "$": "E",
      "%": "F",
      "^": "G",
      "&": "H",
      "*": "I",
      "(": "J",
      ")": "K",
      "-": "L",
      "_": "M",
      "=": "N",
      "+": "O",
      "{": "P",
      "[": "Q",
      "]": "R",
      ":": "S",
      ";": "T",
      "\'": "U",
      "\"": "V",
      ",": "W",
      "<": "X",
      ".": "Y",
      ">": "Z",
      "?": "a",
      "/": "b",
      "5": "c",
      "1": "d",
      "3": "e",
      "2": "f",
      "4": "g",
      "9": "h",
      "0": "i",
      "8": "j",
      "6": "k",
      "7": "l",
      }

for key, value in d1.items():
    d1[value] = key

d2 = {"~": "A",
      "`": "B",
      "@": "C",
      "#": "D",
      "$": "E",
      "%": "F",
      "^": "G",
      "&": "H",
      "*": "I",
      "(": "J",
      ")": "K",
      "-": "L",
      "_": "M",
      "=": "N",
      "+": "O",
      "{": "P",
      "[": "Q",
      "]": "R",
      ":": "S",
      ";": "T",
      "\'": "U",
      "\"": "V",
      ",": "W",
      "<": "X",
      ".": "Y",
      ">": "Z",
      "?": "a",
      "/": "b",
      "5": "c",
      "1": "d",
      "4": "e",
      "2": "f",
      "3": "g",
      "9": "h",
      "0": "i",
      "8": "j",
      "6": "k",
      "7": "l",
      "K": "m",
      "Q": "n",
      "F": "o",
      "V": "p",
      "X": "q",
      "D": "r",
      "S": "s",
      "A": "t",
      "J": "u",
      "N": "v",
      "M": "w",
      "P": "x",
      "I": "y",
      "T": "z",
      "A": "~",
      "B": "`",
      "C": "*",
      "D": "#",
      "E": "$",
      "F": "%",
      "G": "^",
      "H": "&",
      "I": "@",
      "J": "(",
      "K": ")",
      "L": "-",
      "M": "_",
      "N": "=",
      "O": "+",
      "P": "{",
      "Q": "[",
      "R": "]",
      "S": ":",
      "T": ";",
      "U": "\'",
      "V": "\"",
      "W": ",",
      "X": "<",
      "Y": ".",
      "Z": ">",
      "a": "?",
      "b": "/",
      "c": "5",
      "d": "7",
      "e": "3",
      "f": "2",
      "g": "4",
      "h": "9",
      "i": "0",
      "j": "8",
      "k": "6",
      "l": "1",
      }

for key, value in d1.items():
    d1[value] = key


# str1 = base64.b64decode('JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=').decode('utf-8')
# print(str1)


# arr1 = []
# l_c = ''.join(chr(c) for c in range(97, 123))
# u_c = ''.join(chr(c) for c in range(65, 91))
# l_e = l_c[13:] + l_c[:13]
# u_e = u_c[13:] + u_c[:13]
# so = ""
# for c in str1:
#     if c in l_c:
#         so = so + l_e[l_c.find(c)]
#     elif c in u_c:
#         so = so + u_e[u_c.find(c)]
#     else:
#         so = so + c

# vas1 = ""

# for i in so:
#     scr1 = str(d1.get(i))
#     vas1 += str(scr1)
# for c in vas1:
#     arr1.append(ord(c))
# arr2 = []
# for i in arr1:
#     if i % 2 == 0:
#         i += 2
#     else:
#         i += 1
#     arr2.append(i)
# saa2t = ""
# for c in arr2:
#     saa2t += chr(c)

# vas2 = ""
# for i in saa2t:
#     scr2 = str(d2.get(i))
#     vas2 += str(scr2)
# sarev = vas2[::-1]
# msg_b = sarev.encode("utf-8")
# print(msg_b)

# reverse decrypt

msg_b = base64.b64decode('JUglWEMyZlo9MkpCPSgoWj1pKDJaPSgoe1M9Q1oiayNYPV1KI0paLUpKU0M=').decode('utf-8')

vas2 = msg_b[::-1]
print(len(vas2))

saa2t = []

for i in vas2:
    # print(d2.get(i))
    saa2t.append(str(d2.get(i)))
    

arr2 = []

for c in saa2t:
    arr2.append(ord(c))

arr1 = []

print(len(arr2))
for i in arr2:
    if d1.get(chr(i-1)) != None:
        # print(d1.get(chr(i-1)))
        arr1.append(i-1)
    if d1.get(chr(i-2)) != None:
        # print(d1.get(chr(i-2)))
        arr1.append(i-2)
    else:
        print("NOTHING IS GONNA WORK")

vas1 = ""
print(len(arr1))
for c in arr1:
    vas1 += chr(c)

print(len(vas1))

so = ""
for c in vas1:
    so += str(d1.get(c))

# print(so)

str1 = ""

l_c = ''.join(chr(c) for c in range(97, 123))
u_c = ''.join(chr(c) for c in range(65, 91))
l_e = l_c[13:] + l_c[:13]
u_e = u_c[13:] + u_c[:13]

for c in so: 
    if c in l_c:
        str1 = str1 + l_c[l_e.find(c)]
    elif c in u_c:
        str1 = str1 + u_c[u_e.find(c)]
    else:
        str1 = str1 + c

print(str1)