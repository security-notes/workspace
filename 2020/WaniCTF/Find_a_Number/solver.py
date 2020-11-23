from pwn import *

conn = remote('number.wanictf.org',60000)
n_min, n_max = 0, 500000

while True:

    conn.recvuntil('input:')
    mid = (n_min + n_max) // 2
    conn.sendline(str(mid))

    msg = str(conn.recvlines(2))

    if 'small' in msg:
        n_min = mid
    elif 'big' in msg:
        n_max = mid
    else:
        print(msg)
        break