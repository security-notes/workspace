import os
os.environ['PWNLIB_NOTERM'] = 'True' # sage & pwntools

from pwn import *
import re

io = remote('crt.cry.wanictf.org','50000')
P = Primes()

p = 1
rets, primes = [], []
while True:
    p = P.next(p)
    if p > 300:
        break
    io.recvuntil('Mod > ')
    io.sendline(str(p))
    ret = int(re.sub(r'\D','',io.recvline().decode('utf-8')))
    rets.append(ret)
    primes.append(p)

flag = CRT_list(rets,primes)

assert flag <= 10 ** 103

print(bytes.fromhex(hex(flag)[2:]))
