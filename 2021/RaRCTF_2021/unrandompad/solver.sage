from pwn import *
import re
from Crypto.Util.number import *

e, n, c = 3, [], []

for _ in range(3):
    io = remote('193.57.159.27', 28572)
    io.recvline() # e
    n.append(int(re.search(r'n: (\d+)' , str(io.recvline())).group(1)))

    io.recvuntil('opt: ')
    io.sendline('2')
    c.append(int(re.search(r'c: (\d+)' , str(io.recvline())).group(1)))
    io.close()

x = CRT_list(c,n)

print(long_to_bytes(x^(1/e)))
