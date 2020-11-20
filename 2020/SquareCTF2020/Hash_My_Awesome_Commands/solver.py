from pwn import *
import base64
import struct
import re

conn = remote('challenges.2020.squarectf.com',9020)

# debug mode
conn.recvuntil('Enter command:',drop=True)
conn.sendline('debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=')
conn.recvuntil('Enter command:',drop=True)

result = [0 for _ in range(2**8)]

payload = b''

# payload = b'\x9d\xd0(K<\x7f\t\xb8\xb3N\xa3A\x07\x973\xde\xde\x97\x18Q\x06m\x0c\x08s\xd8\xbbI\xac\x20\x4c'

for j in range(1,33):

    buf = b'\x00'*(32-j)

    top = [k for k in range(2**8)]
    while len(top) != 1:
        for i in range(2**8):
            if i not in top:
                continue
            data = struct.pack("B",i) # \x00 - \xff
            data = payload + data + buf
            b64_data = base64.b64encode(data).decode()
            conn.sendline('flag|' + b64_data)
            conn.recvline()
            msg = conn.recvline().decode() # time info
            varify_time = int(re.sub(r"\D","",msg)) 
            result[i] = [varify_time,i]
            print(i,msg,end='') # for debug
            skip = conn.recvuntil('Enter command:',drop=True)
            if(j == 32):
                print(skip) # flag check

        sort_result = sorted(result,reverse=True)
        topgroup = [x[1] for x in sort_result][:10] # just in case
        top = [x for x in top if x in topgroup]
        print('top: ', top)

    payload += struct.pack("B",top[0])
    print('payload: ', payload)