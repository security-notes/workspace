from pwn import *
from string import ascii_lowercase
from itertools import product
from math import ceil, log

conn = remote('queensarah2.chal.perfect.blue',1)

cipher = str(conn.recvline_regex(r'{.*}'))[2:-1] # exclude b""
cipher = cipher[2:-2] # exclude {''}
print(cipher)

ALPHABET = ascii_lowercase + "_"
bigrams = set([''.join(bigram) for bigram in product(ALPHABET, repeat=2)])

first_key = 'aa'
key = first_key
cnt = 0
S_box = {}
while cnt < 27*27:
    mapping = []
    while cnt < 27*27:
        obj = {}
        conn.sendline(key)
        value = str(conn.recvline_regex(r'[a-z_]{2}\n'))[2:-1]
        obj[key] = value
        mapping.append(obj)
        if value == first_key:
            break 
        key = value
        cnt += 1
        print("\r"+str((100*cnt)//(27*27))+'%',end="")

    print(mapping)
    print(len(mapping))

    for obj in mapping:
        key = list(obj.keys())[0]
        value = list(obj.values())[0]
        S_box[key] = value

    # print(S_box)
    # print(len(S_box))

    first_key = list(bigrams - set(S_box.keys()))
    if len(first_key) == 0:
        break
    first_key = first_key[0]
    key = first_key

S_box_inv = { v:k for k, v in S_box.items()} # 逆対応表
print(S_box_inv)
print(len(S_box_inv))

rounds = int(2 * ceil(log(len(cipher), 2)))
mid = len(cipher)//2

cipher = list(cipher)
# Decript
## 最初の1回はシャッフルしない
for i in range(0, len(cipher), 2):
    cipher[i:i+2] = S_box_inv[''.join(cipher[i:i+2])]

## シャッフル + 変換 
for _ in range(rounds+1):
    cipher_shuffle = ''
    for i in range(mid):
        cipher_shuffle += cipher[i] + cipher[i+mid]
    cipher = list(cipher_shuffle)
    for i in range(0, len(cipher), 2):
        cipher[i:i+2] = S_box_inv[''.join(cipher[i:i+2])]

    print(cipher)

conn.close()