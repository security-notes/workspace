from pwn import *

conn = remote('l0g0n.wanictf.org',50002)

cnt = 0
while True:
    cnt += 1
    #　client_challenge -> server_credential
    conn.sendline('00') # any 1byte
    conn.recvuntil('>')
    # client_credential
    conn.sendline('50') # any 1byte
    conn.recvuntil('>')

    msg = str(conn.recvline())
    print(cnt,msg)
    if 'OK' in msg: # 1/256
        break

conn.close()