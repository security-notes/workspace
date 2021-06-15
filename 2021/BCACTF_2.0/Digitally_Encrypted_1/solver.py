from pwn import *

cipher = open('encrypted.txt','r').read().split(' ')
key = 'd4c70f8a67d5456d'
plain = b''

for c in cipher:
    plain += xor(bytes.fromhex(c),bytes.fromhex(key))

print(plain)